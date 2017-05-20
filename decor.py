# decors are nothing special.

# but one interesting thing I'd like to explore here is the ability to
# conveniently share a global cache.
# I'd also like to find out how the above behaves with lambdas. It seems silly to name the returned functions and immediately override their names.

def cached(fun, _cache={}):
    def same(x):
        if x in _cache:
            print("from cache!")
            return _cache[x]
        _cache[x] = fun(x)
        return _cache[x]
    return same

@cached
def hash_me(x):
    return hash(x)

@cached
def ob1_hash_me(x):
    return hash(x) + 1


# we could verify this programmatically without having to check stdout.
# 100 maps to itself.
assert hash_me(100) == 100

# but now this should fail
assert ob1_hash_me(100) == 101

# all decorators are are proof that funcs are first class, and that
# this is literally equivalent to typing:
# cached(hash_me(x))
