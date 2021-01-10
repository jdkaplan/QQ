from command import LOOP_TERMINATE, FUNC_TERMINATE

class While:
    def execute(self, env):
        cond = env.qframe.popleft()
        body = env.qframe.popleft()
        while cond.value == True:
            resp = body.execute(env)
            if resp == LOOP_TERMINATE:
                return None
            elif resp == FUNC_TERMINATE:
                return FUNC_TERMINATE
            cond = env.qframe.popleft()
