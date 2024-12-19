class Towels:
  def __init__(self, input_text: str):
    lines = input_text.strip().splitlines()
    self.patterns = lines[0].split(', ')
    self.designs = lines[2:]
    self.possible_arrangements = {}

  def is_design_possible(self, design: str) -> bool:
    if len(design) == 0:
      return True
    for pattern in self.patterns:
      if design.startswith(pattern):
        if self.is_design_possible(design[len(pattern):]):
          return True
    return False

  @property
  def count_design_possible(self) -> int:
    return sum(1 for design in self.designs if self.is_design_possible(design))

  def count_possible_arrangements(self, design: str) -> int:
    if len(design) == 0:
      return 1
    if design in self.possible_arrangements:
      return self.possible_arrangements[design]
    possible = 0
    for pattern in self.patterns:
      if design.startswith(pattern):
        n = self.count_possible_arrangements(design[len(pattern):])
        possible += n
    self.possible_arrangements[design] = possible
    return possible

  @property
  def count_all_possible_arrangements(self) -> int:
    return sum(self.count_possible_arrangements(design) for design in self.designs)

