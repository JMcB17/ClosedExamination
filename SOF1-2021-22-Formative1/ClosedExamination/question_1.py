from typing import Optional


def create_triangle(n: int) -> Optional[str]:
    """Create triangle of text with height and width n.
    
    When given an integer n, returns a string representing a triangle n levels high 
    when printed. To draw the triangle use the - and x characters.
    If n = 0, the function returns an empty string, if n is not positive it returns None.
    """
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
