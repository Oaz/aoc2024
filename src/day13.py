import re
from typing import List, Tuple


class ClawMachine:

  @staticmethod
  def parse_line(text: str, shift: int = 0) -> Tuple[int, int]:
    result = re.search(r'X.(-?\d+), Y.(-?\d+)', text)
    return int(result.group(1)) + shift, int(result.group(2)) + shift

  def __init__(self, input_text: str, correction=0):
    lines = input_text.strip().splitlines()
    self.delta_x_on_a, self.delta_y_on_a = self.parse_line(lines[0])
    self.delta_x_on_b, self.delta_y_on_b = self.parse_line(lines[1])
    self.x_prize, self.y_prize = self.parse_line(lines[2], correction)
    self.numerator_a = self.x_prize * self.delta_y_on_b - self.y_prize * self.delta_x_on_b
    self.denominator_a = self.delta_x_on_a * self.delta_y_on_b - self.delta_y_on_a * self.delta_x_on_b
    self.numerator_b = self.x_prize * self.delta_y_on_a - self.y_prize * self.delta_x_on_a
    self.denominator_b = self.delta_x_on_b * self.delta_y_on_a - self.delta_y_on_b * self.delta_x_on_a

  @property
  def has_solution(self) -> bool:
    return self.numerator_a % self.denominator_a == 0 and self.numerator_b % self.denominator_b == 0

  @property
  def tokens_to_win(self):
    return 3 * (self.numerator_a // self.denominator_a) + (self.numerator_b // self.denominator_b)


class Arcade(List[ClawMachine]):
  def __init__(self, input_text: str, with_correction=False):
    correction = 10000000000000 if with_correction else 0
    machines = [ClawMachine(block, correction) for block in input_text.split('\n\n') if block.strip()]
    super().__init__(machines)

  @property
  def tokens_to_win_all(self) -> int:
    return sum(machine.tokens_to_win for machine in self if machine.has_solution)
