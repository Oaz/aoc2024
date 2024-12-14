import unittest
from tests.aoc_harness import AocHarness
from src.day14 import *


class TestsDay14(AocHarness):

  def setUp(self):
    self.example = Area(11 + 7j, '''
p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3
      ''')

  def test_example_parsing(self):
    self.assertEqual(0 + 4j, self.example[0].p)
    self.assertEqual(3 - 3j, self.example[0].v)

  def test_part1_example(self):
    self.assertEqual(2 + 4j, self.example[10].move(0))
    self.assertEqual(4 + 1j, self.example[10].move(1))
    self.assertEqual(6 + 5j, self.example[10].move(2))
    self.assertEqual(8 + 2j, self.example[10].move(3))
    self.assertEqual(12, self.example.safety_factor)

  def test_part1_puzzle(self):
    area = Area(101 + 103j, self.read_puzzle_input(day=14))
    self.assertEqual(228421332, area.safety_factor)

  def test_part2_puzzle(self):
    area = Area(101 + 103j, self.read_puzzle_input(day=14))
    seconds = area.fewest_seconds_to_easter_egg
    self.assertEqual(7790, seconds)
    area.print_image(seconds)


if __name__ == '__main__':
  unittest.main()
