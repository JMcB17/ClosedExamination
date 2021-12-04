# camelcase ew ew ewwww ewwwwwww
def hammingDistance(word1: str, word2: str) -> int:
    if len(word1) != len(word2):
        raise ValueError('word1 and word2 must be the same length.')

    distance = 0
    for char1, char2 in zip(word1, word2):
        if char1 != char2:
            distance += 1

    return distance
