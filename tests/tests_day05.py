import unittest
from tests.aoc_harness import AocHarness
from src.day05 import Printer


class TestsDay05(AocHarness):

  def setUp(self):
    self.example = Printer('''
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
      ''')

  def test_example_parsing(self):
    self.assertEqual(21, len(self.example.rules))
    self.assertEqual(47, self.example.rules[0][0])
    self.assertEqual(53, self.example.rules[0][1])
    self.assertEqual(6, len(self.example.updates))
    self.assertEqual([75, 29, 13], self.example.updates[2])

  def test_part1_example(self):
    self.assertTrue(self.example.updates[0].is_ordered)
    self.assertTrue(self.example.updates[1].is_ordered)
    self.assertTrue(self.example.updates[2].is_ordered)
    self.assertFalse(self.example.updates[3].is_ordered)
    self.assertFalse(self.example.updates[4].is_ordered)
    self.assertFalse(self.example.updates[5].is_ordered)
    self.assertEqual(61, self.example.updates[0].middle_page_number)
    self.assertEqual(143, self.example.sum_of_middle_page_number_in_ordered_updates)

  def test_part1_puzzle(self):
    printer = Printer(self.read_puzzle_input(day=5))
    self.assertEqual(5091, printer.sum_of_middle_page_number_in_ordered_updates)

  def test_part2_example(self):
    self.assertEqual(47, self.example.updates[3].middle_page_number)
    self.assertEqual(29, self.example.updates[4].middle_page_number)
    self.assertEqual(123, self.example.sum_of_middle_page_number_in_unordered_updates)

  def test_part2_puzzle(self):
    printer = Printer(self.read_puzzle_input(day=5))
    self.assertEqual(4681, printer.sum_of_middle_page_number_in_unordered_updates)


if __name__ == '__main__':
  unittest.main()
