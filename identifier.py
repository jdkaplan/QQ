import fn_operations
import math_operations
import qqio
import queue

identifiers = {
    'call': fn_operations.FnCall,
    'def': fn_operations.FnDef,
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
    'rot': queue.Rot,
    'rrot': queue.RRot,
    'qrot': queue.QRot,
    'pop': queue.Pop,
    'rpop': queue.RPop,
    'qpop': queue.QPop,
    'push': queue.Push,
    'rpush': queue.RPush,
    'qpush': queue.QPush,
    'rqalloc': queue.RQAlloc,
    'pack': queue.Pack,
}


def Identifier(name):
    global identifiers
    return identifiers[name]()
