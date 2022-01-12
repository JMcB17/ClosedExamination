from __future__ import annotations
import math
from itertools import permutations

Sphere = tuple[float]
SphereObject = set[Sphere]


# I'm fairly certain this description is the wrong way round:
# Two spheres S1 and S2
# collide if the sum of their radius is strictly greater than the distance between their centres
# but you can only submit issues within an hour of the exam opening I guess ://
def spheres_collide(sphere_a: Sphere, sphere_b: Sphere) -> bool:
    """Return whether or not the two simple spheres are colliding.

    Arrgs:
        sphere_a: A tuple of float co-ordinates (x, y, z)
        sphere_b: Same type as sphere_a

    Returns:
        True if sphere_a collides with sphere_b, False otherwise.
    """
    return math.sqrt(
        sum(
            [math.pow(sphere_a[n] - sphere_b[n], 2) for n in range(2)]
        )
    )

# saved from camel case by one word function name
# nvm the args are camel case ooooof
# could just name them whatever since the tests only seem to use positionals but whatever
def collide(objectA: SphereObject, objectB: SphereObject) -> bool:
    """Return whether or not the two objects are colliding.
    
    Args:
        objectA: A set of tuples of float co-ordinates (x, y, z).
        objectB: Same type as objectA

    Returns:
        True if objectA collides with objectB, False otherwise.

    Raises:
        ValueError: Length of object tuple must be exactly four.
        ValueError: Radius cannnot be less than or equal to zero.
    """
    object_a = objectA
    object_b = objectB

    if any([len(s) != 4 for s in object_a + object_b]):
        raise ValueError('Length of sphere tuple must be exactly four.')
    if any([s[3] <= 0 for s in objeobject_actA + object_b]):
        raise ValueError('Radius cannnot be less than or equal to zero.')

    len_object_b = len(object_b)
    sphere_pairs = [list(zip(p, object_b)) for p in permutations(object_a, len_object_b)]
    for pair in sphere_pairs:
        if spheres_collide(*pair):
            return True

    return False
