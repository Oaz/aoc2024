import unittest
from tests.aoc_harness import AocHarness
from src.day13 import *


class TestsDay13(AocHarness):

  def setUp(self):
    self.example_text = '''
Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279
      '''

  def test_machine_parsing(self):
      machine = ClawMachine('''
  Button A: X+94, Y+34
  Button B: X+22, Y+67
  Prize: X=8400, Y=5400
      ''')
      self.assertEqual(94, machine.delta_x_on_a)
      self.assertEqual(34, machine.delta_y_on_a)
      self.assertEqual(22, machine.delta_x_on_b)
      self.assertEqual(67, machine.delta_y_on_b)
      self.assertEqual(8400, machine.x_prize)
      self.assertEqual(5400, machine.y_prize)

  def test_example_parsing(self):
    arcade = Arcade(self.example_text)
    self.assertEqual(94, arcade[0].delta_x_on_a)
    self.assertEqual(26, arcade[1].delta_x_on_a)
    self.assertEqual(7870, arcade[2].x_prize)
    self.assertEqual(10279, arcade[3].y_prize)

  def test_part1_example(self):
    arcade = Arcade(self.example_text)
    self.assertTrue(arcade[0].has_solution)
    self.assertEqual(280, arcade[0].tokens_to_win)
    self.assertFalse(arcade[1].has_solution)
    self.assertTrue(arcade[2].has_solution)
    self.assertEqual(200, arcade[2].tokens_to_win)
    self.assertFalse(arcade[3].has_solution)
    self.assertEqual(480, arcade.tokens_to_win_all)

  def test_part1_puzzle(self):
    arcade = Arcade(self.read_puzzle_input(day=13))
    self.assertEqual(29598, arcade.tokens_to_win_all)

  def test_part2_example(self):
    arcade = Arcade(self.example_text, with_correction=True)
    self.assertFalse(arcade[0].has_solution)
    self.assertTrue(arcade[1].has_solution)
    self.assertFalse(arcade[2].has_solution)
    self.assertTrue(arcade[3].has_solution)
    self.assertGreater(arcade.tokens_to_win_all, 1000000)

  def test_part2_puzzle(self):
    arcade = Arcade(self.read_puzzle_input(day=13), with_correction=True)
    self.assertEqual(93217456941970, arcade.tokens_to_win_all)


if __name__ == '__main__':
  unittest.main()
