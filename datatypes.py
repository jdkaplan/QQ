from collections import deque
from dataclasses import dataclass

class ASQ:
    pass


@dataclass(frozen=True)
class Statement(ASQ):
    pass


@dataclass(frozen=True)
class Boolean:
    value: bool

    def execute(self, env):
        env.qframe.append(self)


@dataclass(frozen=True)
class Number(Statement):
    value: str

    def execute(self, env):
        env.qframe.append(self)


@dataclass(frozen=True)
class String(Statement):
    value: str

    def execute(self, env):
        env.qframe.append(self)


@dataclass(frozen=True)
class Block:
    statements: list[Statement]

    def execute(self, env):
        env.qframe.append(Queue(self.statements))


class Queue(ASQ):
    def __init__(self, statements):
        self.statements = deque(statements)

    def execute(self, env):
        while self.statements:
            inst = self.statements.popleft()
            inst.execute(env)

    def pop(self):
        self.statements.popleft()

    def push(self, value):
        self.statements.append(value)

    def __eq__(self, other):
        return type(self) == type(other) and self.statements == other.statements
