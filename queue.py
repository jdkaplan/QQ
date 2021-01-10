from collections import deque

import datatypes
import exceptions
import pprint


class RQueue:
    def __init__(self, size):
        self.q = deque([])
        self.size = size

    def push(self, val):
        assert self.size <= len(self.q)
        if self.size == len(self.q):
            raise exceptions.QQError("Register queue is full.")
        self.q.append(val)

    def pop(self):
        return self.q.pop()


class RQAlloc:
    def execute(self, env):
        if env.rqueue is not None:
            raise exceptions.QQError("Register queue is already allocated")
        size = env.qframe.pop()
        env.rqueue = RQueue(size)


class QueueFrameBase:
    def get_queue(self, env):
        pass

    def return_queue(self, env):
        pass

    def pop(self, env):
        return env.qframe.pop()

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
        self.queue = env.qframe.pop()

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
        self.return_queue()


class Rot(RotBase, QueueFrameBase): pass
class RRot(RotBase, RegisterQueueBase): pass
class QRot(RotBase, QQueueBase): pass


class PopBase:
    def execute(self, env):
        self.get_queue(env)
        self.pop(env)
        self.return_queue()


class Pop(PopBase, QueueFrameBase): pass
class RPop(PopBase, RegisterQueueBase): pass
class QPop(PopBase, QQueueBase): pass


class PushBase:
    def execute(self, env):
        self.get_queue(env)
        self.push(env, env.qframe.pop())
        self.return_queue()


class Push(PushBase, QueueFrameBase): pass  # This is the same as Rot, but left it for funsies
class RPush(PushBase, RegisterQueueBase): pass
class QPush(PushBase, QQueueBase): pass
