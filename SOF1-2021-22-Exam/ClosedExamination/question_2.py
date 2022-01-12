from __future__ import annotations


Sphere = tuple[float]
SphereObject = set[Sphere]


# saved from camel case by one word function name
# nvm the args are camel case ooooof
# could just name them whatever since the tests only seem to use positionals but whatever
def collide(objectA: SphereObject, objectB: SphereObject) -> bool:
    """Return whether or not the two objects are colliding.
    
    Args:
        objectA: a set of tuples of float co-ordinates (x, y, z).
        objectB: same type as objectA

    Returns:
        True if objectA collides with objectB, False otherwise.

    Raises:
        ValueError: Length of object tuple must be exactly four.
        ValueError: Radius cannnot be less than or equal to zero.
    """
    if any([len(s) != 4 for s in objectA + objectB]):
        raise ValueError('Length of sphere tuple must be exactly four.')
    if any([s[3] <= 0 for s in objectA + objectB]):
        raise ValueError('Radius cannnot be less than or equal to zero.')

    # todo: implement
    return False
