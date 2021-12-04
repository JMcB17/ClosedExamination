# just use matplotlib loll

# showing off
class MarkRange():
    def __init__(self, min: int, bin_size: int):
        self.min = min
        self.max = min + bin_size

    def __str__(self):
        return f'{self.min}-{self.max}'

    def __contains(self, item):
        return self.min <= item >= self.max

class MarkDistribution:
    def __init__(self, mark_min: int = 0, mark_max: int = 100):
        self._min = mark_min
        self._max = mark_max
        self._marks: list[int] = []

    # sorry
    def addAll(student_marks: list[int]):
        for mark in student_marks:
            if not self._min <= mark <= self._max:
                raise ValueError(
                    'Mark is outside the range of allowed marks '
                    f'({self._min} to {self._max} inclusive).'
                )
            else:
                self._marks.append(mark)

    def _count_in_range(marks_dwindling: list[int], mark_range: MarkRange) -> int:
        count = 0
        # reverse iteration for in-place list editing
        for i in range(len(marks_dwindling), 0, -1):
            if mark in mark_range:
                count += 1
                marks_dwindling.pop(i)

        return count

    # sorry
    def getDistribution(bins: int) -> list[tuple[str, int]]:
        len_marks = len(self._marks)
        if len_marks % bins != 0:
            raise ValueError('List of marks must be divisible by number of bins.')

        marks_dwindling = self._marks.copy()
        distribution = {}
        bin_size = len_marks // bins

        for i in range(0, len_marks, bin_size):
            mark_range = MarkRange(i, bin_size)


        return distribution
