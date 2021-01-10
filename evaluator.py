import sys

from environment import Env
import command
import exceptions
import parser

def repl():
    env = Env()
    while (inp := input("> ")) != "QUIT!": # or whatever
        inst = parser.parse(inp)       # TODO
        inst.execute(env)

def evaluate_file(fname):
    with open(fname) as f:
        env = Env()
        inst_q = parser.parse(f.read()) # TODO
        term = inst_q.execute(env) # assuming this will be a Queue for now

        # break on the top level will cause execution to stop, but should really be an error.  ret
        # can be used to return early.
        if term == command.LOOP_TERMINATE:
            raise exceptions.QQError("Can't break out of the main program body.")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        evaluate_file(sys.argv[1])
    else:
        repl()
