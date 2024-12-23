import unittest
from tests.aoc_harness import AocHarness
from src.day22 import *


class TestsDay22(AocHarness):

  def test_part1_example(self):
    b = Buyer(123)
    self.assertEqual(15887950, b.generate(1))
    self.assertEqual(16495136, b.generate(2))
    self.assertEqual(7753432, b.generate(9))
    self.assertEqual(5908254, b.generate(10))
    market = Market('''
1
10
100
2024
      ''')
    self.assertEqual(8685429, market[0].generate(2000))
    self.assertEqual(4700978, market[1].generate(2000))
    self.assertEqual(15273692, market[2].generate(2000))
    self.assertEqual(8667524, market[3].generate(2000))
    self.assertEqual(37327623, market.sum_of_secrets(2000))

  def test_part1_puzzle(self):
    market = Market(self.read_puzzle_input(day=22))
    self.assertEqual(20401393616, market.sum_of_secrets(2000))

  def test_part2_example(self):
    market = Market('''
1
2
3
2024
          ''')
    seller = Seller(market)
    sequence = (-2, 1, -1, 3)
    self.assertEqual(7, seller.price_at(0, sequence))
    self.assertEqual(7, seller.price_at(1, sequence))
    self.assertEqual(None, seller.price_at(2, sequence))
    self.assertEqual(9, seller.price_at(3, sequence))
    self.assertEqual(23, seller.total_price_at(sequence))
    self.assertEqual(23, seller.best_total_price)

  def test_part2_puzzle(self):
    market = Market(self.read_puzzle_input(day=22))
    seller = Seller(market)
    self.assertEqual(2272, seller.best_total_price)


if __name__ == '__main__':
  unittest.main()
