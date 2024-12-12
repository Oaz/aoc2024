import unittest
from tests.aoc_harness import AocHarness
from src.day12 import *


class TestsDay12(AocHarness):

  def setUp(self):
    self.g1 = Garden('''
AAAA
BBCD
BBCC
EEEC
          ''')
    self.g2 = Garden('''
  OOOOO
  OXOXO
  OOOOO
  OXOXO
  OOOOO
                ''')
    self.g3 = Garden('''
    RRRRIICCFF
    RRRRIICCCF
    VVRRRCCFFF
    VVRCCCJFFF
    VVVVCJJCFE
    VVIVCCJJEE
    VVIIICJJEE
    MIIIIIJJEE
    MIIISIJEEE
    MMMISSJEEE
                  ''')
    self.g4 = Garden('''
    EEEEE
    EXXXX
    EEEEE
    EXXXX
    EEEEE
                    ''')
    self.g5 = Garden('''
AAAAAA
AAABBA
AAABBA
ABBAAA
ABBAAA
AAAAAA
                  ''')

  def test_parsing(self):
    self.assertEqual([
      ['A', 'A', 'A', 'A'],
      ['B', 'B', 'C', 'D'],
      ['B', 'B', 'C', 'C'],
      ['E', 'E', 'E', 'C']
    ], self.g1.rows)

  def test_part1_example1(self):
    self.assertEqual({
      ('A0', 4, 10, 40),
      ('B0', 4, 8, 32),
      ('C0', 4, 10, 40),
      ('D0', 1, 4, 4),
      ('E0', 3, 8, 24),
    }, {(r.id, r.area, r.perimeter, r.price) for r in self.g1.regions})
    self.assertEqual(140, self.g1.price)

  def test_part1_example2(self):
    self.assertEqual({
      ('O0', 21, 36, 756),
      ('X0', 1, 4, 4),
      ('X1', 1, 4, 4),
      ('X2', 1, 4, 4),
      ('X3', 1, 4, 4),
    }, {(r.id, r.area, r.perimeter, r.price) for r in self.g2.regions})
    self.assertEqual(772, self.g2.price)

  def test_part1_example3(self):
    self.assertEqual({
      ('R0', 12, 18, 216),
      ('I1', 4, 8, 32),
      ('C0', 14, 28, 392),
      ('F0', 10, 18, 180),
      ('V0', 13, 20, 260),
      ('J0', 11, 20, 220),
      ('C1', 1, 4, 4),
      ('E0', 13, 18, 234),
      ('I0', 14, 22, 308),
      ('M0', 5, 12, 60),
      ('S0', 3, 8, 24),
    }, {(r.id, r.area, r.perimeter, r.price) for r in self.g3.regions})
    self.assertEqual(1930, self.g3.price)

  def test_part1_puzzle(self):
    g = Garden(self.read_puzzle_input(day=12))
    self.assertEqual(1488414, g.price)

  def test_part2_example1(self):
    self.assertEqual({
      ('A0', 4, 4, 16),
      ('B0', 4, 4, 16),
      ('C0', 4, 8, 32),
      ('D0', 1, 4, 4),
      ('E0', 3, 4, 12),
    }, {(r.id, r.area, r.sides, r.bulk_price) for r in self.g1.regions})
    self.assertEqual(80, self.g1.bulk_price)

  def test_part2_example2(self):
    self.assertEqual({
      ('O0', 21, 20, 420),
      ('X0', 1, 4, 4),
      ('X1', 1, 4, 4),
      ('X2', 1, 4, 4),
      ('X3', 1, 4, 4),
    }, {(r.id, r.area, r.sides, r.bulk_price) for r in self.g2.regions})
    self.assertEqual(436, self.g2.bulk_price)

  def test_part2_example4(self):
    self.assertEqual({
      ('X0', 4, 4, 16),
      ('X1', 4, 4, 16),
      ('E0', 17, 12, 204)
    }, {(r.id, r.area, r.sides, r.bulk_price) for r in self.g4.regions})
    self.assertEqual(236, self.g4.bulk_price)

  def test_part2_example5(self):
    self.assertEqual({
      ('A0', 28, 12, 336),
      ('B0', 4, 4, 16),
      ('B1', 4, 4, 16)
    }, {(r.id, r.area, r.sides, r.bulk_price) for r in self.g5.regions})
    self.assertEqual(368, self.g5.bulk_price)

  def test_part2_example3(self):
    self.assertEqual({
      ('R0', 12, 10, 120),
      ('I1', 4, 4, 16),
      ('C0', 14, 22, 308),
      ('F0', 10, 12, 120),
      ('V0', 13, 10, 130),
      ('J0', 11, 12, 132),
      ('C1', 1, 4, 4),
      ('E0', 13, 8, 104),
      ('I0', 14, 16, 224),
      ('M0', 5, 6, 30),
      ('S0', 3, 6, 18),
    }, {(r.id, r.area, r.sides, r.bulk_price) for r in self.g3.regions})
    self.assertEqual(1206, self.g3.bulk_price)

  def test_part2_puzzle(self):
    foo = Garden(self.read_puzzle_input(day=12))
    self.assertEqual(911750, foo.bulk_price)


if __name__ == '__main__':
  unittest.main()
