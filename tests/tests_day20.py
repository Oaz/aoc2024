import unittest
from tests.aoc_harness import AocHarness
from src.day20 import *


class TestsDay20(AocHarness):

  def setUp(self):
    self.example = Race('''
###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############
      ''')

  def test_part1_example(self):
    self.assertEqual(84, self.example.boring_track_time)
    self.assertEqual([(1, 3), (1, 2), (1, 1), (2, 1), (3, 1)], self.example.track[0:5])
    self.assertEqual([(3, 9), (3, 8), (3, 7), (4, 7), (5, 7)], self.example.track[-5:])
    self.assertEqual({
      ((1, 3), (3, 3)): 4, ((3, 1), (5, 1)): 4, ((3, 11), (1, 11)): 4, ((5, 3), (7, 3)): 4,
      ((5, 13), (3, 13)): 4, ((7, 5), (9, 5)): 4, ((7, 11), (5, 11)): 4, ((9, 11), (7, 11)): 4,
      ((11, 1), (11, 3)): 4, ((11, 5), (11, 7)): 4, ((11, 9), (11, 11)): 4, ((11, 11), (9, 11)): 4,
      ((13, 3), (13, 5)): 4, ((13, 7), (13, 9)): 4,
      ((7, 4), (9, 4)): 6, ((9, 12), (7, 12)): 6,
      ((3, 11), (3, 9)): 8, ((7, 3), (9, 3)): 8, ((9, 3), (11, 3)): 8, ((9, 13), (7, 13)): 8,
      ((7, 2), (9, 2)): 10, ((9, 4), (11, 4)): 10,
      ((7, 1), (9, 1)): 12, ((9, 5), (11, 5)): 12, ((11, 9), (9, 9)): 12,
      ((9, 7), (11, 7)): 20,
      ((9, 7), (9, 9)): 36,
      ((8, 7), (8, 9)): 38,
      ((7, 7), (7, 9)): 40,
      ((7, 7), (5, 7)): 64,
    }, self.example.cheats(min_cheat_save=4, max_cheat_length=2))
    self.assertEqual({
      ((7, 1), (9, 1)): 12, ((9, 5), (11, 5)): 12, ((11, 9), (9, 9)): 12,
      ((9, 7), (11, 7)): 20,
      ((9, 7), (9, 9)): 36,
      ((8, 7), (8, 9)): 38,
      ((7, 7), (7, 9)): 40,
      ((7, 7), (5, 7)): 64,
    }, self.example.cheats(min_cheat_save=12, max_cheat_length=2))
    self.assertEqual(8, self.example.number_of_cheats(min_cheat_save=12, max_cheat_length=2))

  def test_part1_puzzle(self):
    race = Race(self.read_puzzle_input(day=20))
    self.assertEqual(9456, race.boring_track_time)
    self.assertEqual(1441, race.number_of_cheats(min_cheat_save=100, max_cheat_length=2))

  def test_part2_example(self):
    self.assertEqual(
      {((1, 3), (3, 7)): 76, ((1, 3), (4, 7)): 76, ((1, 3), (5, 7)): 76},
      self.example.cheats(min_cheat_save=76, max_cheat_length=20)
    )
    self.assertEqual(3, self.example.number_of_cheats(min_cheat_save=76, max_cheat_length=20))
    self.assertEqual(4 + 3, self.example.number_of_cheats(min_cheat_save=74, max_cheat_length=20))
    self.assertEqual(22 + 4 + 3, self.example.number_of_cheats(min_cheat_save=72, max_cheat_length=20))
    self.assertEqual(
      32 + 31 + 29 + 39 + 25 + 23 + 20 + 19 + 12 + 14 + 12 + 22 + 4 + 3,
      self.example.number_of_cheats(min_cheat_save=50, max_cheat_length=20)
    )

  def test_part2_puzzle(self):
    race = Race(self.read_puzzle_input(day=20))
    self.assertEqual(1021490, race.number_of_cheats(min_cheat_save=100, max_cheat_length=20))


if __name__ == '__main__':
  unittest.main()
