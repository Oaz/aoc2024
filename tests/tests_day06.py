import unittest
from tests.aoc_harness import AocHarness
from src.day06 import Lab, Guard, LabHack


class TestsDay06(AocHarness):

  def setUp(self):
    self.example = Lab.parse('''
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
      ''')

  def test_example_parsing(self):
    self.assertEqual(10, self.example.width)
    self.assertEqual(10, self.example.height)
    self.assertFalse(self.example.is_obstacle(complex(0, 0)))
    self.assertTrue(self.example.is_obstacle(complex(4, 0)))
    self.assertEqual(complex(4, 6), self.example.start_position)

  def test_part1_example(self):
    guard = Guard(self.example)
    guard.move_until_obstacle()
    self.assertEqual(complex(4, 1), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(8, 1), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(8, 6), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(2, 6), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(2, 4), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(6, 4), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(6, 8), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(1, 8), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(1, 7), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(7, 7), guard.position)
    guard.move_until_obstacle()
    self.assertEqual(complex(7, 9), guard.position)
    self.assertEqual(41, guard.visited)

  def test_part1_example_oneshot(self):
    guard = Guard(self.example)
    guard.move_until_leaving()
    self.assertEqual(41, guard.visited)
    # print(guard)

  def test_part1_puzzle(self):
    lab = Lab.parse(self.read_puzzle_input(day=6))
    guard = Guard(lab)
    guard.move_until_leaving()
    self.assertEqual(4559, guard.visited)

  def test_part2_example(self):
    hack = LabHack(self.example)
    self.assertFalse(hack.is_loop(complex(0, 0)))
    self.assertFalse(hack.is_loop(complex(4, 2)))
    self.assertTrue(hack.is_loop(complex(3, 6)))
    self.assertTrue(hack.is_loop(complex(6, 7)))
    self.assertEqual(6, hack.count_efficient_obstructions)
    # print(hack)

  def test_part2_puzzle(self):
    lab = Lab.parse(self.read_puzzle_input(day=6))
    hack = LabHack(lab)
    self.assertEqual(1604, hack.count_efficient_obstructions)
    # print(hack)

if __name__ == '__main__':
  unittest.main()
