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

  def is_solved_using(self, *allowed_operators: Operator):
    '''
    Checks if the equation can be solved with the given operators
    :param allowed_operators: operators allowed to solve the equation
    :return: true if the equation can be solved else false

    Examples:
      >>> Equation(3267, [81, 40, 27]).is_solved_using(add, mul)
      True
      >>> Equation(7290, [6, 8, 6, 15]).is_solved_using(add, mul)
      False
      >>> Equation(7290, [6, 8, 6, 15]).is_solved_using(add, mul, concat)
      True
    '''
    if len(self.operands) == 1:
      return self.operands[0] == self.result
    last_operand = self.operands[-1]
    remaining_operands = self.operands[:-1]
    for operator in allowed_operators:
      if operator(self.result, last_operand,
                  lambda result: Equation(result, remaining_operands).is_solved_using(*allowed_operators)):
        return True
    return False

  def __repr__(self):
    return f'{self.result} {self.operands}'


class Equations(List[Equation]):

  def __init__(self, input_text: str):
    super().__init__([Equation.parse(line) for line in input_text.strip().splitlines()])

  def total_calibration_result_using(self, *allowed_operators: Operator):
    return sum(equation.result for equation in self if equation.is_solved_using(*allowed_operators))
