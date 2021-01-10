from collections import deque

class Env:
    def __init__(self, qframe=None, rqueue=None, fnqueue=None):
        self.qframe = qframe if qframe is not None else deque()
        self.rqueue = rqueue
        self.fnqueue = fnqueue if fnqueue is not None else {}
