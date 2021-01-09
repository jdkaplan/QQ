class Number:
    def __init__(self, flt):
        self.val = flt

    def execute(self, qframe):
        qframe.push(self)
