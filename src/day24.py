from typing import Dict, Set, List
import networkx as nx


class Gate:
  def __init__(self, a, b, result):
    self.a = a
    self.b = b
    self.result = result
    self.inputs = sorted([self.a, self.b])
    ix = self.inputs[0][1:]
    iy = self.inputs[1][1:]
    self.level_one_index = int(ix) if (self.inputs[0][0], self.inputs[1][0]) == ('x', 'y') and ix == iy else None
    self.is_z = result[0] == 'z'

  def input_gates(self, gates: Dict[str, 'Gate']) -> List['Gate']:
    return [gates[input] for input in self.inputs]

  def __repr__(self):
    return f'({self.a}-{self.b}-{self.__class__.__name__}-{self.result})'


class XorGate(Gate):
  def __init__(self, a, b, result):
    super().__init__(a, b, result)

  def compute(self, values: Dict[str, int]) -> int:
    return values[self.a] ^ values[self.b]

  def find_weird(self, gates: Dict[str, 'Gate'], bits: int) -> Set['Gate']:
    if self.level_one_index is not None:
      return {self} if self.is_z and self.level_one_index > 0 else set()
    weird = {gate for gate in self.input_gates(gates) if gate.__class__ is AndGate and gate.level_one_index != 0}
    if not self.is_z:
      weird.add(self)
    return weird


class AndGate(Gate):
  def __init__(self, a, b, result):
    super().__init__(a, b, result)

  def compute(self, values: Dict[str, int]) -> int:
    return values[self.a] & values[self.b]

  def find_weird(self, gates: Dict[str, 'Gate'], bits: int) -> Set['Gate']:
    if self.level_one_index is not None:
      return {self} if self.is_z else set()
    weird = {gate for gate in self.input_gates(gates) if gate.__class__ is AndGate and gate.level_one_index != 0}
    if self.is_z:
      weird.add(self)
    return weird


class OrGate(Gate):
  def __init__(self, a, b, result):
    super().__init__(a, b, result)

  def compute(self, values: Dict[str, int]) -> int:
    return values[self.a] | values[self.b]

  def find_weird(self, gates: Dict[str, 'Gate'], bits: int) -> Set['Gate']:
    weird = {gate for gate in self.input_gates(gates) if gate.__class__ is not AndGate}
    if self.is_z:
      weird.update({
        self for gate in self.input_gates(gates)
        if gate.__class__ is AndGate and gate.level_one_index is not None and gate.level_one_index < bits - 1
      })
    return weird


class Device:
  def __init__(self, input_text: str):
    lines = input_text.strip().splitlines()
    split = lines.index('')
    self.initial_values = {line[0:3]: int(line[5]) for line in lines[:split]}
    gate_factory = {'AND': AndGate, 'OR': OrGate, 'XOR': XorGate}
    self.gates = {
      word[4]: gate_factory[word[1]](word[0], word[2], word[4])
      for word in [line.split(' ') for line in lines[split + 1:]]
    }
    self.dependencies = nx.DiGraph()
    for gate in self.gates.values():
      self.dependencies.add_edge(gate.result, gate.a)
      self.dependencies.add_edge(gate.result, gate.b)
    self.forward = list(nx.topological_sort(nx.reverse(self.dependencies)))
    self.defaults = {node: 0 for node in self.initial_values if node[0] == 'x' or node[0] == 'y'}

  @property
  def output(self):
    return self.compute(self.initial_values.copy())

  def compute(self, values: Dict[str, int]) -> int:
    for node in self.forward:
      if node not in values:
        values[node] = self.gates[node].compute(values)
    result = 0
    zs = sorted([z.result for z in self.gates.values() if z.is_z])
    while len(zs) > 0:
      result = 2 * result + values[zs.pop()]
    return result

  @property
  def involved_in_swap(self):
    bits = len(self.defaults) // 2
    return ','.join(sorted([
      gate.result for gate in set().union(*(gate.find_weird(self.gates, bits) for gate in self.gates.values()))
    ]))
