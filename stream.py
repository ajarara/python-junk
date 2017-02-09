from collections import deque
from random import randrange

some = deque()


class why:
    '''
    Return a random character every iteration. If entropy is none, set
    it to 25. Entropy says how many different letters besides "a" to
    emit. 0 will just get you a constant stream of "a"s, 25 will get
    you all other letters.

    '''
    def __init__(self, entropy=None):
        if not entropy:
            entropy = 25
        if not (0 <= entropy <= 25):
            raise ValueError("Homie that's not how this works. See docstring.")
        self.entropy = entropy

    def __iter__(self):
        self.first = ord('a')
        self.count = 0
        return self

    def __next__(self):
        if self.entropy == 0:
            return chr(self.first)
        else:
            return chr(self.first + randrange(self.entropy))
