from typing import List


class Report:
  def __init__(self, input: str | List[int]):
    self.levels = [int(n) for n in input.split()] if isinstance(input, str) else input

  @property
  def is_safe(self) -> bool:
    delta_adjacent_levels = [b - a for a, b in zip(self.levels, self.levels[1:])]
    all_differences_in_adjacent_levels_are_acceptable = all(1 <= abs(d) <= 3 for d in delta_adjacent_levels)
    all_increasing = all(n >= 0 for n in delta_adjacent_levels)
    all_decreasing = all(n <= 0 for n in delta_adjacent_levels)
    return (all_increasing or all_decreasing) and all_differences_in_adjacent_levels_are_acceptable

  @property
  def is_dampener_safe(self) -> bool:
    return self.is_safe or any(self.remove_level(i).is_safe for i in range(len(self.levels)))

  def remove_level(self, i: int):
    return Report(self.levels[:i] + self.levels[i + 1:])


class ReportList(List[Report]):
  def __init__(self, input: str | List[Report]):
    super().__init__([Report(row) for row in input.strip().splitlines()] if isinstance(input, str) else input)

  @property
  def count_safe(self) -> int:
    return sum(1 for report in self if report.is_safe)

  @property
  def count_dampener_safe(self) -> int:
    return sum(1 for report in self if report.is_dampener_safe)
