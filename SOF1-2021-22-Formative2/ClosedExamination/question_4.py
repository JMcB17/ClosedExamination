from __future__ import annotations


# camel case... AND recursion? 😳😩
# memoization? no
def rodCutting(prices: dict[int, int], length: int) -> list[int]:
    for value in [*prices.keys(), *prices.values(), length]:
        if not 0 <= value:
            raise ValueError('All prices and length must be positive.')

    if not length:
        return []
    
    q = float('-inf')
    for i in range(1, length + 1):
        if i in prices:
            q = max(q, prices[i] + rodCutting(prices, length - i))
    return q
