import command

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
    value: float

    def execute(self, env):
        env.qframe.append(self)


@dataclass(frozen=True)
class String(Statement):
    value: str

    def execute(self, env):
        env.qframe.append(self)


class Block(ASQ):
    def __init__(self, statements):
        self.statements = deque(statements)

    def execute(self, env):
        env.qframe.append(Queue(self.statements))

    def __eq__(self, other):
        return type(self) == type(other) and self.statements == other.statements

    def __repr__(self):
        return f"<{type(self).__name__}(statements={repr(self.statements)})>"


class Queue(ASQ):
    def __init__(self, statements):
        self.statements = deque(statements)

    def execute(self, env):
        while self.statements:
            inst = self.statements.popleft()
            term = inst.execute(env)
            if term != command.NO_TERMINATE:
                return term

    def pop(self):
        self.statements.popleft()

    def push(self, value):
        self.statements.append(value)

    def __eq__(self, other):
        return type(self) == type(other) and self.statements == other.statements

    def __repr__(self):
        return f"<{type(self).__name__}(statements={repr(self.statements)})>"
