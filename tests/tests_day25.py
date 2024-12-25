import unittest
from tests.aoc_harness import AocHarness
from src.day25 import *


class TestsDay25(AocHarness):

  def setUp(self):
    self.example = LocksAndKeys('''
#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####
      ''')

  def test_example_parsing(self):
    self.assertEqual([0, 5, 3, 4, 3], parse('''
.####
.####
.####
.#.#.
.#...
.....
    '''.strip().splitlines()))
    self.assertEqual([[0, 5, 3, 4, 3], [1, 2, 0, 5, 3]], self.example.locks)
    self.assertEqual([[5, 0, 2, 1, 3], [4, 3, 4, 0, 2], [3, 0, 2, 0, 1]], self.example.keys)

  def test_part1_example(self):
    self.assertEqual(3, self.example.uniques_fit_without_overlapping)

  def test_part1_puzzle(self):
    s = LocksAndKeys(self.read_puzzle_input(day=25))
    self.assertEqual(3525, s.uniques_fit_without_overlapping)


if __name__ == '__main__':
  unittest.main()
