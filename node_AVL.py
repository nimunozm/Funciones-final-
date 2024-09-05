from typing import Optional 

class Node:
  def __init__(self, key, parent, left, right):
    self._key = key
    self._parent = parent
    self._left = left
    self._right = right
    self._height = 1

  def get_key(self) -> float:
    return self._key

  def get_parent(self) -> Optional["Node"]:
    return self._parent

  def get_left(self) -> Optional["Node"]:
    return self._left

  def get_right(self) -> Optional["Node"]:
    return self._right
  
  def get_height(self) -> int:
    return self._height

  def set_parent(self, parent):
    self._parent = parent

  def set_left(self, left):
    self._left = left

  def set_right(self, right):
    self._right = right    

  def set_n_height(self,height:int):
    self._height = height
    return height

  def print_node(self):
    print("Parent: ",self._parent, " / Key: ", self._key, " / Left: ", self._left, " / Right: ", self._right, " / Height: ", self._height)