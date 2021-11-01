from typing import Optional


def create_triangle(n: int) -> Optional[str]:
    """Return a string representing a triangle n levels high when printed."""
    fill = 'x'
    negative = '-'

    if n < 0:
        return

    format_specifier = f'{{:{negative}<{n}}}'
    lines = [format_specifier.format(fill*i) for i in range(1, n+1)]
    # leading newline
    lines.append('')
    return '\n'.join(lines)


if __name__ == '__main__':
    print(create_triangle(3))
