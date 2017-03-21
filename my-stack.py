class Stack:
    ''' An implementation of the stack abstract data type '''
    def __init__(self, values=None):
        self._len = 0
        for thing in values:
            self.push(thing)
        

    def __len__():
        ''' Length of the stack '''
        return self._len

    def push(value):
        ''' Push value on top of the stack, increment stack pointer, return None '''
        val = StackNode(value)
        val.prev = self.peek()  # should I use the objects own interface?
                                # I could just look at self._top instead.
        self._len += 1
        self._top = val
        return None

    def peek():
        return self._top
        

    def pop():
        val = self.peek()
        self.top = val.prev
        return val

class StackNode:
    def __init__(self, value):
        self.value = value

        # is it important to declare 
        self.prev = None
