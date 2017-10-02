

class Heap(object):
    """
    This is our inspiration: https://www.youtube.com/watch?v=WCm3TqScBM8
    We're using the implicit representation. An explicit
    representation would be using something like an object that stored
    references to the head and end of the list.. but that is a little
    awkward even though the abstraction isn't broken. The implicit
    representation (using an array) is quick to implement and also
    illustrative in general.
    
    
    For now this is a max heap.
    """
    def __init__(self, iterable=None):
        if iterable:
            
