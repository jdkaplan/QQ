class Command:
    def __eq__(self, other):
        return type(self) == type(other)

    def copy(self):
        return self

NO_TERMINATE=None
FUNC_TERMINATE=0
LOOP_TERMINATE=1
