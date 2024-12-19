import unittest
from tests.aoc_harness import AocHarness
from src.day18 import *


class TestsDay18(AocHarness):

  def setUp(self):
    self.example = MemorySpace(6, '''
5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0
      ''')

  def test_part1_example(self):
    self.assertEqual(49, len(self.example.graph.nodes))
    self.example.drop(12)
    self.assertEqual(37, len(self.example.graph.nodes))
    self.assertEqual(22, self.example.minimum_steps_to_exit)

  def test_part1_puzzle(self):
    ms = MemorySpace(70, self.read_puzzle_input(day=18))
    ms.drop(1024)
    self.assertEqual(232, ms.minimum_steps_to_exit)

  def test_part2_example(self):
    self.assertEqual((6, 1), self.example.coordinates_first_byte_that_prevent_exit)

  def test_part2_puzzle(self):
    ms = MemorySpace(70, self.read_puzzle_input(day=18))
    self.assertEqual((44, 64), ms.coordinates_first_byte_that_prevent_exit)


if __name__ == '__main__':
  unittest.main()
