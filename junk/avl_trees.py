

def max_wrapper(left, right):
    if left is None:
        if right is None:
            return -1
        return right.height
    if right is None:
        return left.height
    return max(left.height, right.height)


# we want to generate a worst case AVL tree:
class ValuelessAVLNode(object):
    def __init__(self, left=None, right=None):
        self.height = 1 + max_wrapper(left, right)
        self.left = left
        self.right = right

    def __repr__(self):
        return "{a.height} {0}\n{a.left}{0}\n{a.right}{0}".format(
            ' ' * self.height, a=self)


def memoize(fun):
    cache = {}

    def memoized(*args, **kwargs):
        hashable_params = (
            args,
            frozenset(kwargs.items()))
        if hashable_params not in cache:
            out = fun(*args, **kwargs)
            cache[hashable_params] = out
            return out
        else:
            return cache[hashable_params]
    return memoized


@memoize
def worst_case_AVL(height):
    assert height >= 0, "No way to create AVL tree of height {}".format(height)
    if height == 0:
        return ValuelessAVLNode()
    elif height == 1:
        return ValuelessAVLNode(left=worst_case_AVL(0))
    return ValuelessAVLNode(
        left=worst_case_AVL(height - 1),
        right=worst_case_AVL(height - 2))
