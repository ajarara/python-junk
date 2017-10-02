

def alternator():
    state = 0
    while True:
        if state == 1:
            yield state
            state = state - 1
        elif state == 0:
            yield state
            state = state + 1


class Foo():

    def __init__(self, x):
        self.x = x
        self.state = alternator()

    def __hash__(self):
        return next(self.state)

    def __eq__(self, other):
        return isinstance(other, Foo) and self.x == other.x
