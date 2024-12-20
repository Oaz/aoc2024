from src.day10 import *
from tests.aoc_harness import AocHarness
import os
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

output_dir = "/tmp/frames"
os.makedirs(output_dir, exist_ok=True)

cmap = plt.get_cmap('viridis')
num_colors = 10
colors = [cmap(i) for i in np.linspace(0, 1, num_colors)]

tm = TopoMap(AocHarness().read_puzzle_input(day=10))
k = 1
node_size = 10
dpi = 100
figsize_inches = (k * tm.x_size * node_size / dpi, k * tm.y_size * node_size / dpi)

layout = {
  c: (int(c.real), tm.y_size - int(c.imag))
  for c in tm.graph.nodes
}
node_colors = [colors[tm.heights[node]] for node in tm.graph.nodes]

n = 0
for start in tm.starting:
  for stop in tm.reachable_endings(start):
    plt.figure(figsize=figsize_inches, dpi=dpi)
    nx.draw(
      tm.graph, layout, with_labels=False,
      node_size=node_size, node_color=node_colors, arrows=False,
    )
    nx.draw_networkx_nodes(
      tm.graph, layout,
      nodelist=nx.shortest_path(tm.graph, source=start, target=stop),
      node_size=node_size*2, node_color='red',
    )
    n += 1
    frame_path = os.path.join(output_dir, f"frame_{n:05d}.png")
    print(f"Saving {frame_path}")
    plt.savefig(frame_path, bbox_inches='tight', pad_inches=0)
    plt.close()
