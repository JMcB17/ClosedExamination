# just use matplotlib loll
from __future__ import annotations


# just showing off
class MarkRange():
    def __init__(self, min: int, bin_size: int):
        self.min = min
        self.max = min + bin_size

    def __str__(self):
        return f'{self.min}-{self.max}'

    def __contains__(self, item):
        return self.min <= item <= self.max

    def count(self, marks_dwindling: list[int]) -> int:
        """MUTATES"""
        count = 0
        # reverse iteration for in-place list editing
        for i in range(len(marks_dwindling) - 1, -1, -1):
            if marks_dwindling[i] in self:
                count += 1
                marks_dwindling.pop(i)

        return count


class MarkDistribution:
    def __init__(self, mark_max: int = 100, mark_min: int = 0):
        if not mark_min < mark_max:
            raise ValueError(
                'Maximum value for a mark is less or equal to the minimum value for a mark.'
            )

        self._min = mark_min
        self._max = mark_max
        self._marks: list[int] = []

    # mad with power
    def __len__(self):
        return self._max - self._min

    # sorry
    def addAll(self, student_marks: list[int]):
        for mark in student_marks:
            if not self._min <= mark <= self._max:
                raise ValueError(
                    'Mark is outside the range of allowed marks '
                    f'({self._min} to {self._max} inclusive).'
                )
            else:
                self._marks.append(mark)

    # sorry
    def getDistribution(self, bins: int) -> list[tuple[str, int]]:
        if len(self) % bins != 0:
            raise ValueError('List of marks must be divisible by number of bins.')

        bin_size = len(self) // bins
        marks_dwindling = self._marks.copy()
        distribution = []

        # WHY?? why bin sizes not equal for last one??
        for i in range(0, len(self), bin_size):
            if i == len(self) - bin_size:
                mark_range = MarkRange(i, bin_size)
            else:
                mark_range = MarkRange(i, bin_size-1)
            distribution.append(
                (str(mark_range), mark_range.count(marks_dwindling))
            )

        return distribution
