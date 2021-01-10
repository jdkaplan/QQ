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


class RIfBreak(command.Command):
    def execute(self, env):
        if env.rqueue is None:
            raise exceptions.QQError("Register queue is not allocated")

        cond = bool(env.rqueue.pop().value)
        if cond:
            return command.LOOP_TERMINATE
