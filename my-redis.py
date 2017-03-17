import redis


# redis connection
def red_wrap(conn=[]):
    if not conn:
        conn[0] = redis.StrictRedis(host='localhost', port=6379, db=0)

    return conn[0]


def red_binary():
    conn = red_wrap()
    val = u'bar'
    print("encoding of {} is {}".format(repr(val), type(val)))
    key = 'whatever'
    print("setting {} to {} in conn".format(repr(key), repr(val)))
    conn.set(key, val)
    newval = conn.get(key)
    print("encoding of {} is {}".format(repr(newval), type(newval)))

