import datatypes
import pprint

from command import Command

class QQ(Command):
    def execute(self, env):
        pprint.pprint(list(env.qframe), compact=True)
        exit(1)


class ReadLine(Command):
    def execute(self, env):
        env.qframe.append(datatypes.String(input()))


class ReadNumber(Command):
    def execute(self, env):
        env.qframe.append(datatypes.Number(int(input())))


class Print(Command):
    def execute(self, env):
        print(str(env.qframe[0]))


class Write(Command):
    def execute(self, env):
        print(str(env.qframe[0]), end='')
