

class BSTNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, newval):
        if newval < self.val:
            if self.left:
                self.left.insert(newval)
            else:
                self.left = BSTNode(newval)
        else:
            if self.right:
                self.right.insert(newval)
            else:
                self.right = BSTNode(newval)

    def __iter__(self):
        if self.left:
            for element in self.left:
                yield element
        yield self.val
        if self.right:
            for element in self.right:
                yield element

    def __repr__(self):
        return "BSTNode({}, {}, {})".format(
            '{...}' if self.left else None,
            self.val,
            '{...}' if self.right else None)
