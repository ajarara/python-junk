import redis


def fib(n):
    ''' No caching! '''
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b
    return a


def fib2(n, cache=[0, 1, 1]):
    for i in range(len(cache) - 1, n):
        val = cache[i - 1] + cache[i]
        print("value for {} is {}".format(i, val))
        cache.append(val)
    return cache[n]



def fib(n):
    ''' returns nth fib number '''
    start = [0, 1, 1]

    if n < len(start) - 1:
        # it's already been defined in start.
        return start[n]

    # initialize the main loop
    a, b = start[1], start[2]

    # we know this number is greater than 2.
    for _i in range(n - 1):
        a, b = b, a + b
    return a

def fibc(n, cache=[0, 1, 1]):
    ''' mostly worse implementation of fib2. Seriously, it offers no improvements. '''
    if n < len(cache) - 1:
        return cache[n]
    ir = range(len(cache) - 1, n)
    for i in ir:
        res = cache[i] + cache[i - 1]
        cache.append(res)
    return cache[n]

def fibr(start, stop):
    return [fibc(i) for i in range(start, stop + 1)]




