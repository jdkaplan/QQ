from collections import deque

def repl():
    qframe = deque()
    while (inp := input("> ")) != "QUIT!":
        inst = parse(inp)       # TODO
        inst.execute(qframe)

def evaluate_file(fname):
    with open(fname) as f:
        qframe = deque()
        inst_q = parse(f.read()) # TODO
        inst_q.execute(qframe) # assuming this will be a Queue for now
