from typing import Set, Callable, TypeAlias, Generator


def in_bounds(location: complex, bound: complex):
  return 0 <= location.real < bound.real and 0 <= location.imag < bound.imag


LocationKind: TypeAlias = Callable[[complex, complex, complex], Set[complex]]


def antinodes(antenna1: complex, antenna2: complex, bound: complex) -> Set[complex]:
  v = antenna2 - antenna1
  return {antinode for antinode in [antenna1 - v, antenna2 + v] if in_bounds(antinode, bound)}


antinodes: LocationKind = antinodes


def harmonics_range(start: complex, step: complex, bound: complex) -> Generator[complex, None, None]:
  while in_bounds(start, bound):
    yield start
    start += step


def harmonics(antenna1: complex, antenna2: complex, bound: complex) -> Set[complex]:
  v = antenna2 - antenna1
  return set(harmonics_range(antenna1, -v, bound)) | set(harmonics_range(antenna2, v, bound))


harmonics: LocationKind = harmonics


class Frequency:
  def __init__(self, antennas: Set[complex], bound: complex):
    self.antennas = antennas
    self.bound = bound

  def gather(self, kind: LocationKind):
    return {
      location
      for antenna1 in self.antennas for antenna2 in self.antennas if antenna1 != antenna2
      for location in kind(antenna1, antenna2, self.bound)
    }


class City:
  def __init__(self, input_text: str):
    cells = [list(line) for line in input_text.strip().splitlines()]
    self.width, self.height = len(cells[0]), len(cells)
    locations = {
      complex(x, y): cells[y][x]
      for y in range(self.height) for x in range(self.width)
      if cells[y][x] != '.'
    }
    self.frequencies = {
      frequency: Frequency({c for c, f in locations.items() if f == frequency}, complex(self.width, self.height))
      for frequency in set(locations.values())
    }

  def count_unique_locations(self, kind: LocationKind) -> int:
    return len({location for frequency in self.frequencies.values() for location in frequency.gather(kind)})
