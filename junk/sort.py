import operator


def insertion_sort(lst):
    for idx, element in enumerate(lst):
        for comp_idx, comp_element in enumerate(reversed(lst[idx])):
            if element <= comp_element:
                pass

