from src.day18 import *
from tests.aoc_harness import AocHarness
import os
import networkx as nx
import matplotlib.pyplot as plt

node_size = 4
img_size = 600
figsize_inches = (img_size / 100, img_size / 100)
plt.gca().set_axis_off()

output_dir = "/tmp/frames"
os.makedirs(output_dir, exist_ok=True)

ms = MemorySpace(70, AocHarness().read_puzzle_input(day=18))
layout = {(x, y): (x, ms.size - y) for x, y in ms.graph.nodes}

path = nx.shortest_path(ms.graph, source=(0, 0), target=ms.exit)
n = 0
while len(ms.bytes) > 1:
  byte = ms.bytes.pop(0)
  ms.graph.remove_node(byte)
  if not nx.has_path(ms.graph, source=(0, 0), target=ms.exit):
    break
  n += 1
  plt.figure(figsize=figsize_inches, dpi=100)
  nx.draw(
    ms.graph, layout, with_labels=False,
    node_size=node_size,
    node_color='blue',
    width=node_size / 8,
    edge_color='black'
  )
  if byte in path:
    path = nx.shortest_path(ms.graph, source=(0, 0), target=ms.exit)
  nx.draw(
    ms.graph, layout, with_labels=False,
    nodelist=path,
    node_size=node_size * 3,
    node_color='red',
    edgelist=[],
  )
  frame_path = os.path.join(output_dir, f"frame_{n:05d}.png")
  print(f"Saving {frame_path}")
  plt.savefig(frame_path, bbox_inches='tight', pad_inches=0)
  plt.close()
