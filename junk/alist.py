from collections import deque


class assoc_node():
    ''' singleton key value mapping. represent string'''
    def __init__(self, key=None, value=None, str_sep=""):
        if not key and value:
            raise(LookupError("Assoc value: {} with no key.".format(value)))
        self.key = key
        self.value = value
        self.str_sep = str_sep

    def __str__(self):
        return self.str_sep.join([str(self.key),
                                  str(self.value)])



# make sure to keep in mind what order deques do. appendleft makes it
# read left to right.
def compress_str(strn):
    ''' return a deque using our compr algo '''
    deq = deque()
    for char in strn:
        if not deq or deq[-0].key != char:
            deq.appendleft(assoc_node(char, 1))
        else:
            deq[-0].value += 1
    return deq


def str_rep(deq):
    builder = []
    while deq:
        builder.append(str(deq.pop()))
    return "".join(builder)
