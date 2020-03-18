# -*- coding: utf-8 -*-
# https://stackoverflow.com/q/354038/3973224


def is_number(s):
    """
    Check whether string is number
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def unique(seq, sort=False, reverse=False):
    """
    Keep unique items in list or tuple
    """
    is_tuple = isinstance(seq, tuple)
    new_seq = list(sorted(set(seq), key=seq.index))
    new_seq = sorted(new_seq) if sort else new_seq
    new_seq = reversed(new_seq) if reverse else new_seq

    if is_tuple:
        return tuple(new_seq)
    else:
        return list(new_seq)
