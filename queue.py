from collections import deque

import datatypes
import exceptions
import pprint
from command import Command

class RQueue(Command):
    def __init__(self, size):
        self.q = deque([])
        self.size = size

    def push(self, val):
        assert self.size <= len(self.q)
        if self.size == len(self.q):
            raise exceptions.QQError("Register queue is full.")
        self.q.append(val)

    def pop(self):
        return self.q.popleft()


class RQAlloc(Command):
    def execute(self, env):
        if env.rqueue is not None:
            raise exceptions.QQError("Register queue is already allocated")
        size = env.qframe.popleft()
        env.rqueue = RQueue(size)


class QueueFrameBase:
    def get_queue(self, env):
        pass

    def return_queue(self, env):
        pass

    def pop(self, env):
        return env.qframe.popleft()

    def push(self, env, val):
        env.qframe.append(val)


class RegisterQueueBase:
    def get_queue(self, env):
        pass

    def return_queue(self, env):
        pass

    def pop(self, env):
        if env.rqueue is None:
            raise exceptions.QQError("Register queue is not allocated")

        return env.rqueue.pop()

    def push(self, env, val):
        if env.rqueue is None:
            raise exceptions.QQError("Register queue is not allocated")

        env.rqueue.push()


class QQueueBase:
    def get_queue(self, env):
        if type(env.qframe[0]) != datatypes.Queue:
            raise exceptions.QQException("Element at front of queue is not a Queue")
        self.queue = env.qframe.popleft()

    def return_queue(self, env):
        env.qframe.append(self.queue)

    def pop(self, env):
        return self.queue.pop()

    def push(self, env, val):
        self.queue.push(val)


class RotBase:
    def execute(self, env):
        self.get_queue(env)
        self.push(env, self.pop(env))
        self.return_queue(env)


class Rot(Command, RotBase, QueueFrameBase): pass
class RRot(Command, RotBase, RegisterQueueBase): pass
class QRot(Command, RotBase, QQueueBase): pass


class PopBase:
    def execute(self, env):
        self.get_queue(env)
        self.pop(env)
        self.return_queue(env)


class Pop(Command, PopBase, QueueFrameBase): pass
class RPop(Command, PopBase, RegisterQueueBase): pass
class QPop(Command, PopBase, QQueueBase): pass


class PushBase:
    def execute(self, env):
        self.get_queue(env)
        self.push(env, env.qframe.popleft())
        self.return_queue(env)


class Push(Command, PushBase, QueueFrameBase): pass  # This is the same as Rot, but left it for funsies
class RPush(Command, PushBase, RegisterQueueBase): pass
class QPush(Command, PushBase, QQueueBase): pass


class DrainBase:
    def execute(self, env):
        self.get_queue(env)
        try:
            while True:
                self.pop(env)
        except IndexError:
            pass
        self.return_queue(env)


class Drain(Command, DrainBase, QueueFrameBase): pass  # This is the same as Rot, but left it for funsies
class RDrain(Command, DrainBase, RegisterQueueBase): pass
class QDrain(Command, DrainBase, QQueueBase): pass


class Pack(Command):
    def execute(self, env):
        size = env.qframe.popleft()
        new_q = datatypes.Queue([env.qframe.popleft() for _ in range(size)])
        env.qframe.append(new_q)
