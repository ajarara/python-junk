import operator


class AVLNode():
    def __init__(self, val, key=operator.lt, left=None, right=None):
        self.val = val
        self.key = key
        # enforce that the key is an invariant of the tree
        for subroot in [x for x in (left, right) if x]:
            assert subroot.key == key

        # now assert the key behaves as expected
        if left:
            assert not key(left.val, val)
        if right:
            assert key(right.val, val)

        self.left, self.right = left, right

        self.left = left
        self.right = right

        # this is bothersome. is there a better way of doing this?
        if left:
            if right:
                self.height = 1 + max(left.height, right.height)
            else:
                self.height = 1 + left.height
        elif right:
            self.height = 1 + right.height
        else:
            self.height = 0

        # an assumption I'm making here is that we don't need to rebalance
        # our left and right subtrees
        # but in case that assumption is scary:
        # self.maybe_rebalance()

    def insert(self, newval):
        if self.key(newval, self.val):
            if self.right:
                self.right.insert(newval)
                self.height = max(
                    self.height,
                    self.right.height + 1)
            else:
                # propagate the key
                self.right = AVLNode(newval, key=self.key)
                # this preserves the height unless self was previously a leaf
                self.height = max(self.height, 1)
        else:
            # this can be bumped up above
            # while preserving correctness.
            # I'm going to leave it as is.
            if self.left:
                self.left.insert(newval)
                self.height = max(
                    self.height,
                    self.left.height + 1)
            else:
                self.left = AVLNode(newval, key=self.key)
                self.height = max(self.height, 1)
        self.maybe_rebalance()

    def get_balance(self):
        # if a subtree is none we don't attempt
        # to get the height, which avoids attr error
        # this is... incorrect.
        # if self.left is None the left subtree has a height
        # of -1
        if self.left:
            cands.append(self.left.height)
        return (self.left and self.left.height or 0 -
                self.right and self.right.height or 0)

    def maybe_rebalance(self):
        balance = self.get_balance()
        if balance == -2:
            # the right tree is heavier
            # further we are guaranteed that there is an AVLNode
            # on the right. (so we can right balance)
            self.right_balance()
        elif balance == 2:
            self.left_balance()
        elif balance not in range(-1, 2):
            # can we fix this?
            raise ValueError("This node is broken: ", self)

    # neither of these are right
    # take a break, come back, and address the situations
    # of when and how to rotate a subtree.
    def left_balance(self):
        if self.left and self.left.get_balance() > -1:
            self.left.right_rotate()
        self.right_rotate()

    def right_balance(self):
        if self.right and self.right.get_balance() < 1:
            self.right.left_rotate()
        self.right_rotate()

    # these are correct.
    def left_rotate(self):
        self.left = AVLNode(
            self.val,
            left=self.left,
            right=self.right.left)
        self.val = self.right.val
        self.right = self.right.right

    def right_rotate(self):
        self.right = AVLNode(
            self.val,
            left=self.left.right,
            right=self.right)
        self.val = self.left.val
        self.left = self.left.left
