import unittest
from tests.aoc_harness import AocHarness
from src.day01 import parse, distances, total_distance, similarities, similarity_score


class TestsDay01(AocHarness):

  def setUp(self):
    self.example_input = '''
    3   4
    4   3
    2   5
    1   3
    3   9
    3   3
    '''

  def test_part1_example(self):
    self.assertEqual([(3, 4), (4, 3), (2, 5), (1, 3), (3, 9), (3, 3)], parse(self.example_input))
    self.assertEqual([2, 1, 0, 1, 2, 5], distances(self.example_input))
    self.assertEqual(11, total_distance(self.example_input))

  def test_part1_puzzle(self):
    input = self.read_puzzle_input(day=1)
    self.assertEqual(2264607, total_distance(input))

  def test_part2_example(self):
    self.assertEqual([9, 4, 0, 0, 9, 9], similarities(self.example_input))
    self.assertEqual(31, similarity_score(self.example_input))

  def test_part2_puzzle(self):
    input = self.read_puzzle_input(day=1)
    self.assertEqual(19457120, similarity_score(input))


if __name__ == '__main__':
  unittest.main()
