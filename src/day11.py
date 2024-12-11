from typing import Dict, Tuple
import math


def number_of_digits(n: int):
  if n == 0:
    return 1
  return int(math.log10(n)) + 1


class Stones:
  def __init__(self, input_text: str):
    self.numbers = list(map(int, input_text.split()))
    self.cache: Dict[Tuple[int, int], int] = {}

  def count_stones_after_blinks(self, blinks: int) -> int:
    return sum(self.apply_blink_rules(number, blinks) for number in self.numbers)

  def blink_and_memoize(self, number: int, remaining: int) -> int:
    count: int | None = self.cache.get((number, remaining), None)
    if count is not None:
      return count
    count = self.apply_blink_rules(number, remaining)
    self.cache[(number, remaining)] = count
    return count

  def apply_blink_rules(self, number: int, remaining: int) -> int:
    if remaining == 0:
      return 1
    remaining -= 1
    if number == 0:
      return self.blink_and_memoize(1, remaining)
    n = number_of_digits(number)
    if n % 2 == 1:
      return self.blink_and_memoize(number * 2024, remaining)
    split = 10 ** (n // 2)
    return self.blink_and_memoize(number // split, remaining) + self.blink_and_memoize(number % split, remaining)
