from typing import Set, Tuple
from src.custom import CustomSet


class Box(Tuple[complex, int]):
  def __init__(self, origin_and_size: Tuple[complex, complex]):
    self.base, self.size = origin_and_size
    self.cells = {
      self.base + complex(x, y)
      for x in range(int(self.size.real))
      for y in range(int(self.size.imag))
    }

  def move(self, movement: complex) -> 'Box':
    return Box((self.base + movement, self.size))

  def draw_in(self, text):
    if self.size == 1 + 1j:
      text[int(self.base.imag)][int(self.base.real)] = 'O'
    elif self.size == 2 + 1j:
      text[int(self.base.imag)][int(self.base.real)] = '['
      text[int(self.base.imag)][int(self.base.real) + 1] = ']'
    else:
      raise Exception("Display of bigger size not implemented")


class Boxes(CustomSet[Box]):
  def __init__(self):
    super().__init__()
    self.ref = {}

  def _add_item(self, box: Box) -> Box:
    for cell in box.cells:
      self.ref[cell] = box
    return box

  def _remove_item(self, box: Box) -> Box:
    for cell in box.cells:
      self.ref.pop(cell, None)
    return box

  def move(self, push: complex, movement: complex, walls: Set[complex]) -> bool:
    cursors = {push}
    convoy = []
    while cursors & self.ref.keys():
      for cursor in list(cursors):
        if cursor not in self.ref:
          cursors.remove(cursor)
          continue
        box = self.ref[cursor]
        if box in convoy:
          cursors.remove(cursor)
          continue
        convoy.append(box)
        cursors.remove(cursor)
        cursors.update(box.move(movement).cells)
        if cursors & walls:
          return False
    while convoy:
      box = convoy.pop()
      self.remove(box)
      self.add(box.move(movement))
    return True


class Warehouse:
  movements_translation = {'^': -1j, 'v': 1j, '>': 1, '<': -1}

  def __init__(self, input_text: str, width_factor: int = 1):
    lines = input_text.strip().splitlines()
    self.walls = set()
    self.boxes = Boxes()
    self.robot = 0j
    for y, line in enumerate(lines):
      line = line.strip()
      if not line:
        break
      self.width = 0
      for x, cell in enumerate(line):
        pos = complex(width_factor * x, y)
        if cell == '#':
          self.walls.update({pos, pos + width_factor - 1})
        elif cell == 'O':
          self.boxes.add(Box((pos, width_factor + 1j)))
        elif cell == '@':
          self.robot = pos

    self.movements = [
      self.__class__.movements_translation[movement]
      for movement in ''.join(lines[y + 1:])
    ]

  def move(self):
    movement = self.movements.pop(0)
    new_robot = self.robot + movement
    if new_robot not in self.walls and self.boxes.move(new_robot, movement, self.walls):
      self.robot = new_robot

  def move_all(self):
    while len(self.movements) > 0:
      self.move()

  @property
  def gps_sum(self) -> int:
    return int(sum(100 * box.base.imag + box.base.real for box in self.boxes))

  def __str__(self):
    width = int(max(w.real for w in self.walls)) + 1
    height = int(max(w.imag for w in self.walls)) + 1
    text = [['.' for _ in range(width)] for _ in range(height)]
    for wall in self.walls:
      text[int(wall.imag)][int(wall.real)] = '#'
    for box in self.boxes:
      box.draw_in(text)
    text[int(self.robot.imag)][int(self.robot.real)] = '@'
    return '\n'.join([''.join(line) for line in text])
