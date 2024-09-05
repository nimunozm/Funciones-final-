from typing import Optional 

class Node:
  def __init__(self, key, parent, left, right):
    self._key = key
    self._parent = parent
    self._left = left
    self._right = right

  def get_key(self) -> float:
    try:
      return self._key
    except:
      raise TypeError('No puedes pedir la key a un None .-.')

  def get_parent(self) -> Optional["Node"]:
    return self._parent

  def get_left(self) -> Optional["Node"]:
    return self._left

  def get_right(self) -> Optional["Node"]:
    return self._right

  def set_parent(self, parent):
    self._parent = parent

  def set_left(self, left):
    self._left = left

  def set_right(self, right):
    self._right = right

  def print_node(self):
    print("Parent: ",self._parent, " / Key: ", self._key, " / Left: ", self._left, " / Right: ", self._right)