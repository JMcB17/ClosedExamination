def sum_integers(start: int, end: int) -> int:
    """Sum integers between start and end inclusive.
    
    Returns -1 if one of the following is true:
        end < start
        start < 0
        end < 0
    """
    if any([end < start, start < 0, end < 0]):
        return -1

    return sum(range(start, end+1))
