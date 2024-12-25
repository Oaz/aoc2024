from itertools import product
from typing import List


def parse(input_lines) -> List[int]:
  return list({
    i: j
    for j, line in reversed(list(enumerate(input_lines)))
    for i, char in enumerate(line)
    if char == '.'
  }.values())


class LocksAndKeys:
  def __init__(self, input_text: str):
    groups = input_text.strip().split('\n\n')
    self.locks = [parse(group[6:].strip().splitlines()) for group in groups if group[0] == '#']
    self.keys = [parse(reversed(group[:-6].strip().splitlines())) for group in groups if group[-1] == '#']

  @property
  def uniques_fit_without_overlapping(self):
    return sum(
      1
      for lock, key in product(self.locks, self.keys)
      if all([lock_height + key_height < 6 for lock_height, key_height in zip(lock, key)])
    )
