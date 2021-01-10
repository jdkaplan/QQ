from environment import Env

# TODO we may want to combine these operator/operations things in a different way

class FnCall:
    def execute(self, env):
        fname = env.qframe.popleft()
        subqframe = env.qframe.popleft()
        body = env.fnqueue[fname]

        body.execute(Env(qframe=subqframe, rqueue=None, fnqueue=env.fnqueue))

        env.qframe.push(subqframe)

class FnDef:
    def execute(self, env):
        fname = env.qframe.popleft()
        f_body = env.qframe.popleft()

        env.fnqueue[fname] = f_body
