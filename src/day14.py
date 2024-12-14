from typing import List, Tuple
import re
import itertools
import collections
import functools


class Robot:
  def __init__(self, size: complex, input_text: str):
    result = re.search(r'p=(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)', input_text)
    self.size = size
    self.half = complex(self.size.real // 2, self.size.imag // 2)
    self.p = complex(int(result.group(1)), int(result.group(2)))
    self.v = complex(int(result.group(3)), int(result.group(4)))

  def move(self, steps: int) -> complex:
    new_p = self.p + (self.v * steps)
    return complex(new_p.real % self.size.real, new_p.imag % self.size.imag)

  def quadrant(self, steps: int) -> Tuple[bool, bool] | None:
    position = self.move(steps)
    if position.real == self.half.real or position.imag == self.half.imag:
      return None
    return position.real < self.half.real, position.imag < self.half.imag


class Area(List[Robot]):
  def __init__(self, size: complex, input_text: str):
    robots = [Robot(size, line) for line in input_text.strip().splitlines()]
    super().__init__(robots)
    self.size = size

  def quadrants_counts(self, steps: int) -> List[int]:
    quadrants = [robot.quadrant(steps) for robot in self]
    return [count for (quadrant, count) in collections.Counter(quadrants).items() if quadrant]

  @property
  def safety_factor(self) -> int:
    return functools.reduce(lambda x, y: x * y, self.quadrants_counts(100), 1)

  def is_easter_egg(self, steps: int) -> bool:
    positions = [robot.move(steps) for robot in self]
    return len(positions) == len(set(positions))

  @property
  def fewest_seconds_to_easter_egg(self) -> int:
    return next(i for i in itertools.count() if self.is_easter_egg(i))

  def print_image(self, steps: int):
    positions = [robot.move(steps) for robot in self]
    for y in range(int(self.size.imag)):
      for x in range(int(self.size.real)):
        if complex(x, y) in positions:
          print('█', end='')
        else:
          print(' ', end='')
      print('')
