from __future__ import annotations
from typing import Optional

BINARY = '01'

class Encoding:
    def __init__(self, tree_list: list[Optional[str]]):
        self._encoding = tree_list.copy()

        self.decodeText = self.decode_text

    def decode_text(self, coded: str) -> str:
        if any(c not in BINARY for c in coded):
            raise ValueError('The string coded must contain only 1s and 0s.')

        decoded_list = []

        index = 0
        for c in coded:
            node = self._encoding[index]
            if node:
                decoded_list.append(node)
                index = 0

            pass

        decoded = ''.join(decoded_list)
        return decoded
