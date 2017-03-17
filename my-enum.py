from random import shuffle


# ctci
# assumptions: len(strs) differ by exactly one, short_s is the shorter.
# we're only looking for one disparity here.
def oneChange(short_s, long_s):

    assert len(long_s) - len(short_s) == 1

    # handle the degenerate case
    if (short_s == ""):         # no need to check if len(long_s) is 1
        return True

    long_e = enumerate(long_s)
    disparity = False

    for char in short_s:
        if not(next(long_e)[1] == char):
            if disparity:
                # we've already encountered a disparity, so now there are two.
                return False
            else:
                # we've encountered the only disparity,
                disparity = True
                next(long_e)
    return disparity


def genRand(n):
    return shuffle(range(n))


def findNum(i, n):
    pass
