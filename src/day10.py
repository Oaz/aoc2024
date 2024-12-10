from typing import Set

import networkx as nx


class TopoMap:
  def __init__(self, input_text: str):
    lines = input_text.strip().splitlines()
    heights = {
      complex(x, y): int(char)
      for y, line in enumerate(lines)
      for x, char in enumerate(line)
      if char != '.'
    }
    self.nodes = {node for node in heights.keys()}
    self.starting = {node for node in heights.keys() if heights[node] == 0}
    self.ending = {node for node in heights.keys() if heights[node] == 9}
    self.graph = nx.DiGraph()
    self.graph.add_nodes_from(heights.keys())
    directions = [-1 + 0j, 1 + 0j, 0 - 1j, 0 + 1j]
    self.graph.add_edges_from(
      (node, neighbor)
      for direction in directions
      for node in heights.keys()
      if (neighbor := node + direction) in self.nodes and heights[neighbor] == heights[node] + 1
    )

  def reachable_endings(self, head: complex) -> Set[complex]:
    return {reach for reach in nx.descendants(self.graph, head) if reach in self.ending}

  def trailhead_score(self, head: complex) -> int:
    return len({reach for reach in self.reachable_endings(head)})

  @property
  def count_paths(self) -> int:
    return sum(self.trailhead_score(node) for node in self.starting)

  def trailhead_rating(self, head: complex) -> int:
    return sum(
      1
      for reach in self.reachable_endings(head)
      for _ in nx.all_simple_paths(self.graph, source=head, target=reach)
    )

  @property
  def sum_of_trailheads_ratings(self) -> int:
    return sum(self.trailhead_rating(node) for node in self.starting)
