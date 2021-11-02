import random


def scramble(word: str) -> str:
    # Paddington 2 (2017)
    padding = 2

    start = word[:padding]
    end = word[-padding:]
    middle = word[padding:-padding]

    middle_shuffle = list(middle)
    random.shuffle(middle_shuffle)

    word_scrambled = ''.join([start, *middle_shuffle, end])
    return word_scrambled


if __name__ == '__main__':
    print(scramble('hearing'))
    print(scramble('hearing'))
