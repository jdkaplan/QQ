import sys

from environment import Env
import parser

def repl():
    env = Env
    while (inp := input("> ")) != "QUIT!": # or whatever
        inst = parser.parse(inp)       # TODO
        inst.execute(env)

def evaluate_file(fname):
    with open(fname) as f:
        env = Env()
        inst_q = parser.parse(f.read()) # TODO
        inst_q.execute(env) # assuming this will be a Queue for now

if __name__ == '__main__':
    if len(sys.argv) > 1:
        evaluate_file(sys.argv[1])
    else:
        repl()
