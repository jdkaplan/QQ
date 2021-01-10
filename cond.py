import datatypes
import exceptions
import math_operations
import command
import queue


class If(command.Command):
    def execute(self, env):
        if len(env.qframe) < 2 or type(env.qframe[1]) != datatypes.Queue:
            raise exceptions.QQError("If statement needs a condition and code block in the front of the queue.")

        cond = env.qframe.popleft()
        consequent = env.qframe.popleft()

        if bool(cond.value):
            return consequent.execute(env)


class IfElse(command.Command):
    def execute(self, env):
        if len(env.qframe) < 2 or type(env.qframe[1]) != datatypes.Queue:
            raise exceptions.QQError("If statement needs a condition and code block in the front of the queue.")
        cond = env.qframe.popleft()
        consequent = env.qframe.popleft()
        alternative = env.qframe.popleft()

        if bool(cond.value):
            return consequent.execute(env)
        else:
            return alternative.execute(env)


class NotBase:
    def execute(self, env):
        self.get_queue(env)
        self.push(env, datatypes.Boolean(not self.pop(env).value))
        self.return_queue(env)


class Not(command.Command, NotBase, queue.QueueFrameBase): pass
class RNot(command.Command, NotBase, queue.RegisterQueueBase): pass
class QNot(command.Command, NotBase, queue.QQueueBase): pass


class BoolBinOpBase:
    def execute(self, env):
        self.get_queue(env)
        l, r = self.pop(env), self.pop(env)
        self.push(env, datatypes.Boolean(self.op(l.value, r.value)))
        self.return_queue(env)


class EqualsBase(BoolBinOpBase):
    op = lambda self, l, r: l == r


class Equals(command.Command, EqualsBase, queue.QueueFrameBase): pass
class REquals(command.Command, EqualsBase, queue.RegisterQueueBase): pass
class QEquals(command.Command, EqualsBase, queue.QQueueBase): pass


class NotEqualsBase(BoolBinOpBase):
    op = lambda self, l, r: l != r


class NotEquals(command.Command, NotEqualsBase, queue.QueueFrameBase): pass
class RNotEquals(command.Command, NotEqualsBase, queue.RegisterQueueBase): pass
class QNotEquals(command.Command, NotEqualsBase, queue.QQueueBase): pass


class LessThanBase(BoolBinOpBase):
    op = lambda self, l, r: l < r


class LessThan(command.Command, LessThanBase, queue.QueueFrameBase): pass
class RLessThan(command.Command, LessThanBase, queue.RegisterQueueBase): pass
class QLessThan(command.Command, LessThanBase, queue.QQueueBase): pass


class LessThanEqualsBase(BoolBinOpBase):
    op = lambda self, l, r: l <= r


class LessThanEquals(command.Command, LessThanEqualsBase, queue.QueueFrameBase): pass
class RLessThanEquals(command.Command, LessThanEqualsBase, queue.RegisterQueueBase): pass
class QLessThanEquals(command.Command, LessThanEqualsBase, queue.QQueueBase): pass


class GreaterThanBase(BoolBinOpBase):
    op = lambda self, l, r: l > r


class GreaterThan(command.Command, GreaterThanBase, queue.QueueFrameBase): pass
class RGreaterThan(command.Command, GreaterThanBase, queue.RegisterQueueBase): pass
class QGreaterThan(command.Command, GreaterThanBase, queue.QQueueBase): pass


class GreaterThanEqualsBase(BoolBinOpBase):
    op = lambda self, l, r: l >= r


class GreaterThanEquals(command.Command, GreaterThanEqualsBase, queue.QueueFrameBase): pass
class RGreaterThanEquals(command.Command, GreaterThanEqualsBase, queue.RegisterQueueBase): pass
class QGreaterThanEquals(command.Command, GreaterThanEqualsBase, queue.QQueueBase): pass
