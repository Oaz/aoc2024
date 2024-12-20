from typing import Dict, Tuple
from scipy.spatial import cKDTree


class Race:
  def __init__(self, input_text: str):
    self.cells = [list(line.strip()) for line in input_text.strip().splitlines()]
    self.track_cells = set()
    self.walls = set()
    for y, line in enumerate(self.cells):
      for x, char in enumerate(line):
        xy = (x, y)
        if char == '.':
          self.track_cells.add(xy)
        elif char == '#':
          self.walls.add(xy)
        elif char == 'S':
          self.start = xy
        elif char == 'E':
          self.end = xy
    previous = set()
    current = self.start
    self.track = [current]
    while True:
      x, y = current
      follow = list(({(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)} - previous).intersection(self.track_cells))
      if len(follow) == 0:
        self.track.append(self.end)
        break
      previous = {current}
      current = follow[0]
      self.track.append(current)
    self.tree = cKDTree(self.track)

  @property
  def boring_track_time(self) -> int:
    return len(self.track) - 1

  def number_of_cheats(self, min_cheat_save: int, max_cheat_length: int) -> int:
    return len(self.cheats(min_cheat_save=min_cheat_save, max_cheat_length=max_cheat_length))

  def cheats(self, min_cheat_save: int, max_cheat_length: int) -> Dict[Tuple[Tuple[int, int], Tuple[int, int]], int]:
    cheats = {}
    for start_cheat_index in range(len(self.track) - 1):
      start_cheat = self.track[start_cheat_index]
      neighbors = self.tree.query_ball_point(start_cheat, max_cheat_length, p=1)
      for end_cheat_index in neighbors:
        if end_cheat_index <= start_cheat_index:
          continue
        end_cheat = self.track[end_cheat_index]
        track_length = end_cheat_index - start_cheat_index
        manhattan_length = abs(start_cheat[0] - end_cheat[0]) + abs(start_cheat[1] - end_cheat[1])
        cheat_save = track_length - manhattan_length
        if cheat_save >= min_cheat_save:
          cheats[(start_cheat, end_cheat)] = cheat_save
    return cheats
