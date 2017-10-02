
class Node(object):
    def __init__(self, val, link):
        self.val = val
        assert isinstance(link, Node) or link is None
        self.link = link

    def __repr__(self):
        if self.link is None:
            return "({})".format(self.val)
        return "({} . {})".format(self.val, repr(self.link))


def weak_n_decomps(num, n, _max=None):
    if _max is None:
        _max = num
    if n == 0:
        return [Node(num, None)]
    else:
        out = []
        for i in reversed(
                range(min(_max, num))):
            for subr in weak_n_decomps(num - i, n - 1):
                out.append(Node(i, subr))
        return out

