from __future__ import annotations
from pathlib import Path
# support unions!
from typing import Union, Optional


def str_find_all(text: str, sub: str) -> list[int]:
    len_sub = len(sub)
    location = 0
    hits = []
    while True:
        index = text.find(sub, location)
        if index == -1:
            return hits
        else:
            location = index + len_sub
            hits.append(index)


# fuck
def getWordsIndices(filename: Union[str, Path]) -> Optional[dict[str, list[int, int]]]:
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        # why not specified in assignment pdf only in tests?
        return

    text_no_case = text.casefold()
    words_list = text_no_case.split()
    words_set = set(words_list)

    indices = {word: str_find_all(text_no_case, word) for word in words_set}
    return indices
