class Command:
    def __eq__(self, other):
        return type(self) == type(other)

    def copy(self):
        return self

    def __repr__(self):
        return f"Command(name={repr(type(self).__name__)})"


NO_TERMINATE=None
FUNC_TERMINATE=0
LOOP_TERMINATE=1
