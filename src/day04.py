from typing import Tuple


class WordSearch:
  def __init__(self, input_text: str):
    self.letters = input_text.strip().splitlines()
    self.width = len(self.letters[0])
    self.height = len(self.letters)
    self.positions = [(x, y) for y in range(self.height) for x in range(self.width)]
    self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

  def char_at(self, x: int, y: int) -> str:
    return self.letters[y][x] if 0 <= x < self.width and 0 <= y < self.height else ' '

  def is_word_at(self, start: Tuple[int, int], direction: Tuple[int, int]) -> bool:
    x, y = start
    dx, dy = direction
    word = "XMAS"
    return ''.join([self.char_at(x + i * dx, y + i * dy) for i in range(len(word))]) == word

  @property
  def count_word(self) -> int:
    return sum([1 for d in self.directions for p in self.positions if self.is_word_at(p, d)])

  def is_cross_at(self, center: Tuple[int, int]) -> bool:
    x, y = center
    slash = ''.join([self.char_at(x - 1, y + 1), self.char_at(x, y), self.char_at(x + 1, y - 1)])
    anti_slash = ''.join([self.char_at(x - 1, y - 1), self.char_at(x, y), self.char_at(x + 1, y + 1)])
    return (slash == "MAS" or slash == "SAM") and (anti_slash == "MAS" or anti_slash == "SAM")

  @property
  def count_cross(self) -> int:
    return sum([1 for position in self.positions if self.is_cross_at(position)])
