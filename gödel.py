
# First we need a list of primes. This is a naive algo, but I'm not
# really interested in efficiency beyond the first 256 primes as we
# all know english best-lish

def gen_primes(n, cache=[2,3]):
    ''' Return a sequence of the first n primes. Utilizes a cache. If
    I cared enough, I'd use redis, but I don't have enough caffeine to
    care enough. '''
    if len(cache) > n:
        return cache[n - 1:].copy() # so we don't deal with any shenanigans.

    while len(cache) < n:
        cache.append(_next_prime(cache))

    return cache[:n].copy()


def _next_prime(prlst):
    ''' given a list of primes, return the next one. '''
    # make sure maximum prime is last one.
    assert sorted(prlst) == prlst

    # make sure first two elements are 2, 3.
    assert prlst[:2] == [2, 3]

    # start from end, increment by 2
    start = prlst[-1] + 2
    while True:
        for pr in prlst:
            if start % pr == 0:  # if a prime divides our candidate
                start += 2  # find a new candidate!
                break  # break out of the for, no need to continue
            if pr ** 2 > start:  # we found a prime!
                return start
    
