from __future__ import annotations
from typing import Optional

BINARY = '01'

class Encoding:
    """Stores a huffman tree as a list and has methods to encode and decode text with it."""

    def __init__(self, tree_list: list[Optional[str]]):
        self._encoding = tree_list.copy()
        self._decoding = self.make_decoding()

        self.decodeText = self.decode_text
        self.encodeText = self.encode_text

    def make_decoding(self) -> dict[str, str]:
        decoding = {}

        counter_max = 0
        counter = 0
        digits = 0
        spec = ''
        for index, node in enumerate(self._encoding):
            if node:
                path = spec.format(counter=counter)
                decoding[node] = path

            if counter == counter_max:
                counter_max += 1
                counter_max *= 2
                counter_max -= 1
                counter = 0
                digits += 1
                spec = f'{{counter:0>{digits}b}}'
            else:
                counter += 1

        return decoding

    def decode_text(self, coded: str) -> str:
        """Decode a binary string with the encoding tree.

        Args:
            coded: A valid string of 1s and 0s

        Returns:
            The decoded plaintext string.

        Raises:
            ValueError: The string coded must contain only 1s and 0s.        
        """
        if any(c not in BINARY for c in coded):
            raise ValueError('The string coded must contain only 1s and 0s.')

        decoded_list = []

        index = 0
        for c in coded:
            if c == '0':
                index = 2 * index + 1
            else:
                index = 2 * index + 2

            node = self._encoding[index]
            if node:
                decoded_list.append(node)
                index = 0
        if not node:
            raise ValueError('Coded string did not end on a leaf, must be corrupt.')

        decoded = ''.join(decoded_list)
        return decoded

    def encode_text(self, text: str) -> str:
        """Encode plaintext into binary string.

        Args:
            text: Plaintext string

        Returns:
            Encoded string of 1s and 0s

        Raises:
            ValueError: Text contains symbols not present in the encoding tree.
        """
        encoded_list = []
        for c in text:
            e = self._decoding.get(c)
            if e is None:
                raise ValueError('Text contains symbols not present in the encoding tree.')
            encoded_list.append(e)

        encoded = ''.join(encoded_list)
        return encoded


if __name__ == '__main__':
    l = [
    # path
    #       0   1   00  01  10   11   000  001  010  011
    # digits
    #   0   1   1   2   2   2    2    3    3    3    3
    # counter
    #   0   0   1   0   1   2    3    0    1    2    3
    # max
    #   0   1   1   3   3   3    3    7    7    7    7
        '', '', '', '', '', 'E', 'F', 'A', 'B', 'C', 'D', None, None, None, None, 
        None, None, None, None, None, None, None, None
    ]
    e = Encoding(l)
    print(e._encoding)
    print(e._decoding)
    print(e.decode_text('1100001010'))
    print(e.encode_text('ACE'))
