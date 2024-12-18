import re
from typing import List, Dict
from dataclasses import dataclass


@dataclass(frozen=True)
class Context:
  a: int
  b: int
  c: int
  counter: int
  output: List[int]

  @staticmethod
  def mk(ints: List[int], counter: int = 0, output: List[int] = None):
    return Context(a=ints[0], b=ints[1], c=ints[2], counter=counter, output=output if output else [])

  def update(self, **kwargs) -> 'Context':
    return Context(**{**self.__dict__, **kwargs})

  def inc_counter(self) -> 'Context':
    return self.update(counter=self.counter + 2)

  def print(self, value: int) -> 'Context':
    return self.update(output=self.output + [value])

  def combo(self, n: int) -> int:
    return n if n <= 3 else (self.a if n == 4 else (self.b if n == 5 else (self.c if n == 6 else None)))


class Computer:
  def __init__(self, input_text: str):
    ints = list(map(int, re.findall(r'-?\d+', input_text)))
    self.start = Context.mk(ints)
    self.code = ints[3:]
    instruction_map = [self.adv, self.bxl, self.bst, self.jnz, self.bxc, self.out, self.bdv, self.cdv]
    self.program = [(instruction_map[self.code[i]], self.code[i + 1]) for i in range(0, len(self.code), 2)]

  def run(self, context=None) -> List[int]:
    context = context if context else self.start
    while context.counter < len(self.code):
      instruction, operand = self.program[context.counter // 2]
      context = instruction(operand, context)
    return context.output

  @staticmethod
  def format(output: List[int]) -> str:
    return ','.join(map(str, output))

  @staticmethod
  def adv(operand: int, context: Context) -> Context:
    return context.update(a=context.a >> context.combo(operand)).inc_counter()

  @staticmethod
  def bxl(operand: int, context: Context) -> Context:
    return context.update(b=context.b ^ operand).inc_counter()

  @staticmethod
  def bst(operand: int, context: Context) -> Context:
    return context.update(b=context.combo(operand) % 8).inc_counter()

  @staticmethod
  def jnz(operand: int, context: Context) -> Context:
    return context.update(counter=operand) if context.a != 0 else context.inc_counter()

  @staticmethod
  def bxc(operand: int, context: Context) -> Context:
    return context.update(b=context.b ^ context.c).inc_counter()

  @staticmethod
  def out(operand: int, context: Context) -> Context:
    return context.print(context.combo(operand) % 8).inc_counter()

  @staticmethod
  def bdv(operand: int, context: Context) -> Context:
    return context.update(b=context.a >> context.combo(operand)).inc_counter()

  @staticmethod
  def cdv(operand: int, context: Context) -> Context:
    return context.update(c=context.a >> context.combo(operand)).inc_counter()

  def run_with_a(self, a: int) -> List[int]:
    return self.run(self.start.update(a=a))

  def find_initial_a_for_program_copy(self) -> int:
    return self.find_initial_a_for(self.code)

  def find_initial_a_for(self, output: List[int]) -> int:
    p, q = [operand for instruction, operand in self.program if instruction == self.bxl]
    table = {a: ((a & 7) ^ p ^ q ^ (a >> ((a & 7) ^ p))) & 7 for a in range(1024)}
    reverse_table = {value: sorted([key for key in table if table[key] == value]) for value in set(table.values())}
    return self._find_a(list(reversed(output)), 0, reverse_table)

  def _find_a(self, digits: List[int], a: int, r_table: Dict[int, List[int]]) -> int | None:
    if len(digits) == 0:
      return a
    min_key = (a * 8) % 1024
    max_key = min_key + 8
    for key in r_table[digits[0]]:
      if min_key <= key < max_key:
        find_a = self._find_a(digits[1:], (a * 8) | key, r_table)
        if find_a:
          return find_a
    return None
