import unittest
from tests.aoc_harness import AocHarness
from src.day17 import *


class TestsDay17(AocHarness):

  def setUp(self):
    self.example = Computer('''
Register A: 729
Register B: 0
Register C: 0

Program: 0,1,5,4,3,0
      ''')

  def test_instructions(self):
    self.assertEqual(Context.mk([225, 0, 15], 66), Computer.adv(0, Context.mk([225, 0, 15], 64)))
    self.assertEqual(Context.mk([112, 0, 16], 66), Computer.adv(1, Context.mk([225, 0, 16], 64)))
    self.assertEqual(Context.mk([56, 17, 0], 66), Computer.adv(2, Context.mk([225, 17, 0], 64)))
    self.assertEqual(Context.mk([28, 18, 0], 66), Computer.adv(3, Context.mk([225, 18, 0], 64)))
    self.assertEqual(Context.mk([0, 19, 20], 66), Computer.adv(4, Context.mk([225, 19, 20], 64)))
    self.assertEqual(Context.mk([112, 1, 0], 66), Computer.adv(5, Context.mk([225, 1, 0], 64)))
    self.assertEqual(Context.mk([4, 0, 2], 66), Computer.adv(6, Context.mk([16, 0, 2], 64)))

    self.assertEqual(Context.mk([17, 12, 18], 66), Computer.bxl(9, Context.mk([17, 5, 18], 64)))

    self.assertEqual(Context.mk([15, 3, 16], 66), Computer.bst(3, Context.mk([15, 3, 16], 64)))
    self.assertEqual(Context.mk([17, 5, 18], 66), Computer.bst(5, Context.mk([17, 221, 18], 64)))
    self.assertEqual(Context.mk([17, 6, 18], 66), Computer.bst(5, Context.mk([17, 222, 18], 64)))
    self.assertEqual(Context.mk([222, 6, 18], 66), Computer.bst(4, Context.mk([222, 17, 18], 64)))

    self.assertEqual(Context.mk([0, 17, 18], 66), Computer.jnz(28, Context.mk([0, 17, 18], 64)))
    self.assertEqual(Context.mk([16, 17, 18], 28), Computer.jnz(28, Context.mk([16, 17, 18], 64)))

    self.assertEqual(Context.mk([17, 12, 9], 66), Computer.bxc(42, Context.mk([17, 5, 9], 64)))

    self.assertEqual(Context.mk([15, 16, 17], 66, [42, 2]), Computer.out(2, Context.mk([15, 16, 17], 64, [42])))
    self.assertEqual(Context.mk([15, 16, 17], 66, [42, 3]), Computer.out(3, Context.mk([15, 16, 17], 64, [42])))
    self.assertEqual(Context.mk([15, 16, 17], 66, [45, 7]), Computer.out(4, Context.mk([15, 16, 17], 64, [45])))
    self.assertEqual(Context.mk([15, 16, 17], 66, [1, 2, 0]), Computer.out(5, Context.mk([15, 16, 17], 64, [1, 2])))

    self.assertEqual(Context.mk([225, 28, 0], 66), Computer.bdv(3, Context.mk([225, 18, 0], 64)))
    self.assertEqual(Context.mk([32, 4, 20], 66), Computer.bdv(5, Context.mk([32, 3, 20], 64)))

    self.assertEqual(Context.mk([225, 18, 28], 66), Computer.cdv(3, Context.mk([225, 18, 0], 64)))
    self.assertEqual(Context.mk([32, 3, 4], 66), Computer.cdv(5, Context.mk([32, 3, 20], 64)))

  def test_part1_example(self):
    self.assertEqual(729, self.example.start.a)
    self.assertEqual(0, self.example.start.b)
    self.assertEqual(0, self.example.start.c)
    self.assertEqual([
      (Computer.adv, 1),
      (Computer.out, 4),
      (Computer.jnz, 0)
    ], self.example.program)
    self.assertEqual([4, 6, 3, 5, 6, 3, 5, 2, 1, 0], self.example.run())

  def test_part1_puzzle(self):
    c = Computer(self.read_puzzle_input(day=17))
    self.assertEqual('6,5,7,4,5,7,3,1,0', Computer.format(c.run()))

  def test_part2_example(self):
    c = Computer('''
  Register A: 117440
  Register B: 0
  Register C: 0

  Program: 0,3,5,4,3,0
      ''')
    self.assertEqual('0,3,5,4,3,0', Computer.format(c.run()))

  def test_part2_puzzle(self):
    c = Computer(self.read_puzzle_input(day=17))
    self.assertEqual(59573664, c.find_initial_a_for([6, 5, 7, 4, 5, 7, 3, 1, 0]))
    self.assertEqual([6, 5, 7, 4, 5, 7, 3, 1, 0], c.run_with_a(59573664))
    a = c.find_initial_a_for_program_copy()
    self.assertEqual(c.code, c.run_with_a(a))
    self.assertEqual(105875099912602, a)

  def test_part2_other(self):
    c = Computer('''
  Register A: 0
  Register B: 0
  Register C: 0

  Program: 2,4,1,5,7,5,0,3,4,1,1,6,5,5,3,0
      ''')
    a = c.find_initial_a_for_program_copy()
    self.assertEqual(c.code, c.run_with_a(a))

if __name__ == '__main__':
  unittest.main()
