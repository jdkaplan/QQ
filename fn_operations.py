import command
import exceptions
from environment import Env


# TODO we may want to combine these operator/operations things in a different way

class FnCall(command.Command):
    def execute(self, env):
        fname = env.qframe.popleft()
        subqframe = env.qframe.popleft()
        body = env.fnqueue[fname].copy()

        term = body.execute(Env(qframe=subqframe.statements, rqueue=None, fnqueue=env.fnqueue))

        if term == command.LOOP_TERMINATE:
            raise exceptions.QQError("Can't break from a function")

        env.qframe.append(subqframe)


class FnDef(command.Command):
    def execute(self, env):
        fname = env.qframe.popleft()
        f_body = env.qframe.popleft()

        env.fnqueue[fname] = f_body


class Ret(command.Command):
    def execute(self, env):
        return command.FUNC_TERMINATE
