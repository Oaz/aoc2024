from itertools import product
from typing import Dict, Tuple, List
import networkx as nx
import re
import numpy as np

numericPad = {
  (0, 0): '7',
  (1, 0): '8',
  (2, 0): '9',
  (0, 1): '4',
  (1, 1): '5',
  (2, 1): '6',
  (0, 2): '1',
  (1, 2): '2',
  (2, 2): '3',
  (1, 3): '0',
  (2, 3): 'A',
}

directionalPad = {
  (1, 0): '^',
  (2, 0): 'A',
  (0, 1): '<',
  (1, 1): 'v',
  (2, 1): '>',
}


class Keypad:
  def __init__(self, layout: Dict[Tuple[int, int], str]):
    width = max(x for x, _ in layout.keys()) + 1
    height = max(y for _, y in layout.keys()) + 1
    g = nx.grid_2d_graph(width, height)
    g.remove_nodes_from(g.nodes - layout.keys())
    g = g.to_directed()
    labels = {edge: {'label': value} for edge in g.edges if (value := self.edge_label(edge)) is not None}
    nx.set_edge_attributes(g, labels)
    nx.relabel_nodes(g, layout, copy=False)
    self.graph = g
    self.bests = {
      (a, b): min(
        self.all_from_to(a, b),
        key=lambda s: len([s[i] for i in range(len(s)) if i == 0 or s[i] != s[i - 1]])
      )
      for a, b in product(layout.values(), layout.values())
    }

  def best_from_to(self, start: str, end: str) -> str:
    return self.bests[(start, end)]

  def all_from_to(self, start: str, end: str) -> List[str]:
    paths = nx.all_shortest_paths(self.graph, start, end)
    return [self.path_to_labels(path) for path in paths]

  def path_to_labels(self, path: List[str]) -> str:
    path_labels = [self.graph.edges[(path[i], path[i + 1])]['label'] for i in range(len(path) - 1)]
    return ''.join(path_labels) + 'A'

  def best_sequence(self, outcome: str) -> str:
    steps = [self.best_from_to(a, b) for a, b in zip('A' + outcome, outcome)]
    return ''.join(steps)

  def best_sequences(self, outcome: str) -> List[str]:
    steps = [self.best_from_to(a, b) for a, b in zip('A' + outcome, outcome)]
    return steps

  def all_sequences(self, outcome: str) -> List[str]:
    all_steps = [self.all_from_to(a, b) for a, b in zip('A' + outcome, outcome)]
    combinations = [''.join(combination) for combination in product(*all_steps)]
    return combinations

  def send(self, order: str) -> str:
    current = 'A'
    pressed = ''
    for label in order:
      if label == 'A':
        pressed = pressed + current
        continue
      for neighbor in self.graph.neighbors(current):
        if self.graph.edges[current, neighbor].get("label") == label:
          current = neighbor
          break
    return pressed

  @property
  def atomic_moves(self):
    return nx.get_edge_attributes(self.graph, 'label')

  @staticmethod
  def edge_label(edge: Tuple[Tuple[int, int], Tuple[int, int]]) -> str:
    (x1, y1), (x2, y2) = edge
    dx, dy = x2 - x1, y2 - y1
    labels = {
      (0, 1): 'v',
      (0, -1): '^',
      (1, 0): '>',
      (-1, 0): '<',
    }
    return labels.get((dx, dy), None)

  @property
  def key_pairs(self):
    return product(self.graph.nodes, self.graph.nodes)


class Robot:
  numeric = Keypad(numericPad)
  directional = Keypad(directionalPad)

  @classmethod
  def init(cls):
    cls.sequences = cls._compute_sequences()
    cls._transitions = cls._compute_transitions()
    cls.indexes = {key: idx for idx, key in enumerate(cls._transitions.keys())}
    cls.tokens = {idx: key for key, idx in cls.indexes.items()}
    cls.matrix = cls._create_matrix()

  @classmethod
  def _compute_sequences(cls) -> Dict[Tuple[str,str], str]:
    sequences = {(a, b): cls.numeric.best_from_to(a, b) for a, b in cls.numeric.key_pairs}
    sequences.update({(a, b): cls.directional.best_from_to(a, b) for a, b in cls.directional.key_pairs})
    return sequences

  @classmethod
  def _compute_transitions(cls) -> Dict[str, List[str]]:
    transitions = {}
    for _, sequence in cls.sequences.items():
      transitions[sequence] = cls.directional.best_sequences(sequence)[::-1]
    return transitions

  @classmethod
  def count_transitions(cls, items) -> np.ndarray:
    counts = np.zeros(len(cls.indexes), dtype=int)
    for item in items:
      if item in cls.indexes:
        idx = cls.indexes[item]
        counts[idx] += 1
    return counts

  @classmethod
  def _create_matrix(cls) -> np.ndarray:
    transition_matrix = np.zeros((len(cls.indexes), len(cls.indexes)), dtype=int)
    for from_key, to_keys in cls._transitions.items():
      from_idx = cls.indexes[from_key]
      counts = cls.count_transitions(to_keys)
      transition_matrix[:, from_idx] = counts
    return transition_matrix


Robot.init()


class RobotChain:
  def __init__(self, length: int = 2):
    self.chain_length = length
    self.matrix = np.linalg.matrix_power(Robot.matrix, length)
    self.token_lengths = np.zeros(len(Robot.indexes), dtype=int)
    for token, idx in Robot.indexes.items():
      self.token_lengths[idx] = len(token)

  def sequence_length(self, outcome: str) -> int:
    vector = Robot.count_transitions(Robot.numeric.best_sequences(outcome))
    result = self.matrix @ vector
    length = np.dot(result, self.token_lengths)
    return length

  def sequence(self, outcome: str) -> str:
    outcome = Robot.numeric.best_sequence(outcome)
    for _ in range(self.chain_length):
      outcome = Robot.directional.best_sequence(outcome)
    return outcome

  def send(self, order: str) -> str:
    for _ in range(self.chain_length):
      order = Robot.directional.send(order)
    return Robot.numeric.send(order)


class Codes:
  def __init__(self, input_text: str):
    self.keys = [line.strip() for line in input_text.strip().splitlines()]
    self.codes = [int(code) for code in re.findall(r'\d+', input_text)]

  def sum_of_complexities(self, number_of_directional_keypad_robots: int = 2) -> int:
    rc = RobotChain(number_of_directional_keypad_robots)
    lengths = [rc.sequence_length(key) for key in self.keys]
    complexities = [code * length for code, length in zip(self.codes, lengths)]
    return sum(complexities)
