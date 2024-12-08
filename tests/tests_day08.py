import unittest
from tests.aoc_harness import AocHarness
from src.day08 import *


class TestsDay08(AocHarness):

  def setUp(self):
    self.example = City('''
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
      ''')

  def test_example_parsing(self):
    self.assertEqual(2, len(self.example.frequencies))
    self.assertEqual(4, len(self.example.frequencies['0'].antennas))
    self.assertEqual(3, len(self.example.frequencies['A'].antennas))
    self.assertEqual({6+5j, 8+8j, 9+9j}, self.example.frequencies['A'].antennas)

  def test_part1_example(self):
    self.assertEqual({4+2j, 10+11j}, antinodes(6 + 5j, 8 + 8j, 12 + 12j))
    self.assertEqual({3+1j}, antinodes(6 + 5j, 9 + 9j, 12 + 12j))
    self.assertEqual({7+7j, 10+10j}, antinodes(8 + 8j, 9 + 9j, 12 + 12j))
    self.assertEqual({4+2j, 10+11j, 3+1j, 7+7j, 10+10j}, self.example.frequencies['A'].gather(antinodes))
    self.assertEqual(14, self.example.count_unique_locations(antinodes))

  def test_part1_puzzle(self):
    city = City(self.read_puzzle_input(day=8))
    self.assertEqual(327, city.count_unique_locations(antinodes))

  def test_part2_example(self):
    self.assertEqual([0+0j, 3+1j, 6+2j, 9+3j], list(harmonics_range(0 + 0j, 3 + 1j, 10 + 10j)))
    self.assertEqual({0+0j, 3+1j, 6+2j, 9+3j}, harmonics(0 + 0j, 3 + 1j, 10 + 10j))
    self.assertEqual({0+0j, 1+2j, 2+4j, 3+6j, 4+8j}, harmonics(0 + 0j, 1 + 2j, 10 + 10j))
    self.assertEqual({1+1j, 3+3j, 5+5j, 7+7j}, harmonics(5 + 5j, 7 + 7j, 9 + 9j))
    self.assertEqual({0+0j, 1+1j, 2+2j, 3+3j, 4+4j, 5+5j}, harmonics(3 + 3j, 4 + 4j, 6 + 6j))
    self.assertEqual({
      4+2j, 6+5j, 8+8j, 10+11j,
      3+1j, 6+5j, 9+9j,
      0+0j, 1+1j, 2+2j, 3+3j, 4+4j, 5+5j, 6+6j, 7+7j, 8+8j, 9+9j, 10+10j, 11+11j
    }, self.example.frequencies['A'].gather(harmonics))
    self.assertEqual({10+2j, 7+3j, 4+4j, 1+5j}, harmonics(7 + 3j, 4 + 4j, 12 + 12j))
    self.assertEqual({8+1j, 7+3j, 6+5j, 5+7j, 4+9j, 3+11j}, harmonics(7 + 3j, 8 + 1j, 12 + 12j))
    self.assertEqual({1+0j, 3+1j, 5+2j, 9+4j, 7+3j, 11+5j}, harmonics(7 + 3j, 5 + 2j, 12 + 12j))
    self.assertEqual({0+7j, 4+4j, 8+1j}, harmonics(4 + 4j, 8 + 1j, 12 + 12j))
    self.assertEqual({6+0j, 5+2j, 4+4j, 3+6j, 2+8j, 1+10j}, harmonics(4 + 4j, 5 + 2j, 12 + 12j))
    self.assertEqual({11+0j, 8+1j, 5+2j, 2+3j}, harmonics(8 + 1j, 5 + 2j, 12 + 12j))
    self.assertEqual(34, self.example.count_unique_locations(harmonics))

  def test_part2_puzzle(self):
    city = City(self.read_puzzle_input(day=8))
    self.assertEqual(1233, city.count_unique_locations(harmonics))


if __name__ == '__main__':
  unittest.main()
