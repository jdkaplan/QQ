from environment import Env
from command import Command

# TODO we may want to combine these operator/operations things in a different way

class FnCall(Command):
    def execute(self, env):
        fname = env.qframe.popleft()
        subqframe = env.qframe.popleft()
        body = env.fnqueue[fname]

        body.execute(Env(qframe=subqframe, rqueue=None, fnqueue=env.fnqueue))

        env.qframe.push(subqframe)

class FnDef(Command):
    def execute(self, env):
        fname = env.qframe.popleft()
        f_body = env.qframe.popleft()

        env.fnqueue[fname] = f_body
