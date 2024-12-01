from typing import List, Tuple


def parse(input_text: str) -> List[Tuple[int, int]]:
  return [
    (int(left), int(right)) for left, right in [
      row.split() for row in input_text.strip().splitlines()
    ]
  ]


def distances(input: str) -> List[int]:
  numbers = parse(input)
  left_sorted_numbers = sorted([left for left, _ in numbers])
  right_sorted_numbers = sorted([right for _, right in numbers])
  return [abs(left - right) for left, right in zip(left_sorted_numbers, right_sorted_numbers)]


def total_distance(input: str) -> int:
  return sum(distances(input))


def similarities(input: str) -> List[int]:
  numbers = parse(input)
  right_numbers = [right for _, right in numbers]
  return [left * right_numbers.count(left) for left, _ in numbers]


def similarity_score(input: str) -> int:
  return sum(similarities(input))
