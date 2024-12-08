import os
import unittest
import requests
import timeit


class AocHarness(unittest.TestCase):

  def __init__(self, *args, **kwargs):
    super(AocHarness, self).__init__(*args, **kwargs)
    session = os.environ.get('AOC_SESSION')
    self.cookies = {
      'session': session
    }
    year = os.environ.get('AOC_YEAR')
    self.base_url = f'https://adventofcode.com/{year}/day'

  def read_puzzle_input(self, day):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    filename = os.path.join(current_dir, f'../inputs/day{day:02d}.txt')
    if os.path.isfile(filename):
      return self.read_text_file_full_content(filename)
    response = requests.get(
      url=f'{self.base_url}/{day}/input',
      cookies=self.cookies
    )
    if response.status_code == 200:
      return self.write_text_file_full_content(filename, response.text)
    raise Exception(response.text)

  @staticmethod
  def read_text_file_full_content(filename):
    with open(filename, 'r') as file:
      return file.read()

  @staticmethod
  def write_text_file_full_content(filename, content):
    with open(filename, 'w') as file:
      file.write(content)
    return content

  @staticmethod
  def time(statement: str, scope, iterations: int = 100):
    return timeit.timeit(stmt=statement, globals=scope, number=iterations) / iterations
