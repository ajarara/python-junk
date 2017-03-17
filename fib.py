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





