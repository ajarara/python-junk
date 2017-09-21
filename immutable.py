import ctypes

def change(a_num, new_num):
    ctypes.memmove(id(a_num) + 24, id(new_num) + 24, 8)

