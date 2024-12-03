from typing import List, Tuple
import re


class Interpreter:
  def __init__(self):
    self.multiplications = []

  def proceed(self, arg):
    if arg[0] and arg[1]:
      self.multiplications.append((int(arg[0]), int(arg[1])))


class InterpreterWithDoDont(Interpreter):
  def __init__(self):
    super().__init__()
    self.mul_enabled = True

  def proceed(self, arg):
    if self.mul_enabled and arg[0] and arg[1]:
      self.multiplications.append((int(arg[0]), int(arg[1])))
    if arg[2]:
      self.mul_enabled = True
    if arg[3]:
      self.mul_enabled = False


class Computer:
  def __init__(self, input_text: str, with_do_dont: bool = False):
    self.interpreter = InterpreterWithDoDont() if with_do_dont else Interpreter()
    for match in re.findall(r'mul\((\d+),(\d+)\)|(do)\(\)|(don)\'t\(\)', input_text):
      self.interpreter.proceed(match)

  @property
  def multiplications(self) -> List[Tuple[int, int]]:
    return self.interpreter.multiplications

  @property
  def result(self) -> int:
    return sum([a * b for a, b in self.multiplications])
