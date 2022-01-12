from __future__ import annotations

import csv
from pathlib import Path
from typing import Union

############# DO NOT DELETE THIS LINE OF CODE ######################
from invalidfileformatexception import InvalidFileFormatException

##################  WRITE YOUR CODE HERE ###########################
VALID_ITEMS = (0 ,1)


def read_adjacency(filename: Union[str, Path]) -> list[list[int]]:
    adjacency_matrix = []

    filename = Path(filename)
    with open(filename) as file:
        reader = csv.reader(file)
        for row in reader:
            adjacency_matrix.append(row)

    len_matrix = len(adjacency_matrix)
    for line in adjacency_matrix:
        if len(line) != len_matrix:
            raise InvalidFileFormatException('Matrix is not square.')
        if any([i not in VALID_ITEMS for i in line]):
            raise InvalidFileFormatException('File contains values other than 0s and 1s.')

    return adjacency_matrix


readAdjacency = read_adjacency
