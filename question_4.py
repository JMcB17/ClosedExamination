import random


def scramble(word: str) -> str:
    """Shuffle the inner characters of a string.
    
    Takes a string parameter named word, 
    and returns a string where the first two letters and the last two letters 
    are the same as word, and the middle letters of the returned string
    are the remaining letters from word in a random order. A word of
    length smaller or equal to five letters is not changed by the function.
    """
    word_len_min = 5
    # Paddington 2 (2017)
    padding = 2

    if len(word) <= word_len_min:
        return word

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
