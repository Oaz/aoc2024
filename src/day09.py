def sum_consecutive_ints(start: int, length: int):
  return length * (2 * start + length - 1) // 2


class DiskMap:
  def __init__(self, input_text: str):
    self.spaces = [int(n) for n in input_text.strip()]

  @property
  def checksum_move_left(self) -> int:
    ml = MoveLeft(self)
    while not ml.is_complete:
      ml.step()
    return ml.checksum

  @property
  def checksum_no_fragmentation(self) -> int:
    nf = NoFragment(self)
    while not nf.is_complete:
      nf.step()
    return nf.checksum


class Compactor:
  def __init__(self, disk_map: DiskMap):
    self.used = {}
    self.to_move = []
    self.is_complete = False
    used = False
    n = 0
    i = 0
    for size in disk_map.spaces:
      used = not used
      if used:
        self.used[i] = (size, n)
        self.to_move.append(i)
        n += 1
      else:
        self.add_free_space(size, i)
      i += size

  def add_free_space(self, size: int, index: int):
    pass

  @property
  def checksum(self) -> int:
    return sum(n * sum_consecutive_ints(start, size) for start, (size, n) in self.used.items())


class MoveLeft(Compactor):
  def __init__(self, disk_map: DiskMap):
    self.free_indexes = []
    self.free_sizes = {}
    super().__init__(disk_map)

  def add_free_space(self, size: int, index: int):
    if size > 0:
      self.free_indexes.append(index)
      self.free_sizes[index] = size

  def step(self):
    i_last = self.to_move.pop()
    i_first_free = self.free_indexes.pop(0)
    if i_first_free > i_last:
      self.is_complete = True
      return self
    last_file_size, last_file_num = self.used.pop(i_last)
    free_size = self.free_sizes.pop(i_first_free)
    if free_size < last_file_size:
      self.used[i_first_free] = (free_size, last_file_num)
      self.used[i_last] = (last_file_size - free_size, last_file_num)
      self.to_move.append(i_last)
    elif free_size == last_file_size:
      self.used[i_first_free] = (free_size, last_file_num)
    else:
      self.used[i_first_free] = (last_file_size, last_file_num)
      new_free_index = i_first_free + last_file_size
      self.free_sizes[new_free_index] = free_size - last_file_size
      self.free_indexes.append(new_free_index)
      self.free_indexes.sort()
    return self


class NoFragment(Compactor):
  def __init__(self, disk_map: DiskMap):
    self.free = {}
    super().__init__(disk_map)

  def add_free_space(self, size: int, index: int):
    if size == 0:
      return
    if size not in self.free:
      self.free[size] = []
    self.free[size].append(index)
    self.free[size].sort()

  def step(self):
    if len(self.to_move) == 0:
      self.is_complete = True
      return self
    i_last = self.to_move.pop()
    last_file = self.used[i_last]
    last_file_size, _ = last_file

    leftmost_free_space_candidates = {indexes[0]: size for size, indexes in self.free.items() if size >= last_file_size}
    if len(leftmost_free_space_candidates) == 0:
      return self
    free_size = leftmost_free_space_candidates[min(leftmost_free_space_candidates.keys())]
    available_spaces = self.free[free_size]
    i_free_space_for_last_file = available_spaces.pop(0)
    if len(available_spaces) == 0:
      del self.free[free_size]
    if i_free_space_for_last_file > i_last:
      return self
    self.used.pop(i_last)

    self.add_free_space(free_size - last_file_size, i_free_space_for_last_file + last_file_size)
    self.used[i_free_space_for_last_file] = last_file
    return self
