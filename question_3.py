def sum_integers(start: int, end: int) -> int:
    """Take two positive integers, start and end, and return the sum of all integers comprised between start and end inclusive."""
    if any([end < start, start < 0, end < 0]):
        return -1

    return sum(range(start, end+1))
