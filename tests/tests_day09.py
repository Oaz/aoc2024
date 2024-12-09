import unittest
from tests.aoc_harness import AocHarness
from src.day09 import *


class TestsDay08(AocHarness):

  def setUp(self):
    self.example = DiskMap('2333133121414131402')
    self.small_example = DiskMap('12345')

  def test_parsing(self):
    self.assertEqual([1, 2, 3, 4, 5], self.small_example.spaces)

  def test_sum_consecutive_ints(self):
    self.assertEqual(1 + 2, sum_consecutive_ints(1, 2))
    self.assertEqual(4 + 5 + 6, sum_consecutive_ints(4, 3))
    self.assertEqual(12 + 13 + 14 + 15 + 16, sum_consecutive_ints(12, 5))

  def test_part1_small_example(self):
    ml = MoveLeft(self.small_example)
    self.assertEqual([1, 6], ml.free_indexes)
    self.assertEqual({1: 2, 6: 4}, ml.free_sizes)
    self.assertEqual({0: (1, 0), 3: (3, 1), 10: (5, 2)}, ml.used)
    self.assertEqual([0, 3, 10], ml.to_move)
    ml.step()
    self.assertEqual([6], ml.free_indexes)
    self.assertEqual({6: 4}, ml.free_sizes)
    self.assertEqual({0: (1, 0), 1: (2, 2), 3: (3, 1), 10: (3, 2)}, ml.used)
    self.assertEqual([0, 3, 10], ml.to_move)
    ml.step()
    self.assertEqual([9], ml.free_indexes)
    self.assertEqual({9: 1}, ml.free_sizes)
    self.assertEqual({0: (1, 0), 1: (2, 2), 3: (3, 1), 6: (3, 2)}, ml.used)
    self.assertEqual([0, 3], ml.to_move)
    self.assertEqual(60, ml.checksum)
    self.assertEqual(60, self.small_example.checksum_move_left)

  def test_part1_example(self):
    ml = MoveLeft(self.example)
    self.assertEqual([2, 8, 12, 18, 21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({2: 3, 8: 3, 12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4),
                      22: (4, 5), 27: (4, 6), 32: (3, 7), 36: (4, 8), 40: (2, 9)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32, 36, 40], ml.to_move)
    ml.step()
    self.assertEqual([4, 8, 12, 18, 21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({4: 1, 8: 3, 12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4),
                      22: (4, 5), 27: (4, 6), 32: (3, 7), 36: (4, 8)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32, 36], ml.to_move)
    ml.step()
    self.assertEqual([8, 12, 18, 21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({8: 3, 12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4),
                      22: (4, 5), 27: (4, 6), 32: (3, 7), 36: (3, 8)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32, 36], ml.to_move)
    ml.step()
    self.assertEqual([12, 18, 21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({12: 3, 18: 1, 21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 8: (3, 8), 11: (1, 2), 15: (3, 3), 19: (2, 4),
                      22: (4, 5), 27: (4, 6), 32: (3, 7)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32], ml.to_move)
    ml.step()
    self.assertEqual([18, 21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({18: 1, 21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 8: (3, 8), 11: (1, 2), 12: (3, 7), 15: (3, 3),
                      19: (2, 4), 22: (4, 5), 27: (4, 6)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27], ml.to_move)
    ml.step()
    self.assertEqual([21, 26, 31, 35], ml.free_indexes)
    self.assertEqual({21: 1, 26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 8: (3, 8), 11: (1, 2), 12: (3, 7), 15: (3, 3),
                      18: (1, 6), 19: (2, 4), 22: (4, 5), 27: (3, 6)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27], ml.to_move)
    ml.step()
    self.assertEqual([26, 31, 35], ml.free_indexes)
    self.assertEqual({26: 1, 31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 8: (3, 8), 11: (1, 2), 12: (3, 7), 15: (3, 3),
                      18: (1, 6), 19: (2, 4), 21: (1, 6), 22: (4, 5), 27: (2, 6)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27], ml.to_move)
    ml.step()
    self.assertEqual([31, 35], ml.free_indexes)
    self.assertEqual({31: 1, 35: 1}, ml.free_sizes)
    self.assertEqual({0: (2, 0), 2: (2, 9), 4: (1, 8), 5: (3, 1), 8: (3, 8), 11: (1, 2), 12: (3, 7), 15: (3, 3),
                      18: (1, 6), 19: (2, 4), 21: (1, 6), 22: (4, 5), 26: (1, 6), 27: (1, 6)}, ml.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27], ml.to_move)
    ml.step()
    self.assertTrue(ml.is_complete)
    self.assertEqual(1928, ml.checksum)
    self.assertEqual(1928, self.example.checksum_move_left)

  def test_part1_puzzle(self):
    disk_map = DiskMap(self.read_puzzle_input(day=9))
    self.assertEqual(6367087064415, disk_map.checksum_move_left)

  def test_part2_example(self):
    nf = NoFragment(self.example)
    self.assertEqual({3: [2, 8, 12], 1: [18, 21, 26, 31, 35]}, nf.free)
    self.assertEqual(
      {0: (2, 0), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4), 22: (4, 5), 27: (4, 6), 32: (3, 7), 36: (4, 8),
       40: (2, 9)}, nf.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32, 36, 40], nf.to_move)
    nf.step()  # move 99
    self.assertEqual({3: [8, 12], 1: [4, 18, 21, 26, 31, 35]}, nf.free)
    self.assertEqual(
      {0: (2, 0), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4), 22: (4, 5), 27: (4, 6), 32: (3, 7), 36: (4, 8),
       2: (2, 9)}, nf.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32, 36], nf.to_move)
    nf.step()  # do not move 8888
    self.assertEqual([0, 5, 11, 15, 19, 22, 27, 32], nf.to_move)
    nf.step()  # move 777
    self.assertEqual({3: [12], 1: [4, 18, 21, 26, 31, 35]}, nf.free)
    self.assertEqual(
      {0: (2, 0), 5: (3, 1), 11: (1, 2), 15: (3, 3), 19: (2, 4), 22: (4, 5), 27: (4, 6), 8: (3, 7), 36: (4, 8),
       2: (2, 9)}, nf.used)
    self.assertEqual([0, 5, 11, 15, 19, 22, 27], nf.to_move)
    nf.step()  # do not move 6666
    self.assertEqual([0, 5, 11, 15, 19, 22], nf.to_move)
    nf.step()  # do not move 5555
    self.assertEqual([0, 5, 11, 15, 19], nf.to_move)
    nf.step()  # move 44
    self.assertEqual({1: [4, 14, 18, 21, 26, 31, 35]}, nf.free)
    self.assertEqual(
      {0: (2, 0), 5: (3, 1), 11: (1, 2), 15: (3, 3), 12: (2, 4), 22: (4, 5), 27: (4, 6), 8: (3, 7), 36: (4, 8),
       2: (2, 9)}, nf.used)
    self.assertEqual([0, 5, 11, 15], nf.to_move)
    nf.step()  # do not move 333
    self.assertEqual([0, 5, 11], nf.to_move)
    nf.step()  # move 2
    self.assertEqual({1: [14, 18, 21, 26, 31, 35]}, nf.free)
    self.assertEqual(
      {0: (2, 0), 5: (3, 1), 4: (1, 2), 15: (3, 3), 12: (2, 4), 22: (4, 5), 27: (4, 6), 8: (3, 7), 36: (4, 8),
       2: (2, 9)}, nf.used)
    self.assertEqual([0, 5], nf.to_move)
    nf.step()  # do not move 111
    self.assertEqual([0], nf.to_move)
    nf.step()  # do not move 00
    self.assertEqual([], nf.to_move)
    self.assertEqual(2858, nf.checksum)
    self.assertEqual(2858, self.example.checksum_no_fragmentation)

  def test_part2_puzzle(self):
    disk_map = DiskMap(self.read_puzzle_input(day=9))
    self.assertEqual(6390781891880, disk_map.checksum_no_fragmentation)


if __name__ == '__main__':
  unittest.main()
