from typing import Tuple
import re
import networkx as nx


class MemorySpace:
  def __init__(self, xy_max: int, input_text: str):
    self.size = xy_max + 1
    self.bytes = [
      (int(x), int(y))
      for line in input_text.strip().splitlines()
      for x, y in re.findall(r'(\d+),(\d+)', line)
    ]
    self.exit = (xy_max, xy_max)
    self.graph = nx.Graph()
    for y in range(self.size):
      for x in range(self.size):
        if y < xy_max:
          self.graph.add_edge((x, y), (x, y + 1))
        if x < xy_max:
          self.graph.add_edge((x, y), (x + 1, y))

  def drop(self, n: int = 1):
    while n > 0:
      byte = self.bytes.pop(0)
      self.graph.remove_node(byte)
      n -= 1

  @property
  def minimum_steps_to_exit(self) -> int | None:
    return nx.shortest_path_length(self.graph, source=(0, 0), target=self.exit)

  @property
  def coordinates_first_byte_that_prevent_exit(self) -> Tuple[int, int] | None:
    while len(self.bytes) > 1:
      byte = self.bytes.pop(0)
      self.graph.remove_node(byte)
      if nx.has_path(self.graph, source=(0, 0), target=self.exit):
        continue
      return byte
    return None

  @property
  def bar(self) -> int:
    return 0
