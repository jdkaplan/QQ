from environment import Env

# TODO we may want to combine these operator/operations things in a different way

class FnCall:
    # TODO
    def execute(self, env):
        fname = env.qframe.pop()
        subqframe = env.qframe.pop()
        body = env.fnqueue[fname]

        body.execute(Env(qframe=subqframe, rqueue=None, fnqueue=env.fnqueue))

        env.qframe.push(subqframe)

class FnDef:
    # TODO
    def execute(self, env):
        fname = env.qframe.pop()
        f_body = env.qframe.pop()

        env.fnqueue[fname] = f_body
