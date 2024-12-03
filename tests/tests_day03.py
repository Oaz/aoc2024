import unittest
from tests.aoc_harness import AocHarness
from src.day03 import Computer


class TestsDay03(AocHarness):

  def test_part1_example(self):
    computer = Computer('''
    xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
        ''')
    self.assertEqual([(2, 4), (5, 5), (11, 8), (8, 5)], computer.multiplications)
    self.assertEqual(161, computer.result)

  def test_part1_puzzle(self):
    computer = Computer(self.read_puzzle_input(day=3))
    self.assertEqual(166905464, computer.result)

  def test_part2_example(self):
    computer = Computer('''
    xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
        ''', with_do_dont=True)
    self.assertEqual([(2, 4), (8, 5)], computer.multiplications)
    self.assertEqual(48, computer.result)

  def test_part2_puzzle(self):
    computer = Computer(self.read_puzzle_input(day=3), with_do_dont=True)
    self.assertEqual(72948684, computer.result)


if __name__ == '__main__':
  unittest.main()
