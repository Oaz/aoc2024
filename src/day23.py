from itertools import combinations
import networkx as nx


class LanParty:
  def __init__(self, input_text: str):
    self.graph = nx.Graph()
    self.graph.add_edges_from([(line[0:2], line[3:]) for line in input_text.strip().splitlines()])

  @property
  def sets_of_three_connected_computers(self):
    return nx.simple_cycles(self.graph, length_bound=3)

  @property
  def number_of_three_connected_computers_sets_where_one_is_starting_with_letter_t(self):
    triangles = set()
    for node in self.graph:
      if not node.startswith('t'):
        continue
      for neighbor_pair in combinations(self.graph[node], 2):
        if self.graph.has_edge(*neighbor_pair):
          triangles.add(tuple(sorted((node,) + neighbor_pair)))
    return len(triangles)

  @property
  def password(self):
    cliques = nx.find_cliques(self.graph)
    max_clique = max(cliques, key=len)
    return ','.join(sorted(max_clique))

