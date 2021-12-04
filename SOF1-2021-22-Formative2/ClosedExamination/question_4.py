from __future__ import annotations


# camel case... AND recursion? 😳😩
# memoization? no
def rodCutting(prices: dict[int, int], length: int) -> list[int]:
    for value in [*prices.keys(), *prices.values(), length]:
        if not 0 <= value:
            raise ValueError('All prices and length must be positive.')

    # base case
    if not length:
        return []
    
    cuts = []
    for i in range(1, length + 1):
        if i in prices:
            alt_cuts = [i] + rodCutting(prices, length - i)
            # what
            if sum([prices[size] for size in alt_cuts]) > sum([prices[size] for size in cuts]):
                cuts = alt_cuts

    return cuts
