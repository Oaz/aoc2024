import unittest
from tests.aoc_harness import AocHarness
from src.day10 import *


class TestsDay10(AocHarness):

  def test_tiny_example(self):
    tm = TopoMap('''
0123
1234
8765
9876
''')
    self.assertEqual({0}, tm.starting)
    self.assertEqual({3j}, tm.ending)
    self.assertEqual(1, tm.trailhead_score(0))
    self.assertEqual(1, tm.count_paths)

  def test_score_example(self):
    tm = TopoMap('''
...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
''')
    self.assertEqual({3}, tm.starting)
    self.assertEqual({6j, 6 + 6j}, tm.ending)
    self.assertEqual(2, tm.trailhead_score(3))
    self.assertEqual(2, tm.count_paths)

  def test_other_score_example(self):
    tm = TopoMap('''
..90..9
...1.98
...2..7
6543456
765.987
876....
987....
''')
    self.assertEqual({3}, tm.starting)
    self.assertEqual({2, 6, 5 + 1j, 4 + 4j, 6j}, tm.ending)
    self.assertEqual(4, tm.trailhead_score(3))
    self.assertEqual(4, tm.count_paths)

  def test_part1_example(self):
    tm = TopoMap('''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
    ''')
    self.assertEqual({
      (2 + 0j, 5),
      (4 + 0j, 6),
      (4 + 2j, 5),
      (6 + 4j, 3),
      (2 + 5j, 1),
      (5 + 5j, 3),
      (6j, 5),
      (6 + 6j, 3),
      (1 + 7j, 5)
    }, {(head, tm.trailhead_score(head)) for head in tm.starting})
    self.assertEqual(36, tm.count_paths)

  def test_part1_puzzle(self):
    topo_map = TopoMap(self.read_puzzle_input(day=10))
    self.assertEqual(644, topo_map.count_paths)

  def test_part2_example(self):
    tm = TopoMap('''
89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732
        ''')
    self.assertEqual({
      (2 + 0j, 20),
      (4 + 0j, 24),
      (4 + 2j, 10),
      (6 + 4j, 4),
      (2 + 5j, 1),
      (5 + 5j, 4),
      (6j, 5),
      (6 + 6j, 8),
      (1 + 7j, 5)
    }, {(head, tm.trailhead_rating(head)) for head in tm.starting})
    self.assertEqual(81, tm.sum_of_trailheads_ratings)

  def test_part2_puzzle(self):
    topo_map = TopoMap(self.read_puzzle_input(day=10))
    self.assertEqual(1366, topo_map.sum_of_trailheads_ratings)


if __name__ == '__main__':
  unittest.main()
