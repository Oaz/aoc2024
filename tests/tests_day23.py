import unittest
from tests.aoc_harness import AocHarness
from src.day23 import *


class TestsDay23(AocHarness):

  def setUp(self):
    self.example = LanParty('''
kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
      ''')

  def test_part1_example(self):
    self.assertEqual([
      ['aq', 'cg', 'yn'],
      ['aq', 'vc', 'wq'],
      ['co', 'de', 'ka'],
      ['co', 'de', 'ta'],
      ['co', 'ka', 'ta'],
      ['de', 'ka', 'ta'],
      ['kh', 'qp', 'ub'],
      ['qp', 'td', 'wh'],
      ['tb', 'vc', 'wq'],
      ['tc', 'td', 'wh'],
      ['td', 'wh', 'yn'],
      ['ub', 'vc', 'wq']
    ], sorted([sorted(circuit) for circuit in self.example.sets_of_three_connected_computers]))
    self.assertEqual(7, self.example.number_of_three_connected_computers_sets_where_one_is_starting_with_letter_t)

  def test_part1_puzzle(self):
    lp = LanParty(self.read_puzzle_input(day=23))
    self.assertEqual(1098, lp.number_of_three_connected_computers_sets_where_one_is_starting_with_letter_t)

  def test_part2_example(self):
    self.assertEqual('co,de,ka,ta', self.example.password)

  def test_part2_puzzle(self):
    lp = LanParty(self.read_puzzle_input(day=23))
    self.assertEqual('ar,ep,ih,ju,jx,le,ol,pk,pm,pp,xf,yu,zg', lp.password)


if __name__ == '__main__':
  unittest.main()
