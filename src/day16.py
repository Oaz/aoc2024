import networkx as nx


class Maze:
  def __init__(self, input_text: str):
    cells = [list(line.strip()) for line in input_text.strip().splitlines()]
    g = nx.DiGraph()
    turn_cost = 1000
    forward_cost = 1
    for y, line in enumerate(cells):
      for x, char in enumerate(line):
        if char == '#':
          continue
        n = (x, y, 'N')
        s = (x, y, 'S')
        e = (x, y, 'E')
        w = (x, y, 'W')
        can_go_S = (cells[y + 1][x] != '#')
        can_go_N = (cells[y - 1][x] != '#')
        can_go_E = (cells[y][x + 1] != '#')
        can_go_W = (cells[y][x - 1] != '#')
        if char == 'S':
          # start always at bottom left and can only turn north or move foward to east
          self.start = e
          if can_go_N:
            g.add_edge(e, n, weight=turn_cost)
        if char == 'E':
          # end always at top right and can only come from south or west
          self.end = [n, e]
        if can_go_N and can_go_E:
          g.add_edge(s, e, weight=turn_cost)
          g.add_edge(w, n, weight=turn_cost)
        if can_go_N and can_go_W:
          g.add_edge(s, w, weight=turn_cost)
          g.add_edge(e, n, weight=turn_cost)
        if can_go_S and can_go_E:
          g.add_edge(n, e, weight=turn_cost)
          g.add_edge(w, s, weight=turn_cost)
        if can_go_S and can_go_W:
          g.add_edge(n, w, weight=turn_cost)
          g.add_edge(e, s, weight=turn_cost)
        if can_go_S:
          g.add_edge(s, (x, y + 1, 'S'), weight=forward_cost)
        if can_go_N:
          g.add_edge(n, (x, y - 1, 'N'), weight=forward_cost)
        if can_go_E:
          g.add_edge(e, (x + 1, y, 'E'), weight=forward_cost)
        if can_go_W:
          g.add_edge(w, (x - 1, y, 'W'), weight=forward_cost)
    self.cells = cells
    self.graph = g

  def cost_to(self, node):
    return nx.shortest_path_length(self.graph, source=self.start, target=node, weight='weight')

  @property
  def lowest_score(self) -> int:
    min_cost = float('inf')
    for endpoint in self.end:
      cost = self.cost_to(endpoint)
      if cost < min_cost:
        min_cost = cost
    return min_cost

  @property
  def number_of_best_spots(self) -> int:
    shortest_cost = self.lowest_score
    all_best_spots = set()
    for endpoint in self.end:
      cost = self.cost_to(endpoint)
      if cost > shortest_cost:
        continue
      for path in nx.all_shortest_paths(self.graph, source=self.start, target=endpoint, weight='weight'):
        all_best_spots.update({(x, y) for x, y, _ in path})
    return len(all_best_spots)

  def print_path(self, nodes):
    coords = {(x, y) for x, y, _ in nodes}
    for y, line in enumerate(self.cells):
      for x, char in enumerate(line):
        if (x, y) in coords:
          print('O', end='')
        else:
          print(char, end='')
      print('')
