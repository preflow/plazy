# -*- coding: utf-8 -*-
import base64


def b64encode(value, pretty=False):
    res = str(base64.b64encode(value.encode()).decode("utf-8"))
    if pretty:
        res = res.replace("=", "")
    return res


def b64decode(value):
    return str(base64.b64decode(value).decode("utf-8"))


def is_number(s):
    """
    Check whether string is number
    Reference: https://stackoverflow.com/q/354038/3973224
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
