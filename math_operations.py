from command import Command
from queue import (
    QueueFrameBase,
    RegisterQueueBase,
    QQueueBase
)

class BinOpBase:
    def execute(self, env):
        self.get_queue(env)
        l, r = self.pop(env), self.pop(env)
        self.push(env, type(l)(self.op(l.value, r.value)))
        self.return_queue(env)


class AddBase(BinOpBase):
    op = lambda self, l, r: l + r


class Add(Command, AddBase, QueueFrameBase): pass
class RAdd(Command, AddBase, RegisterQueueBase): pass
class QAdd(Command, AddBase, QQueueBase): pass


class SubBase(BinOpBase):
    op = lambda self, l, r: l - r


class Sub(Command, SubBase, QueueFrameBase): pass
class RSub(Command, SubBase, RegisterQueueBase): pass
class QSub(Command, SubBase, QQueueBase): pass


class MulBase(BinOpBase):
    op = lambda self, l, r: l * r


class Mul(Command, MulBase, QueueFrameBase): pass
class RMul(Command, MulBase, RegisterQueueBase): pass
class QMul(Command, MulBase, QQueueBase): pass


class DivBase(BinOpBase):
    op = lambda self, l, r: l / r


class Div(Command, DivBase, QueueFrameBase): pass
class RDiv(Command, DivBase, RegisterQueueBase): pass
class QDiv(Command, DivBase, QQueueBase): pass


class ModBase(BinOpBase):
    op = lambda self, l, r: l % r


class Mod(Command, ModBase, QueueFrameBase): pass
class RMod(Command, ModBase, RegisterQueueBase): pass
class QMod(Command, ModBase, QQueueBase): pass


class ExpBase(BinOpBase):
    op = lambda self, l, r: l ** r


class Exp(Command, ExpBase, QueueFrameBase): pass
class RExp(Command, ExpBase, RegisterQueueBase): pass
class QExp(Command, ExpBase, QQueueBase): pass


class BitAndBase(BinOpBase):
    op = lambda self, l, r: l & r


class BitAnd(Command, BitAndBase, QueueFrameBase): pass
class RBitAnd(Command, BitAndBase, RegisterQueueBase): pass
class QBitAnd(Command, BitAndBase, QQueueBase): pass


class BitOrBase(BinOpBase):
    op = lambda self, l, r: l | r


class BitOr(Command, BitOrBase, QueueFrameBase): pass
class RBitOr(Command, BitOrBase, RegisterQueueBase): pass
class QBitOr(Command, BitOrBase, QQueueBase): pass


class BitXorBase(BinOpBase):
    op = lambda self, l, r: l ^ r


class BitXor(Command, BitXorBase, QueueFrameBase): pass
class RBitXor(Command, BitXorBase, RegisterQueueBase): pass
class QBitXor(Command, BitXorBase, QQueueBase): pass


class IncBase:
    def execute(self, env):
        self.get_queue(env)
        v = self.pop(env)
        self.push(env, type(v)(v.value + 1))
        self.return_queue(env)


class Inc(Command, IncBase, QueueFrameBase): pass
class RInc(Command, IncBase, RegisterQueueBase): pass
class QInc(Command, IncBase, QQueueBase): pass


class DecBase:
    def execute(self, env):
        self.get_queue(env)
        v = self.pop(env)
        self.push(env, type(v)(v.value - 1))
        self.return_queue(env)


class Dec(Command, DecBase, QueueFrameBase): pass
class RDec(Command, DecBase, RegisterQueueBase): pass
class QDec(Command, DecBase, QQueueBase): pass
