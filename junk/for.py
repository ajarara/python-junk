

def fibs(x):
    "gets the nth fibonacci number"
    assert(x > 0)
    if x < 3:
        return 1

    a, b = 0, 1
    for _ in range(x):
        a, b = b, a
        b += a
    return a


def fibs2(x):
    assert(x > 0)
    if x < 3:
        return 1
    
    def loop(a, b):
        return (b, b + a)

    out = (0, 1)
    for _ in range(x):
        out = loop(*out)
    return out[0]
