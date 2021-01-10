import command

class While(command.Command):
    def execute(self, env):
        cond = env.qframe.popleft()
        body = env.qframe.popleft()
        while cond.value == True:
            resp = body.execute(env)
            if resp == command.LOOP_TERMINATE:
                return None
            elif resp == command.FUNC_TERMINATE:
                return command.FUNC_TERMINATE
            cond = env.qframe.popleft()
