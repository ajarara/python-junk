from collections import deque
from random import randrange

some = deque()


class randCharStream:
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


class PRNG:
    '''
    Implementation of a pseudorandom number generator. See:

    https://en.wikipedia.org/wiki/Linear_congruential_generator

    Seed must be 0 < 2^32

    Derive multipliers and increments from modulus
    '''

    def __init__(self, seed=None):
        if not seed:
            self.seed = (2 ** 32) - 1
        else:
            self.seed = seed
        self.mod = 2 ** 32
        self.mult = 86028121         # 5e6th prime
        self.incr = 2 ** 12          # number given by my sister

    def __iter__(self):
        self.last = self.seed
        return self

    def __next__(self):
        self.last = ((self.mult * self.last) + self.incr) % self.mod
        return self.last



if __name__ == "__main__":
    a = iter(randCharStream())
    for i in range(100):
        next(a)
    print("Done!")
