from typing import Dict, List

# camel case... AND recursion? 😳😩
def rodCutting(prices: Dict[int, int], length: int) -> List[int]:
    if not length:
        return 0
    
    q = float('-inf')
    for i in range(1, length + 1):
        q = max(q, prices[i] + rodCutting(prices, length - i))
    return q
