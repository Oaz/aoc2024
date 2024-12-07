import unittest
from tests.aoc_harness import AocHarness
from src.day07 import *


class TestsDay07(AocHarness):

  def setUp(self):
    self.example = Equations('''
190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20
      ''')

  def test_example_parsing(self):
    self.assertEqual(9, len(self.example))
    self.assertEqual(190, self.example[0].result)
    self.assertEqual([10, 19], self.example[0].operands)
    self.assertEqual(161011, self.example[5].result)
    self.assertEqual([16, 10, 13], self.example[5].operands)

  def test_part1_example(self):
    self.assertTrue(self.example[0].is_solved_using(add, mul))
    self.assertTrue(self.example[1].is_solved_using(add, mul))
    self.assertFalse(self.example[2].is_solved_using(add, mul))
    self.assertFalse(self.example[3].is_solved_using(add, mul))
    self.assertFalse(self.example[4].is_solved_using(add, mul))
    self.assertFalse(self.example[5].is_solved_using(add, mul))
    self.assertFalse(self.example[6].is_solved_using(add, mul))
    self.assertFalse(self.example[7].is_solved_using(add, mul))
    self.assertTrue(self.example[8].is_solved_using(add, mul))
    self.assertEqual(3749, self.example.total_calibration_result_using(add, mul))

  def test_part1_puzzle(self):
    equations = Equations(self.read_puzzle_input(day=7))
    self.assertEqual(42283209483350, equations.total_calibration_result_using(add, mul))

  def test_part2_example(self):
    self.assertTrue(self.example[0].is_solved_using(add, mul, concat))
    self.assertTrue(self.example[1].is_solved_using(add, mul, concat))
    self.assertFalse(self.example[2].is_solved_using(add, mul, concat))
    self.assertTrue(self.example[3].is_solved_using(add, mul, concat))
    self.assertTrue(self.example[4].is_solved_using(add, mul, concat))
    self.assertFalse(self.example[5].is_solved_using(add, mul, concat))
    self.assertTrue(self.example[6].is_solved_using(add, mul, concat))
    self.assertFalse(self.example[7].is_solved_using(add, mul, concat))
    self.assertTrue(self.example[8].is_solved_using(add, mul, concat))
    self.assertEqual(11387, self.example.total_calibration_result_using(add, mul, concat))

  def test_part2_puzzle(self):
    equations = Equations(self.read_puzzle_input(day=7))
    self.assertEqual(1026766857276279, equations.total_calibration_result_using(add, mul, concat))

  def timing_part2_puzzle(self):
    equations = Equations(self.read_puzzle_input(day=7))
    compute = lambda: equations.total_calibration_result_using(add, mul, concat)
    print(self.time('compute()', scope=locals()))


if __name__ == '__main__':
  unittest.main()
