import unittest
from tests.aoc_harness import AocHarness
from src.day15 import *


class TestsDay15(AocHarness):

  def setUp(self):
    self.example = Warehouse('''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
    ''')

  def test_example_parsing(self):
    self.assertEqual(2 + 2j, self.example.robot)
    self.assertEqual({(3 + 1j), (5 + 1j), (4 + 2j), (4 + 3j), (4 + 4j), (4 + 5j)},
                     {box.base for box in self.example.boxes})
    self.assertEqual([-1, -1j, -1j, 1, 1, 1, 1j, 1j, -1, 1j, 1, 1, 1j, -1, -1], self.example.movements)

  def test_part1_example(self):
    self.example.move()
    self.assertEqual('''
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.example.move()
    self.assertEqual('''
########
#.@O.O.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#..@OO.#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#...@OO#
##..O..#
#...O..#
#.#.O..#
#...O..#
#......#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.example.move()
    self.assertEqual('''
########
#....OO#
##..@..#
#...O..#
#.#.O..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.@...#
#...O..#
#.#.O..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.....#
#..@O..#
#.#.O..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.....#
#...@O.#
#.#.O..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.....#
#....@O#
#.#.O..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.....#
#.....O#
#.#.O@.#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.example.move()
    self.example.move()
    self.assertEqual('''
########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########
    '''.strip(), str(self.example))
    self.assertEqual(2028, self.example.gps_sum)

  def test_part1_bigger_example(self):
    w = Warehouse('''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    ''')
    w.move_all()
    self.assertEqual('''
##########
#.O.O.OOO#
#........#
#OO......#
#OO@.....#
#O#.....O#
#O.....OO#
#O.....OO#
#OO....OO#
##########
    '''.strip(), str(w))
    self.assertEqual(10092, w.gps_sum)

  def test_part1_puzzle(self):
    w = Warehouse(self.read_puzzle_input(day=15))
    w.move_all()
    self.assertEqual(1448589, w.gps_sum)

  def test_part2_example(self):
    w = Warehouse('''
#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

<vv<<^^<<^^
    ''', 2)
    self.assertEqual('''
##############
##......##..##
##..........##
##....[][]@.##
##....[]....##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##..........##
##...[][]@..##
##....[]....##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##..........##
##...[][]...##
##....[].@..##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.......@..##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##......@...##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##..........##
##...[][]...##
##....[]....##
##.....@....##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##...[][]...##
##....[]....##
##.....@....##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##...[][]...##
##....[]....##
##....@.....##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##...[][]...##
##....[]....##
##...@......##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##......##..##
##...[][]...##
##...@[]....##
##..........##
##..........##
##############
    '''.strip(), str(w))
    w.move()
    self.assertEqual('''
##############
##...[].##..##
##...@.[]...##
##....[]....##
##..........##
##..........##
##############
    '''.strip(), str(w))

  def test_part2_bigger_example(self):
    w = Warehouse('''
##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^
    ''', 2)
    w.move_all()
    self.assertEqual('''
####################
##[].......[].[][]##
##[]...........[].##
##[]........[][][]##
##[]......[]....[]##
##..##......[]....##
##..[]............##
##..@......[].[][]##
##......[][]..[]..##
####################
    '''.strip(), str(w))
    self.assertEqual(9021, w.gps_sum)

  def test_part2_puzzle(self):
    w = Warehouse(self.read_puzzle_input(day=15), 2)
    w.move_all()
    self.assertEqual(1472235, w.gps_sum)


if __name__ == '__main__':
  unittest.main()
