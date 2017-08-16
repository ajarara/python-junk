from threading import Lock


class ConcurrentMap():

    def __init__(self, key_value_pairs=None, lock_rate=8):
        self._d = {}
        self._locks = {}
        self._lock_count = 0
        self._lock_rate = lock_rate
        self._curr_lock = None
        # initialize the array
        if key_value_pairs:
            for key, value in key_value_pairs:
                self[key] = value

    def __getitem__(self, key, lock=True):
        # it's reasonable to have the option to bypass the Lock
        if lock:
            self._locks[key].acquire()
            out = self._d[key]
            self._locks[key].release()
            return out
        return self._d[key]

    def __setitem__(self, key, value):
        if self._lock_count & self._lock_rate == 0:
            # time for a new lock
            self._curr_lock = Lock()
            self._lock_count += 1
            self._locks[key] = self._curr_lock
            self._curr_lock.acquire()
            self._d[key] = value
            self._curr_lock.release()
        else:
            self._locks[key].acquire()
            self._d[key] = value
            self._locks[key].release()
