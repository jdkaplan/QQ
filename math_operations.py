from command import Command

class BinOp(Command):
    def execute(self, env):
        l, r = env.qframe.popleft(), env.qframe.popleft()
        env.qframe.append(type(l)(self.op(l.value, r.value)))


class Add(BinOp):
    op = lambda self, l, r: l + r


class Sub(BinOp):
    op = lambda self, l, r: l - r


class Mul(BinOp):
    op = lambda self, l, r: l * r


class Div(BinOp):
    op = lambda self, l, r: l / r


class Mod(BinOp):
    op = lambda self, l, r: l % r


class Exp(BinOp):
    op = lambda self, l, r: l ** r


class BitAnd(BinOp):
    op = lambda self, l, r: l & r


class BitOr(BinOp):
    op = lambda self, l, r: l | r


class BitXor(BinOp):
    op = lambda self, l, r: l ^ r


class Inc(Command):
    def execute(self, env):
        v = env.qframe.popleft()
        env.qframe.append(type(v)(v.value + 1))


class Dec(Command):
    def execute(self, env):
        v = env.qframe.popleft()
        env.qframe.append(type(v)(v.value - 1))
