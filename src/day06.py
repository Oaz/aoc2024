from typing import List, Tuple, Dict


class Lab:
  @staticmethod
  def parse(input_text: str):
    input_text = input_text.strip()
    cells = [list(line) for line in input_text.strip().splitlines()]
    width = len(cells[0])
    height = len(cells)
    cells = {complex(x, y): (cells[y][x] == '#') for y in range(height) for x in range(width)}
    mark = input_text.index("^")
    start_position = complex(mark % (width + 1), mark // (width + 1))
    return Lab(width, height, start_position, cells)

  def __init__(self, width, height, start_position, cells: Dict[complex, bool]):
    self.width, self.height, self.start_position, self.cells = width, height, start_position, cells

  def is_obstacle(self, c: complex) -> bool: return self.cells.get(c) is True


class GuardBase:
  def __init__(self, lab: Lab):
    self.lab = lab
    self.position = lab.start_position
    self.direction = complex(0, -1)
    self.in_loop = False

  def visit(self):
    pass

  def move_until_obstacle(self):
    next_position = self.position + self.direction
    while self.lab.cells.get(next_position) is False and not self.in_loop:
      self.position = next_position
      self.visit()
      next_position = self.position + self.direction
    if self.lab.cells.get(next_position) is True:
      self.direction *= complex(0, 1)

  def move_until_leaving(self):
    while self.lab.cells.get(self.position + self.direction) is not None and not self.in_loop:
      self.move_until_obstacle()


class Guard(GuardBase):
  def __init__(self, lab: Lab):
    super().__init__(lab)
    self.visited_positions = {self.position}

  @property
  def visited(self):
    return len(self.visited_positions)

  def visit(self):
    self.visited_positions.add(self.position)

  def __str__(self):
    return '\n'.join(''.join(
      '#' if self.lab.cells.get(complex(x, y)) is True else 'X' if complex(x, y) in self.visited_positions else '.'
      for x in range(self.lab.width)
    ) for y in range(self.lab.height))


class LoopingGuard(GuardBase):
  def __init__(self, lab: Lab):
    super().__init__(lab)
    self.visited_positions_and_directions = {(self.position, self.direction)}
    self.in_loop = False

  def visit(self):
    position_and_direction = (self.position, self.direction)
    if position_and_direction in self.visited_positions_and_directions:
      self.in_loop = True
    else:
      self.visited_positions_and_directions.add(position_and_direction)


class LabHack:
  def __init__(self, lab: Lab):
    self.lab = lab

  def hack_guard_with(self, obstruction) -> LoopingGuard:
    cells = self.lab.cells.copy()
    cells[obstruction] = True
    lab = Lab(self.lab.width, self.lab.height, self.lab.start_position, cells)
    guard = LoopingGuard(lab)
    guard.move_until_leaving()
    return guard

  def is_loop(self, obstruction) -> bool:
    return self.hack_guard_with(obstruction).in_loop

  @property
  def efficient_obstructions(self) -> List[Tuple[int, int]]:
    guard = Guard(self.lab)
    guard.move_until_leaving()
    return [candidate for candidate in guard.visited_positions if self.is_loop(candidate)]

  @property
  def count_efficient_obstructions(self) -> int:
    return len(self.efficient_obstructions)

  def __str__(self):
    guard = Guard(self.lab)
    guard.move_until_leaving()
    obstructions = set(self.efficient_obstructions)
    txt = ''
    for y in range(self.lab.height):
      for x in range(self.lab.width):
        c = complex(x, y)
        txt += (
          '#' if self.lab.is_obstacle(c)
          else 'O' if c in obstructions
          else 'X' if c in guard.visited_positions
          else '.'
        )
      txt += '\n'
    return txt
