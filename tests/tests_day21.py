import unittest
from tests.aoc_harness import AocHarness
from pprint import pprint
from src.day21 import *


class TestsDay21(AocHarness):

  def setUp(self):
    self.example = Codes('''
029A
980A
179A
456A
379A
        ''')

  def test_layouts(self):
    self.assertEqual({
      ('0', '2'): '^',
      ('0', 'A'): '>',
      ('1', '2'): '>',
      ('1', '4'): '^',
      ('2', '0'): 'v',
      ('2', '1'): '<',
      ('2', '3'): '>',
      ('2', '5'): '^',
      ('3', '2'): '<',
      ('3', '6'): '^',
      ('3', 'A'): 'v',
      ('4', '1'): 'v',
      ('4', '5'): '>',
      ('4', '7'): '^',
      ('5', '2'): 'v',
      ('5', '4'): '<',
      ('5', '6'): '>',
      ('5', '8'): '^',
      ('6', '3'): 'v',
      ('6', '5'): '<',
      ('6', '9'): '^',
      ('7', '4'): 'v',
      ('7', '8'): '>',
      ('8', '5'): 'v',
      ('8', '7'): '<',
      ('8', '9'): '>',
      ('9', '6'): 'v',
      ('9', '8'): '<',
      ('A', '0'): '<',
      ('A', '3'): '^'
    }, Keypad(numericPad).atomic_moves)
    self.assertEqual({
      ('<', 'v'): '>',
      ('>', 'A'): '^',
      ('>', 'v'): '<',
      ('A', '>'): 'v',
      ('A', '^'): '<',
      ('^', 'A'): '>',
      ('^', 'v'): 'v',
      ('v', '<'): '<',
      ('v', '>'): '>',
      ('v', '^'): '^'
    }, Keypad(directionalPad).atomic_moves)

  def test_exploration(self):
    dr = Robot.directional
    nr = Robot.numeric
    self.assertEqual(['<v<A', 'v<<A'], dr.all_from_to('A', '<'))
    self.assertEqual(['>^>A', '>>^A'], dr.all_from_to('<', 'A'))
    self.assertEqual(['vA'], dr.all_from_to('A', '>'))
    self.assertEqual(['^A'], dr.all_from_to('>', 'A'))
    self.assertEqual(['<A'], dr.all_from_to('A', '^'))
    self.assertEqual(['>A'], dr.all_from_to('^', 'A'))
    self.assertEqual(['<vA', 'v<A'], dr.all_from_to('A', 'v'))
    self.assertEqual(['^>A', '>^A'], dr.all_from_to('v', 'A'))
    self.assertEqual(['^^>A', '^>^A', '>^^A'], nr.all_from_to('2', '9'))
    self.assertEqual('<A', nr.best_from_to('A', '0'))
    self.assertEqual('^A', nr.best_from_to('0', '2'))
    self.assertEqual('^^>A', nr.best_from_to('2', '9'))
    self.assertEqual('vvvA', nr.best_from_to('9', 'A'))
    self.assertEqual(['<A^A^^>AvvvA', '<A^A^>^AvvvA', '<A^A>^^AvvvA'], nr.all_sequences('029A'))
    self.assertEqual('<A^A^^>AvvvA', nr.best_sequence('029A'))
    self.assertEqual('029A', nr.send('<A^A^^>AvvvA'))
    self.assertEqual('029A', nr.send(nr.best_sequence('029A')))
    self.assertEqual('v<<A>>^A<A>A<AAv>A^A<vAAA^>A', dr.best_sequence('<A^A^^>AvvvA'))
    self.assertEqual('<A^A^^>AvvvA', dr.send(dr.best_sequence('<A^A^^>AvvvA')))
    self.assertEqual('<A^A>^^AvvvA', dr.send(dr.best_sequence('<A^A>^^AvvvA')))
    self.assertEqual('<A^A^>^AvvvA', dr.send(dr.best_sequence('<A^A^>^AvvvA')))
    self.assertEqual('v<<A>>^A<A>AvA<^AA>A<vAAA>^A', dr.send(dr.best_sequence('v<<A>>^A<A>AvA<^AA>A<vAAA>^A')))
    self.assertEqual(
      '<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A',
      dr.send(dr.best_sequence('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'))
    )

  def test_part1_example(self):
    rc = RobotChain()

    self.assertEqual('029A', rc.send('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'))
    code1 = rc.sequence('029A')
    self.assertEqual('029A', rc.send(code1))
    self.assertEqual(len('<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'), len(code1))

    self.assertEqual('980A', rc.send('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A'))
    code2 = rc.sequence('980A')
    self.assertEqual('980A', rc.send(rc.sequence('980A')))
    self.assertEqual(len('<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A'), len(code2))

    self.assertEqual('179A', rc.send('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'))
    code3 = rc.sequence('179A')
    self.assertEqual('179A', rc.send(code3))
    self.assertEqual(len('<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'), len(code3))

    self.assertEqual('456A', rc.send('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'))
    code4 = rc.sequence('456A')
    self.assertEqual('456A', rc.send(code4))
    self.assertEqual(len('<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A'), len(code4))

    self.assertEqual('379A', rc.send('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'))
    code5 = rc.sequence('379A')
    self.assertEqual('379A', rc.send(code5))
    self.assertEqual(len('<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'), len(code5))

    self.assertEqual(126384, self.example.sum_of_complexities(number_of_directional_keypad_robots=2))

  def test_part1_puzzle(self):
    codes = Codes(self.read_puzzle_input(day=21))
    self.assertEqual(152942, codes.sum_of_complexities(number_of_directional_keypad_robots=2))

  def test_part2_example(self):
    self.assertEqual(154115708116294, self.example.sum_of_complexities(number_of_directional_keypad_robots=25))

  def test_part2_puzzle(self):
    codes = Codes(self.read_puzzle_input(day=21))
    self.assertEqual(189235298434780, codes.sum_of_complexities(number_of_directional_keypad_robots=25))


if __name__ == '__main__':
  unittest.main()
