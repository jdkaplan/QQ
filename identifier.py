import fn_operations
import math_operations
import qqio
import queue
import cond

identifiers = {
    'call': fn_operations.FnCall,
    'def': fn_operations.FnDef,
    'ret': fn_operations.Ret,
    '+': math_operations.Add,
    '-': math_operations.Sub,
    '*': math_operations.Mul,
    '/': math_operations.Div,
    '%': math_operations.Mod,
    '**': math_operations.Exp,
    '&': math_operations.BitAnd,
    '|': math_operations.BitOr,
    '^': math_operations.BitXor,
    'QQ': qqio.QQ,
    'read_line': qqio.ReadLine,
    'read_num': qqio.ReadNumber,
    'print': qqio.Print,
    'write': qqio.Write,
    'rot': queue.Rot,
    'rrot': queue.RRot,
    'qrot': queue.QRot,
    'pop': queue.Pop,
    'rpop': queue.RPop,
    'qpop': queue.QPop,
    'push': queue.Push,
    'rpush': queue.RPush,
    'qpush': queue.QPush,
    'drain': queue.Drain,
    'rdrain': queue.RDrain,
    'qdrain': queue.QDrain,
    'rqalloc': queue.RQAlloc,
    'pack': queue.Pack,
    'if': cond.If,
    'ifelse': cond.IfElse,
    'not': cond.Not,
    '==': cond.Equals,
    '!=': cond.NotEquals,
    '<': cond.LessThan,
    '<=': cond.LessThanEquals,
    '>': cond.GreaterThan,
    '>=': cond.GreaterThanEquals,
}


def Identifier(name):
    global identifiers
    return identifiers[name]()
