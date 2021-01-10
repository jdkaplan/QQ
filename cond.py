import datatypes
import exceptions
import math_operations
import command


class If(command.Command):
    def execute(self, env):
        if len(env.qframe) < 2 or type(env.qframe[1]) != datatypes.Queue:
            raise QQError("If statement needs a condition and code block in the front of the queue.")
        cond = env.qframe.popleft()
        consequent = env.qframe.popleft()

        res = bool(cond.value)
        env.qframe.append(res)
        if res:
            return consequent.execute(env)


class IfElse(command.Command):
    def execute(self, env):
        if len(env.qframe) < 2 or type(env.qframe[1]) != datatypes.Queue:
            raise QQError("If statement needs a condition and code block in the front of the queue.")
        cond = env.qframe.popleft()
        consequent = env.qframe.popleft()
        alternative = env.qframe.popleft()

        res = bool(cond.value)
        env.qframe.append(res)
        if res:
            return consequent.execute(env)
        else:
            return alternative.execute(env)


class Not(command.Command):
    def execute(self, env):
        env.qframe.append(datatypes.Boolean(not env.qframe.popleft()))


class BoolBinOp(command.Command):
    def execute(self, env):
        l, r = env.qframe.popleft(), env.qframe.popleft()
        env.qframe.append(datatypes.Boolean(self.op(l.value, r.value)))

    def __eq__(self, other):
        return type(self) == type(other)


class Equals(BoolBinOp):
    op = lambda self, l, r: l == r


class NotEquals(BoolBinOp):
    op = lambda self, l, r: l != r


class LessThan(BoolBinOp):
    op = lambda self, l, r: l < r


class LessThanEquals(BoolBinOp):
    op = lambda self, l, r: l <= r


class GreaterThan(BoolBinOp):
    op = lambda self, l, r: l > r


class GreaterThanEquals(BoolBinOp):
    op = lambda self, l, r: l >= r
