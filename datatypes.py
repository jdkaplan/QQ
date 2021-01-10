class Boolean:
    def __init__(self, truth):
        self.val = truth

    def execute(self, env):
        env.qframe.push(self)

class Number:
    def __init__(self, flt):
        self.val = flt

    def execute(self, env):
        env.qframe.push(self)

class String:
    def __init__(self, s):
        self.val = s

    def execute(self, env):
        env.qframe.push(self)

class Block:
    def __init__(self, contents):
        self.contents = contents

    def execute(self, env):
        env.qframe.push(Queue(self.contents))

class Queue:
    def __init__(self, contents):
        self.contents = contents

    def execute(self, env):
        while self.contents:
            inst = self.contents.pop()
            inst.execute(env)
