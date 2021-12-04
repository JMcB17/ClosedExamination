from __future__ import annotations
from pathlib import Path
# support unions!
from typing import Union

def str_find_all(text: str, sub: str) -> list[int]:
    location = 0
    hits = []
    while True:
        index = text.find(sub, start=location)
        if index == -1:
            return hits
        else:
            location = index
            hits.append(index)

# fuck
def getWordsIndices(filename: Union[str, Path]) -> dict[str, list[int, int]]:
    with open(filename, encoding='utf-8') as file:
        text = file.read()

    text_no_case = text.casefold()
    words_list = text_no_case.split()
    words_set = set(words_list)

    indices = {word: str_find_all(text_no_case, word) for word in words_set}
    return indices
