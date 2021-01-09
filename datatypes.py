class Number:
    def __init__(self, flt):
        self.val = flt

    def execute(self, qframe):
        qframe.push(self)

class String:
    def __init__(self, s):
        self.val = s

    def execute(self, qframe):
        qframe.push(self)

class Block:
    # TODO
    def __init__(self, contents):
        self.contents = contents

    def execute(self, qframe):
        qframe.push(Queue(self.contents))

class Queue:
    # TODO
    def __init__(self, contents):
        self.contents = contents

    def execute(self, qframe):
        while self.contents:
            inst = self.contents.pop()
            inst.execute(qframe)
