import unittest
from tests.aoc_harness import AocHarness
from src.day11 import *


class TestsDay11(AocHarness):

  def test_part1_example(self):
    s = Stones('125 17')
    self.assertEqual(2, s.count_stones_after_blinks(0))  # 125 17
    self.assertEqual(3, s.count_stones_after_blinks(1))  # 253000 1 7
    self.assertEqual(4, s.count_stones_after_blinks(2))  # 253 0 2024 14168
    self.assertEqual(5, s.count_stones_after_blinks(3))  # 512072 1 20 24 28676032
    self.assertEqual(9, s.count_stones_after_blinks(4))  # 512 72 2024 2 0 2 4 2867 6032
    self.assertEqual(13, s.count_stones_after_blinks(5))  # 1036288 7 2 20 24 4048 1 4048 8096 28 67 60 32
    self.assertEqual(22, s.count_stones_after_blinks(6))
    # 2097446912 14168 4048 2 0 2 4 40 48 2024 40 48 80 96 2 8 6 7 6 0 3 2

    self.assertEqual(55312, s.count_stones_after_blinks(25))

  def test_part1_puzzle(self):
    s = Stones(self.read_puzzle_input(day=11))
    self.assertEqual(200446, s.count_stones_after_blinks(25))

  def test_part2_puzzle(self):
    s = Stones(self.read_puzzle_input(day=11))
    self.assertEqual(238317474993392, s.count_stones_after_blinks(75))


if __name__ == '__main__':
  unittest.main()
