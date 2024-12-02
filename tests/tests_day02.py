import unittest
from tests.aoc_harness import AocHarness
from src.day02 import ReportList


class TestsDay02(AocHarness):

  def setUp(self):
    self.example_input = '''
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
    '''

  def test_part1_example(self):
    reports = ReportList(self.example_input)
    self.assertTrue(reports[0].is_safe)
    self.assertFalse(reports[1].is_safe)
    self.assertFalse(reports[2].is_safe)
    self.assertFalse(reports[3].is_safe)
    self.assertFalse(reports[4].is_safe)
    self.assertTrue(reports[5].is_safe)
    self.assertEqual(2, reports.count_safe)

  def test_part1_puzzle(self):
    reports = ReportList(self.read_puzzle_input(day=2))
    self.assertEqual(516, reports.count_safe)

  def test_part2_example(self):
    reports = ReportList(self.example_input)
    self.assertTrue(reports[0].is_dampener_safe)
    self.assertFalse(reports[1].is_dampener_safe)
    self.assertFalse(reports[2].is_dampener_safe)
    self.assertTrue(reports[3].is_dampener_safe)
    self.assertTrue(reports[4].is_dampener_safe)
    self.assertTrue(reports[5].is_dampener_safe)
    self.assertEqual(4, reports.count_dampener_safe)

  def test_part2_puzzle(self):
    reports = ReportList(self.read_puzzle_input(day=2))
    self.assertEqual(561, reports.count_dampener_safe)


if __name__ == '__main__':
  unittest.main()
