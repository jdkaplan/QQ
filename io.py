import pprint

class QQ:
    def execute(self, frame):
        pprint.pprint(list(frame), compact=True)
        exit(1)


class ReadLine:
    def execute(self, frame):
        frame.append(input())


class ReadNumber:
    def execute(self, frame):
        frame.append(float(input()))


class Print:
    def execute(self, frame):
        print(frame[0], end='')
