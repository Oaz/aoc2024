from src.day23 import *
from tests.aoc_harness import AocHarness
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt

lp = LanParty(AocHarness().read_puzzle_input(day=23))
cliques = nx.find_cliques(lp.graph)
max_clique = max(cliques, key=len)
max_clique_edges = list(combinations(max_clique, 2))

fig = plt.figure(figsize=(100, 100), dpi=100)
layout = nx.spring_layout(lp.graph)
nx.draw(
  lp.graph, layout,
  with_labels=True,
  node_size=5000,
  node_color='cyan',
  edge_color='white',
  width=2
)
nx.draw_networkx_nodes(
  lp.graph, layout,
  nodelist=max_clique,
  node_size=5000,
  node_color='orange'
)
nx.draw_networkx_edges(
  lp.graph, layout,
  edgelist=max_clique_edges,
  edge_color='green',
  width=5
)
fig.set_facecolor('black')
plt.show()
