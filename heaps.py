import math


def xor_swap(arr, idx1, idx2):
    "Why not?"
    assert idx1 != idx2
    arr[idx1] = arr[idx1] ^ arr[idx2]
    arr[idx2] = arr[idx1] ^ arr[idx2]
    arr[idx1] = arr[idx1] ^ arr[idx2]


class Heap(object):
    """
    This is our inspiration: https://www.youtube.com/watch?v=WCm3TqScBM8
    We're using the implicit representation. An explicit
    representation would be using something like an object that stored
    references to the head and end of the list.. but that is a little
    awkward even though the abstraction isn't broken. The implicit
    representation (using an array) is quick to implement and also
    illustrative in general.

    For now this is a max heap... and it only works on integers.
    The only reason it does is because of xor_swap (which can be
    modified to work on bytes underlying the object).
    """
    def __init__(self, iterable=None):
        self.heap = []
        if iterable:
            for element in iterable:
                self.insert(element)

    def __repr__(self, opt=False):
        return repr(self.heap)

    def _get_parent_idx(self, idx):
        # the root has no parent. makes insertion easier to implement.
        if idx != 0:
            return math.floor((idx - 1)/2)

    def _get_left_child_idx(self, idx):
        left = 2 * idx + 1
        if left < len(self.heap):
            return left

    def _get_right_child_idx(self, idx):
        right = 2 * idx + 2
        if right < len(self.heap):
            return right

    # BROKEN. Sleeping on it.
    def _sift_target(self, idx):
        """
        Given an index, decides if the element at that index should
        swap with a child.  If the index has no child (or the children
        don't compare) returns None. Otherwise returns the idx to swap.
        """
        # this code is a little terse so it warrants explanation I
        # think.  if a node does not have a left child, it cannot have
        # a right child.  (this also means there is no sift_target and
        # we return None without any branching.) Further, we delay
        # getting the right child as late as possible
        left_idx = self._get_left_child_idx(idx)
        if left_idx is not None:
            parent = self.heap[idx]
            left = self.heap[left_idx]
            if left > parent:
                right_idx = self._get_right_child_idx(idx)
                if right_idx is not None and self.heap[right_idx] > left:
                    return right_idx
                else:
                    return left_idx

    def get_max(self):
        # should I raise an error if getmax is called on an empty heap?
        # probably. is IndexError the right error to send?
        # or should I mask it with something else?
        try:
            return self.heap[0]
        except IndexError:
            raise IndexError("get_max called on an empty heap")

    def insert(self, element):
        self.heap.append(element)
        if len(self.heap) > 1:
            curr_idx = len(self.heap) - 1
            parent_idx = self._get_parent_idx(curr_idx)
            while parent_idx is not None and self.heap[parent_idx] < element:
                xor_swap(self.heap, parent_idx, curr_idx)
                curr_idx = parent_idx
                parent_idx = self._get_parent_idx(curr_idx)

    def pop_max(self):
        if not self.heap:
            raise IndexError("pop_max called on an empty heap")
        elif len(self.heap) == 1:
            return self.heap.pop()
        else:
            xor_swap(self.heap, 0, len(self.heap) - 1)
            out = self.heap.pop()
            # and now we sift down
            curr_idx = 0
            swap_idx = self._sift_target(curr_idx)
            while swap_idx is not None:
                xor_swap(self.heap, swap_idx, curr_idx)
                curr_idx = swap_idx
                swap_idx = self._sift_target(curr_idx)
            return out
