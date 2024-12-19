import unittest
from tests.aoc_harness import AocHarness
from src.day19 import *


class TestsDay99(AocHarness):

  def setUp(self):
    self.example = Towels('''
r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb
      ''')

  def test_example_parsing(self):
    self.assertEqual(['r', 'wr', 'b', 'g', 'bwu', 'rb', 'gb', 'br'], self.example.patterns)
    self.assertEqual([
      'brwrr', 'bggr', 'gbbr', 'rrbgbr', 'ubwu', 'bwurrg', 'brgr', 'bbrgwb'], self.example.designs)

  def test_part1_example(self):
    self.assertEqual(True, self.example.is_design_possible('brwrr'))
    self.assertEqual(True, self.example.is_design_possible('bggr'))
    self.assertEqual(True, self.example.is_design_possible('gbbr'))
    self.assertEqual(True, self.example.is_design_possible('rrbgbr'))
    self.assertEqual(False, self.example.is_design_possible('ubwu'))
    self.assertEqual(True, self.example.is_design_possible('bwurrg'))
    self.assertEqual(True, self.example.is_design_possible('brgr'))
    self.assertEqual(False, self.example.is_design_possible('bbrgwb'))
    self.assertEqual(6, self.example.count_design_possible)

  def test_part1_puzzle(self):
    towels = Towels(self.read_puzzle_input(day=19))
    self.assertEqual(242, towels.count_design_possible)

  def test_part2_example(self):
    self.assertEqual(2, self.example.count_possible_arrangements('brwrr'))
    self.assertEqual(1, self.example.count_possible_arrangements('bggr'))
    self.assertEqual(4, self.example.count_possible_arrangements('gbbr'))
    self.assertEqual(6, self.example.count_possible_arrangements('rrbgbr'))
    self.assertEqual(0, self.example.count_possible_arrangements('ubwu'))
    self.assertEqual(1, self.example.count_possible_arrangements('bwurrg'))
    self.assertEqual(2, self.example.count_possible_arrangements('brgr'))
    self.assertEqual(0, self.example.count_possible_arrangements('bbrgwb'))
    self.assertEqual(16, self.example.count_all_possible_arrangements)

  def test_part2_puzzle(self):
    towels = Towels(self.read_puzzle_input(day=19))
    self.assertEqual(595975512785325, towels.count_all_possible_arrangements)


if __name__ == '__main__':
  unittest.main()
