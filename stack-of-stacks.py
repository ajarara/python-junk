class Stack():
    ''' This is pretty! '''

    def __init__(self, values=None):
        self._len = 0
        self.top = None
        if values:
            for i in values:
                self.append(i)

    def append(self, thing):
        val = StackNode(thing)
        val.down = self.top
        self.top = val
        self._len += 1
        return None

    def pop(self):
        if not self:
            raise IndexError("pop from an empty stack")
        res = self.top
        self.top = res.down
        self._len -= 1
        return res.value

    def peek(self):
        if self.top:
            return self.top.value

    def __len__(self):
        return self._len


class StackNode():
    def __init__(self, value):
        self.down = None
        self.value = value


# 3.3 solution inc
MAXHEIGHT = 100


class StackRec():
    ''' A recursive stack pool.'''
    def __init__(self, values=None):
        # initialize the first stack
        first = Stack()

        # init the pool
        self._stack_pool = Stack()

        # stick the first one in there.
        self._stack_pool.append(first)

    def append(self, value):
        # if the stack is "full", append a new one.
        if len(self._stack_pool.peek()) >= MAXHEIGHT:
            self._stack_pool.append(Stack())
        self._stack_pool.peek().append(value)
        return None

    def pop(self):
        if not self._stack_pool.peek():
            # empty stack pool
            self._stack_pool.pop()
        return self._stack_pool.peek().pop()
        

        
        
# 3.4 solution, given the previous Stack()
