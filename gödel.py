from math import sqrt

# First we need a list of primes. This is a naive algo, but I'm not
# really interested in efficiency beyond the first 256 primes as we
# all know english best-lish

# using a global cache so that we can generate by length and by maximum
# yes, this is ugly. yes, this probably belongs in a redis store
# unfortunately I don't have enough caffeine to care about ugly.
_cache=[2,3]

def gen_primes(n):
    ''' generate the first n primes. return them. '''
    if len(_cache) > n:
        return _cache[n - 1:].copy() # so we don't deal with any shenanigans.

    while len(_cache) < n:
        _cache.append(_next_prime(_cache))

    return _cache[:n].copy()


def gen_primes_until(maximum):
    while _cache[-1] < maximum:
        _cache.append(_next_prime(_cache))
    return _cache.copy()
        

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
    

# now that we can generate a list of primes, we have our bijection: the gödel numbering!
def gödelize(string):
    pr = gen_primes(len(string))
    seq = [pr[index] ** ord(string[index]) for index in range(len(string))]
    result = 1
    for num in seq:
        result = result * num
    return result


# this wouldn't be a bijection if we couldn't formulate the inverse!
def rev_gödelize(number):
    ''' infinite loop '''
    assert number > 0 and (number) == int
    
    # cowboy coding best coding
    exp = []
    i = 0
    
    while number != 1:  # every integer has a prime factorization
        # avoiding an index error:
        if i > (len(_cache) -1):
            pass
        while number % prime[i] == 0
            
        
        

def bump_cache():
    _cache.append(_next_prime(_cache))
        
    
