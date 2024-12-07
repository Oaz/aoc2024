from typing import List, Callable, TypeAlias
import math

FollowUp: TypeAlias = Callable[[int], bool]
Operator: TypeAlias = Callable[[int, int, FollowUp], bool]


def add(result: int, operand: int, follow: FollowUp) -> bool:
  return follow(result - operand)


def mul(result: int, operand: int, follow: FollowUp) -> bool:
  return follow(result // operand) if result % operand == 0 else False


def concat(result: int, operand: int, follow: FollowUp) -> bool:
  power10 = 10 ** (int(math.log10(operand)) + 1)
  return follow(result // power10) if result % power10 == operand else False


class Equation:
  @staticmethod
  def parse(input_text: str):
    result, *operands = map(int, input_text.replace(':', '').split())
    return Equation(result, operands)

  def __init__(self, result: int, operands: List[int]):
    self.result, self.operands = result, operands

  def is_valid(self, *ops: Operator):
    if len(self.operands) == 1:
      return self.operands[0] == self.result
    last_operand = self.operands[-1]
    remaining_operands = self.operands[:-1]
    for op in ops:
      if op(self.result, last_operand, lambda new_result: Equation(new_result, remaining_operands).is_valid(*ops)):
        return True
    return False

  def __repr__(self):
    return f'{self.result} {self.operands}'


class Equations(List[Equation]):

  def __init__(self, input_text: str):
    super().__init__([Equation.parse(line) for line in input_text.strip().splitlines()])

  def total_calibration_result(self, *ops: Operator):
    return sum(equation.result for equation in self if equation.is_valid(*ops))
