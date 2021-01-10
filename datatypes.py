import command

from collections import deque
from dataclasses import dataclass

class ASQ:
    pass


class ValueCopy:
    def copy(self):
        return type(self)(self.value)


@dataclass(frozen=True)
class Statement(ASQ):
    pass


@dataclass(frozen=True)
class Boolean(Statement, ValueCopy):
    value: bool

    def execute(self, env):
        env.qframe.append(self)

    def __str__(self):
        return str(self.value)


@dataclass(frozen=True)
class Number(Statement, ValueCopy):
    value: int

    def execute(self, env):
        env.qframe.append(self)

    def __str__(self):
        return str(self.value)


@dataclass(frozen=True)
class String(Statement, ValueCopy):
    value: str

    def execute(self, env):
        env.qframe.append(self)

    def __str__(self):
        return self.value


class Block(ASQ):
    def __init__(self, statements):
        self.statements = deque(statements)

    def execute(self, env):
        env.qframe.append(Queue(self.statements))

    def __eq__(self, other):
        return type(self) == type(other) and self.statements == other.statements

    def __repr__(self):
        return f"{type(self).__name__}(statements={repr(self.statements)})"

    def __str__(self):
        return repr(self)

    def copy(self):
        return Block([s.copy() for s in self.statements])



class Queue(ASQ):
    def __init__(self, statements):
        self.statements = deque(statements)

    def execute(self, env):
        while self.statements:
            inst = self.statements.popleft()
            term = inst.execute(env)
            if term != command.NO_TERMINATE:
                return term

    def execute_loop(self, env):
        while self.statements:
            inst = self.statements.popleft()
            self.statements.append(inst.copy())
            term = inst.execute(env)
            if term != command.NO_TERMINATE:
                return term

    def pop(self):
        return self.statements.popleft()

    def push(self, value):
        self.statements.append(value)

    def __eq__(self, other):
        return type(self) == type(other) and self.statements == other.statements

    def __repr__(self):
        return f"{type(self).__name__}(statements={repr(self.statements)})"

    def __str__(self):
        return repr(self)

    def copy(self):
        return Queue([s.copy() for s in self.statements])
