# QQ: *The* Queue-Based Programming Language

_Winner of the `-03`, "30 minutes or it's free", and "self-documenting" awards from Quirky Languages Done Quick!_

_Note:  This language is a WIP MVP for the QLDQ mini-hackathon.  It has some rough edges, and there are no promises or expectations that these will ever be polished away.  Feel free to fork if you want to modify or improve (within MIT license allowances), and have fun!  We'd be glad to hear about anything cool you come up with :)_

A programming language built on the oft-overshadowed datatype, the queue.  While languages like Forth and its ilk are based on stacks, QQ strives to take the road less travelled.  QQ is a language whose power is that every advanced data structure, including the frame itself, is a form of queue.

And it's clearly very intuitive to use.

## Rites of Passage

Here are some of the programs that language designers are contractually obligated to write:

<details><summary>hello_world.qq</summary>

```
"hello world"
print
```

</details>

<details><summary>fizz_buzz.qq</summary>

```
"fizzbuzz"
[
  dup

  100
  rot
  >
  [ ret ]
  rot
  if

  dup

  3
  rot
  %
  [
    dup

    5 rot
    %
    [ print ]
    [ "buzz" rot print pop ]
    rot
    ifelse
  ]
  [
    "fizz" rot write pop
    dup

    5 rot
    %
    [ " " rot print pop ]
    [ "buzz" rot print pop ]
    rot
    ifelse
  ]
  rot
  ifelse

  1
  +
  1
  rot
  pack

  "fizzbuzz"
  rot
  call
]
def

"fizzbuzz"
[ 1 ]
call
```
</details>

<details><summary>factorial.qq</summary>

```
"factorial"
[
    dup
    1
    rot
    !=
    [
        dup
        [ ]
        dec
        rot
        "factorial"
        qpush
        rot
        call

        rot
        exec
        *
    ]
    rot
    if
]
def

"loop_factorial"
[
    [
        1
        dup
        rot
        ==
        [ break ]
        dec
        rot
        if
        dup
        *
    ]
    dup
    loop
    pop
]
def


"factorial"
[ 10 ]
call
exec
print
pop

"loop_factorial"
[ 10 ]
call
exec
print
```
</details>

## Memory Model

There are in essence two places to store data.  Unlike many "modern" programming languages, QQ eschews the use of random access variables.  The only nameable things by default are functions, but everything else lives in a queue.

The main queue, which can become arbitrarily large, is called the **qframe**.  It is the default space to store things and so serves as memory.  **qframes** are scoped so that each function call takes place with its own **qframe**.

There is a secondary queue for convenience known as the *register queue*, and it can be allocated within a function using the `rqalloc` command.  When a register queue is allocated, a size must be specified, and the register queue that is created cannot hold more elements than its size.  This makes it useful primarily as an alternative place to store data that is used repeatedly, but otherwise behaves like a normal queue.

Additionally, one can create additional **Queues**, but they are not independent and must be stored inside of either the **qframe** or the register queue.  More on that in the datatypes section.

## Datatypes

There are 4 different types of objects that can be put into memory: **Integers**, **Strings**, **Booleans**, and **Queues**.

**Integers** can be any whole number and behave like arbitrary-precision integers.  Think of them like you do in Python or most other modern languages for the sake of basic arithmetic.

**Strings** can be of arbitrary length and have basic functionality for printing and concatenation (using `+`).

**Booleans** can be `true` or `false` and are primarily used in conditions.

**Queues** are special, in that they can contain both data and operations.  This is because a **Queue** can be used both for storing data and for storing instructions, like a code block.

## Basic Operations

QQ supports many basic binary math operations for its **Integers**, including `+ - * / % ** & | ^ == != < <= > >=` (where `^` is bitwise xor and `**` is exponentiation).

Each of these operations pops the two elements off the front of the queue, performs the operation between them (using the frontmost element on the left side), and enqueues the result of the calculation.  The comparison operations return **Booleans**.

QQ also supports some unary operations for basic datatypes: `not`, `inc`, and `dec` (for increment and decrement respectively).  They pop off only one element, apply the transformation, and then enqueue the result.

There is also the `dup` operation, which works on any datatype, popping off the element at the front of the queue and enqueuing it twice.  This is useful for when you want to use something for calculation but then want to also be able to refer to it again.

Each of these operations by default operate on the current **qframe**, but they also have variants to operate on other queues.  Prefixing any of these operations with `r` causes it to instead refer to the _register queue_, and prefixing any of them with `q` causes it to refer to the **Queue** object on the front of the current **qframe**

## Queue Management

Sometimes one may want to simply remove something from a queue or transfer it to another queue.  To do this, QQ offers some builtins for managing queues of all sorts.

`rot` is a crucial operation for success.  It pops from the front of the queue and then pushes that same element to the back, rotating the queue.  Like the operations above, it has an `r` and `q` variant which operate on the register queue and **Queue** objects, respectively.

`pop` behaves slightly differently depending on if it is used on the **qframe**.  If it is, then it simply discards the element at the front of the **qframe**.  Its variants instead pop the element from the front of the relevant queue and enqueue it on the **qframe**.

`push` similarly varies depending on its target.  In its default form, it is identical to `rot`, rotating the **qframe**, but its primary utility is in moving things from the **qframe** onto another queue.  `rpush` and `qpush` will take the element from the front of the **qframe** and push it onto the relevant queue.

`drain` completely empties out the queue it is used on.

`rqalloc`, mentioned above, takes a single argument and creates a register queue of that size.  Note that you can only have one register queue at any given scope.

`pack` is used to take several consecutive elements from the **qframe** and pack them together into a **Queue** object, which it then puts onto the back of the **qframe**.  When using it, the element at the front serves to tell `pack` how many elements to pack together, and then that many subsequent elements are used to form the queue.

`exec` takes the element off the front of the **qframe** and executes it like a program.  Note this only works on **Queues**.  This is also an effective way to "unpack" a queue primarily used for storing data.

## Control Flow

There are three primary ways to do control flow in QQ: `if`, `ifelse`, `loop`, and the special `rifbreak`.

`if` is an operation that takes two elements off the queue.  The first is the *condition*.  The second is the *consequent*, which should be a **Queue**.  If the condition is truthy, the consequent is executed by treating it as if it were itself a program (though in the current scope), executing each element in it one by one in order.  In either case, the condition and the consequent are not re-enqueued.

`ifelse` is very much like `if`, but takes three elements.  The first two are the same as `if`, but the third is the `alternate`, which is executed if the condition is falsey.

`loop` takes a single element off the queue, which is the loop body.  It is executed like the consequent above, but unconditionally.  Additionally, as the queue is executed, each element is preserved and re-enqueued on the loop body, so that it gets executed again once the loop comes around.  The only way to exit the loop is via either `break` or `rifbreak`

`rifbreak` is a special condition check, which takes its condition from the front of the register queue, and if true, breaks out of the current loop.

## Functions

QQ provides some basic capabilities for defining and calling functions.  Functions are unique from simple queues as code blocks in that they have their own **qframe** during execution.  They are defined using `def` and called using `call`, and have the convenience of being the only thing stored outside of the queues described above, meaning they are accessible at any time.

`def` takes two elements off the front of the **qframe**: the name of the function (which should be a **String**) and the body of the function (which should be a **Queue**).  This body is then forever associated with the name.

`call` takes two elements off of the front.  The first should be the function name (again a **string**), and then a **Queue** that will become the **qframe** for that particular execution of the function.  This queue can be filled with anything that the function expects to have as its initial **qframe**.  After execution of the function, the callee's (probably mutated) **qframe** will be enqueued onto the caller's **qframe**.

A function terminates by either executing its final instruction or by executing the `ret` instruction, which takes no arguments, since the return value is always the **qframe**.

## IO

QQ provides some basic IO operations: `write`, `print`, and `QQ`.

`write` and `print` both print out the element at the front of the queue (without popping it off), but cannot access anything other than the frontmost element of the queue.  They differ only in that `print` adds an extra trailing newline that `write` doesn't.

`QQ` is a signal to the computer that you are now in tears.  As a mercy, it prints the entire **qframe** and then terminates the program to spare you from further harm.

## Running

Currently, QQ is run by executing the `evaluator.py` program with Python 3.9+.  If given a filename afterwards, QQ will execute the whole file.  Otherwise, it will put you into an interactive shell.

You can find some example programs in the `test_programs` directory.
