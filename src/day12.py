from itertools import groupby
from typing import Set, Tuple
import networkx as nx


class LazyProperty:
  def __init__(self, func):
    self.func = func

  def __get__(self, instance, owner):
    if instance is None:
      return self
    value = self.func(instance)
    setattr(instance, self.func.__name__, value)
    return value


class Region:
  def __init__(self, label: str, component: int, graph: nx.Graph):
    self.label, self.id = label, f'{label}{component}'
    self.graph, self.nodes, self.edges = graph, set(graph.nodes), set(graph.edges)
    self.area = len(graph.nodes)
    self.perimeter = 4 * self.area - 2 * len(graph.edges)
    self.price = self.area * self.perimeter

  @LazyProperty
  def sides(self) -> int:
    return sum(self.corners(node) for node in self.nodes)

  @LazyProperty
  def bulk_price(self) -> int:
    return self.area * self.sides

  def corners(self, node: complex) -> int:
    connections = set(self.graph.edges(node))
    if len(connections) == 0:
      return 4
    if len(connections) == 1:
      return 2
    return sum(
      self.count_corner(node, dx, dy, connections)
      for dx in [-1, 1]
      for dy in [-1, 1]
    )

  def count_corner(self, node: complex, dx: int, dy: int, connections: Set[Tuple[complex, complex]]) -> int:
    horizontal_neighbour = node + complex(dx, 0)
    vertical_neighbour = node + complex(0, dy)
    diagonal_neighbour = node + complex(dx, dy)
    if ((node, horizontal_neighbour) in connections) ^ ((node, vertical_neighbour) in connections):
      return 0
    if diagonal_neighbour not in self.nodes:
      return 1
    if horizontal_neighbour not in self.nodes and vertical_neighbour not in self.nodes:
      return 1
    return 0

  def __repr__(self):
    return f"Region({self.id}, {self.edges})"


class Garden:
  def __init__(self, input_text: str):
    self.rows = [
      [plot for plot in row.strip()]
      for row in input_text.strip().splitlines()
    ]
    self.width, self.height = len(self.rows[0]), len(self.rows)

  @LazyProperty
  def regions(self) -> Set[Region]:
    graph = nx.Graph()
    for x in range(self.width):
      for y in range(self.height):
        node = complex(x, y)
        if y < self.height - 1:
          graph.add_edge(node, node + 1j)
        if x < self.width - 1:
          graph.add_edge(node, node + 1)
    labels = {
      complex(x, y): self.rows[y][x]
      for x in range(0, self.width)
      for y in range(0, self.height)
    }
    sorted_nodes = sorted(graph.nodes(), key=lambda n: labels[n])
    return {
      Region(label, component_id, nx.Graph(graph.subgraph(component_nodes)))
      for label, group in groupby(sorted_nodes, key=lambda n: labels[n])
      for component_id, component_nodes in enumerate(nx.connected_components(graph.subgraph(group)))
    }

  @LazyProperty
  def price(self) -> int:
    return sum(region.price for region in self.regions)

  @LazyProperty
  def bulk_price(self) -> int:
    return sum(region.bulk_price for region in self.regions)
