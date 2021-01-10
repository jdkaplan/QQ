class BinOp:
    def execute(self, env):
        l, r = env.qframe.pop(), env.qframe.pop()
        env.qframe.push(type(l)(self.op(l.value, r.value)))


class Add(BinOp):
    op = lambda l, r: l + r


class Sub(BinOp):
    op = lambda l, r: l - r


class Mul(BinOp):
    op = lambda l, r: l * r


class Div(BinOp):
    op = lambda l, r: l / r


class Mod(BinOp):
    op = lambda l, r: l % r


class Exp(BinOp):
    op = lambda l, r: l ** r


class BitAnd(BinOp):
    op = lambda l, r: l & r


class BitOr(BinOp):
    op = lambda l, r: l | r


class BitXor(BinOp):
    op = lambda l, r: l ^ r
