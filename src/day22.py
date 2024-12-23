import re
from typing import List, Tuple
import numpy as np
from collections import defaultdict


def mix_and_prune(number: int, secret: int) -> int:
  return (number ^ secret) & 16777215


def next_secret(secret: int) -> int:
  new_secret = mix_and_prune(secret << 6, secret)
  new_secret = mix_and_prune(new_secret >> 5, new_secret)
  new_secret = mix_and_prune(new_secret << 11, new_secret)
  return new_secret


class Buyer:
  def __init__(self, initial_secret: int):
    self.secret = initial_secret

  def generate(self, steps: int) -> int:
    secret = self.secret
    for _ in range(steps):
      secret = next_secret(secret)
    return secret


class Market(List[Buyer]):
  def __init__(self, input_text: str):
    super().__init__([Buyer(int(secret)) for secret in re.findall(r'\d+', input_text)])

  def sum_of_secrets(self, steps: int) -> int:
    return sum(buyer.generate(steps) for buyer in self)


class Seller:
  def __init__(self, market: Market, steps: int = 2000):
    self.market = market
    prices = np.zeros((len(market), steps + 1), dtype=int)
    for i, buyer in enumerate(market):
      secret = buyer.secret
      prices[i, 0] = secret % 10
      for j in range(1, steps + 1):
        secret = next_secret(secret)
        prices[i, j] = secret % 10
    self.prices = prices
    self.deltas = np.diff(prices, axis=1)

  def price_at(self, buyer_index: int, variations: Tuple[int, int, int, int]) -> int | None:
    deltas = self.deltas[buyer_index, :]
    index = np.where(
      (deltas[:-3] == variations[0]) & (deltas[1:-2] == variations[1]) & (
        deltas[2:-1] == variations[2]) & (deltas[3:] == variations[3]))[0]
    return int(self.prices[buyer_index, index + 4][0]) if index.shape[0] else None

  def total_price_at(self, variations: Tuple[int, int, int, int]) -> int | None:
    prices = [self.price_at(i, variations) for i in range(len(self.market))]
    return sum(price for price in prices if price is not None)

  @property
  def best_total_price(self) -> int:
    sequence_found_for_buyer = set()
    variations_to_best_prices = defaultdict(int)
    for row_idx, row in enumerate(self.deltas):
      for col_idx in range(len(row) - 3):
        sequence = tuple(row[col_idx:col_idx + 4])
        if (row_idx, sequence) in sequence_found_for_buyer:
          continue
        sequence_found_for_buyer.add((row_idx, sequence))
        variations_to_best_prices[sequence] += self.prices[row_idx, col_idx + 4]
    return int(max(variations_to_best_prices.values()))
