import unittest
from tests.aoc_harness import AocHarness
from src.day04 import WordSearch


class TestsDay04(AocHarness):

  def setUp(self):
    self.example_input = WordSearch('''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
      ''')

  def test_part1_example(self):
    self.assertFalse(self.example_input.is_word_at((0, 0), (1, 0)))
    self.assertFalse(self.example_input.is_word_at((0, 9), (1, -1)))
    self.assertTrue(self.example_input.is_word_at((5, 0), (1, 0)))
    self.assertTrue(self.example_input.is_word_at((4, 1), (-1, 0)))
    self.assertTrue(self.example_input.is_word_at((9, 3), (-1, 1)))
    self.assertTrue(self.example_input.is_word_at((9, 9), (-1, -1)))
    self.assertTrue(self.example_input.is_word_at((6, 5), (-1, -1)))
    self.assertTrue(self.example_input.is_word_at((3, 9), (1, -1)))
    self.assertTrue(self.example_input.is_word_at((3, 9), (-1, -1)))
    self.assertFalse(self.example_input.is_word_at((0, 0), (-1, -1)))
    self.assertEqual(18, self.example_input.count_word)

  def test_part1_puzzle(self):
    word_search = WordSearch(self.read_puzzle_input(day=4))
    self.assertEqual(2532, word_search.count_word)

  def test_part2_example(self):
    self.assertFalse(self.example_input.is_cross_at((0, 0)))
    self.assertFalse(self.example_input.is_cross_at((0, 2)))
    self.assertTrue(self.example_input.is_cross_at((2, 1)))
    self.assertTrue(self.example_input.is_cross_at((4, 3)))
    self.assertTrue(self.example_input.is_cross_at((5, 7)))
    self.assertFalse(self.example_input.is_cross_at((5, 6)))
    self.assertEqual(9, self.example_input.count_cross)

  def test_part2_puzzle(self):
    word_search = WordSearch(self.read_puzzle_input(day=4))
    self.assertEqual(1941, word_search.count_cross)


if __name__ == '__main__':
  unittest.main()
