import unittest
from tests.aoc_harness import AocHarness
from src.day16 import *


class TestsDay16(AocHarness):

  def setUp(self):
    self.example1 = '''
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
      '''

    self.example2 = '''
#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################
        '''

  def test_part1_example1(self):
    m = Maze(self.example1)
    self.assertEqual(7036, m.lowest_score)

  def test_part1_example2(self):
    m = Maze(self.example2)
    self.assertEqual(11048, m.lowest_score)

  def test_part1_puzzle(self):
    m = Maze(self.read_puzzle_input(day=16))
    self.assertEqual(66404, m.lowest_score)

  def test_part2_example1(self):
    m = Maze(self.example1)
    self.assertEqual(45, m.number_of_best_spots)

  def test_part2_example2(self):
    m = Maze(self.example2)
    self.assertEqual(64, m.number_of_best_spots)

  def test_part2_puzzle(self):
    m = Maze(self.read_puzzle_input(day=16))
    self.assertEqual(433, m.number_of_best_spots)


if __name__ == '__main__':
  unittest.main()
