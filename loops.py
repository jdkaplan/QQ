import command

class Loop(command.Command):
    def execute(self, env):
        body = env.qframe.popleft()
        while True:
            resp = body.execute(env)
            if resp == command.LOOP_TERMINATE:
                return command.NO_TERMINATE
            elif resp == command.FUNC_TERMINATE:
                return command.FUNC_TERMINATE
