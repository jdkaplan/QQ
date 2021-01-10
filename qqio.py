import datatypes
import pprint

class QQ:
    def execute(self, env):
        pprint.pprint(list(env.qframe), compact=True)
        exit(1)


class ReadLine:
    def execute(self, env):
        env.qframe.append(datatypes.String(input()))


class ReadNumber:
    def execute(self, env):
        env.qframe.append(datatypes.Number(float(input())))


class Print:
    def execute(self, env):
        print(env.qframe[0].value, end='')
