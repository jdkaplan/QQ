from collections import deque
from dataclasses import dataclass

class ASQ:
    pass


@dataclass(frozen=True)
class Statement(ASQ):
    pass


@dataclass(frozen=True)
class Identifier(Statement):
    name: str


@dataclass
class Boolean:
    def __init__(self, truth):
        self.value = truth

    def execute(self, env):
        env.qframe.push(self)


@dataclass(frozen=True)
class Number(Statement):
    value: str

    def execute(self, env):
        env.qframe.push(self)


@dataclass(frozen=True)
class String(Statement):
    value: str

    def execute(self, env):
        env.qframe.push(self)


class Block:
    def __init__(self, contents):
        self.contents = contents

    def execute(self, env):
        env.qframe.push(Queue(self.contents))


@dataclass(frozen=True)
class Queue(ASQ):
    statements: list[Statement]

    def execute(self, env):
        while self.statements:
            inst = self.statements.pop()
            inst.execute(env)

    def pop(self):
        self.statements.pop()

    def push(self, value):
        self.statements.append(value)
