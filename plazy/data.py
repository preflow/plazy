# -*- coding: utf-8 -*-
import base64
from datetime import datetime


def ts2dt(ts, format="%Y/%m/%d %H:%M:%S.%f"):
    """
    Convert timestamp to datetime string.

    Plazy version: 0.1.5+

    Parameters
    ----------
    ts : float
        Timestamp
    format : str, optional
        Datetime format of the result string. Default: "%Y/%m/%d %H:%M:%S.%f"

    Keyword Arguments
    -----------------

    Returns
    -------
    out : str
        Datetime string.

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 5

        import time
        import plazy

        if __name__ == "__main__":
            res = plazy.ts2dt(time.time()) # 2021/08/28 08:48:05.451271

    See Also
    --------
    dt2ts
    """
    return datetime.fromtimestamp(float(ts)).strftime(format)


def dt2ts(dt, format="%Y/%m/%d %H:%M:%S.%f"):
    """
    Convert datetime object / datetime string to timestamp.

    Plazy version: 0.1.5+

    Parameters
    ----------
    dt : str or datetime
        Datetime to convert.
    format : str, optional
        Datetime format of "dt". Default: "%Y/%m/%d %H:%M:%S.%f"

    Keyword Arguments
    -----------------

    Returns
    -------
    out : float
        Timestamp.

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 5

        import time
        import plazy

        if __name__ == "__main__":
            res = plazy.dt2ts("2021/08/28 08:48:05.451271") # 1630140485.451271
            print(res)

    See Also
    --------
    ts2dt
    """
    if isinstance(dt, str):
        dt = datetime.strptime(dt, format)
    return dt.timestamp()


def b64encode(value, pretty=False):
    """
    Base64 encode for string.

    Plazy version: 0.1.3+

    Parameters
    ----------
    value : str
        String to encode.
    pretty : bool, optional
        Pretty string or not (remove "=" character). Default: False

    Keyword Arguments
    -----------------

    Returns
    -------
    out : str
        Encoded string.

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,5

        import plazy

        if __name__ == "__main__":
            encoded_val = plazy.b64encode('plazy') # cGxhenk=
            encoded_val = plazy.b64encode('plazy', pretty=True) # cGxhenk => Note: this string cannot be decoded!
            original_val = plazy.b64decode('cGxhenk=') # plazy

    See Also
    --------
    b64decode
    """
    res = str(base64.b64encode(value.encode()).decode("utf-8"))
    if pretty:
        res = res.replace("=", "")
    return res


def b64decode(value):
    """
    Base64 decode for string.

    Plazy version: 0.1.3+

    Parameters
    ----------
    value : str
        String to decode.

    Keyword Arguments
    -----------------

    Returns
    -------
    out : str
        Decoded string.

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 6

        import plazy

        if __name__ == "__main__":
            encoded_val = plazy.b64encode('plazy') # cGxhenk=
            encoded_val = plazy.b64encode('plazy', pretty=True) # cGxhenk => Note: this string cannot be decoded!
            original_val = plazy.b64decode('cGxhenk=') # plazy

    See Also
    --------
    b64encode
    """
    return str(base64.b64decode(value).decode("utf-8"))


def is_number(s):
    """
    Check whether string is a number.

    Plazy version: 0.1.4+

    Parameters
    ----------
    s : str
        String to check.

    Keyword Arguments
    -----------------

    Returns
    -------
    out : bool

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,5,6,7,8,9,10

        import plazy

        if __name__ == "__main__":
            is_number = plazy.is_number("1")         # True
            is_number = plazy.is_number("0.234")     # True
            is_number = plazy.is_number("-0.234")    # True
            is_number = plazy.is_number("1e3")       # True
            is_number = plazy.is_number("plazy")     # False
            is_number = plazy.is_number("1.23k9")    # False
            is_number = plazy.is_number("x.3253254") # False

    See Also
    --------
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def unique(seq, sort=False, reverse=False):
    """
    Keep unique items in list or tuple.

    Plazy version: 0.1.3+

    Parameters
    ----------
    seq : list or tuple
    sort : bool, optional
        Sorting the result. Default: False
    reverse : bool, optional
        Reverse the result. Default: False

    Keyword Arguments
    -----------------

    Returns
    -------
    out : list or tuple

    Examples
    --------

    .. code-block:: python
        :linenos:
        :emphasize-lines: 4,5,6

        import plazy

        if __name__ == "__main__":
            unique_t = plazy.unique(seq=(7, 3, 5, 3, 3, 7, 9)) # -> (7, 3, 5, 9)
            unique_l = plazy.unique(seq=[7, 3, 5, 3, 3, 7, 9]) # -> [7, 3, 5, 9]
            unique_rt = plazy.unique(seq=(7, 3, 5, 3, 3, 7, 9), sort=True, reverse=True) # -> (9, 7, 5, 3)

    See Also
    --------
    """
    is_tuple = isinstance(seq, tuple)
    new_seq = list(sorted(set(seq), key=seq.index))
    new_seq = sorted(new_seq) if sort else new_seq
    new_seq = reversed(new_seq) if reverse else new_seq

    if is_tuple:
        return tuple(new_seq)
    else:
        return list(new_seq)
