import functools
from typing import List, Tuple


class Update(List[int]):
  def __init__(self, input_text: str, rules: List[Tuple[int, int]]):
    items = [int(x) for x in input_text.split(",")]
    super().__init__(items)
    self.is_ordered = all(pair in rules for pair in zip(items, items[1:]))
    if not self.is_ordered:
      items = sorted(items, key=functools.cmp_to_key(
        lambda a, b: 1 if (a, b) in rules else -1 if (b, a) in rules else 0
      ))
    self.middle_page_number = items[len(items) // 2]


class Printer:
  def __init__(self, input_text: str):
    lines = input_text.strip().splitlines()
    self.rules = [
      (int(a), int(b))
      for line in lines if '|' in line
      for a, b in [line.split('|')]
    ]
    self.updates = [Update(line, self.rules) for line in lines if ',' in line]

  @property
  def sum_of_middle_page_number_in_ordered_updates(self):
    return sum(update.middle_page_number for update in self.updates if update.is_ordered)

  @property
  def sum_of_middle_page_number_in_unordered_updates(self):
    return sum(update.middle_page_number for update in self.updates if not update.is_ordered)
