
class CustomSet(set):
  def _add_item(self, item):
    return item

  def _remove_item(self, item):
    return item

  def add(self, item):
    super().add(self._add_item(item))

  def update(self, *iterables):
    for iterable in iterables:
      super().update(self._add_item(item) for item in iterable)

  def remove(self, item):
    super().remove(self._remove_item(item))

  def discard(self, item):
    super().discard(self._remove_item(item))

  def pop(self):
    item = next(iter(self))
    super().remove(self._remove_item(item))
    return item

  def clear(self):
    while self:
      self.pop()
