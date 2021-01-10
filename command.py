class Command:
    def __eq__(self, other):
        return type(self) == type(other)
