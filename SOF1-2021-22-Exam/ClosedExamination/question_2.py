from __future__ import annotations


# saved from camel case by one word function name
# nvm the args are camel case ooooof
# could just name them whatever since the tests only seem to use positionals but whatever
def collide(objectA: tuple[float], objectB: tuple[float]) -> bool:
    """Return whether or not the two objects are colliding.
    
    Args:
        objectA: a tuple of float co-ordinates (x, y, z).
        objectB: same type as objectA

    Returns:
        True if objectA collides with objectB, False otherwise.

    Raises:
        ValueError: Length of object tuple must be exactly four.
        ValueError: Radius cannnot be less than or equal to zero.
    """
    if any([len(ob) != 4 for ob in (objectA, objectB)]):
        raise ValueError('Length of object tuple must be exactly four.')
    if any([ob[3] <= 0 for ob in (objectA, objectB)]):
        raise ValueError('Radius cannnot be less than or equal to zero.')

    # todo: implement
    return False
