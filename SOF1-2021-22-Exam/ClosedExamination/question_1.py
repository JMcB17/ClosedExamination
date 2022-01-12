from __future__ import annotations
import math
from fractions import Fraction


MASS_CONSTANT = Fraction(4, 3)


def total_mass(sphere: tuple[float]) -> float:
    """Calculate the mass of a sphere from its radius and unit mass.
    
    Args:
        sphere: A tuple (x, y, z, radius, unit_mass).
            x, y, and z are not used by this function and can be dummy values.
            radius and unit_mass should be floats.

    Returns:
        The mass of the sphere as a float

    Raises:
        ValueError: Radius or unit mass cannnot be less than or equal to zero.
    """
    radius = sphere[3]
    unit_mass = sphere[4]
    if radius <= 0 or unit_mass <= 0:
        raise ValueError('Radius or unit mass cannnot be less than or equal to zero.')

    return MASS_CONSTANT * unit_mass * math.pi * math.pow(radius, 3)


def centre_of_mass(spheres: set[tuple[float]]) -> tuple[float]:
    """Calculate the overall centre of mass of a set of spheres.

    Args:
        spheres: a set of tuples like (x, y, z, radius, unit_mass), where x, y, and z are coords
            and all the values in the tuple are floats.

    Returns:
        The centre of mass as a tuple like (x, y, z).

    Raises:
        ValueError: The set of spheres cannot be empty!
    """
    if not spheres:
        raise ValueError('The set of spheres cannot be empty!')

    sphere_masses = [(s, total_mass(s)) for s in spheres]

    com = []
    for n in range(3):
        com.append(
            sum([sm[0][n] * sm[1] for sm in sphere_masses]) / sum([sm[1] for sm in sphere_masses])
        )
    com = tuple(com)

    return com


# haha
centreOfMass = centre_of_mass


if __name__ == '__main__':
    print(centre_of_mass(
        {
            (-4, 1, 0, 1, 1),
            (-4, -1, 0, 1, 1),
            (1, 0, 0, 2, 1),
        }
    ))
