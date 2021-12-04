from __future__ import annotations


# camel case... AND recursion? 😳😩
# memoization? no
def rodCutting(prices: dict[int, int], length: int) -> list[int]:
    if not length:
        return 0
    
    q = float('-inf')
    for i in range(1, length + 1):
        q = max(q, prices[i] + rodCutting(prices, length - i))
    return q
