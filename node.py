class Node:
  def __init__(self, key, left, right, parent):
    self._key = key
    self._left = left
    self._right = right
    self._parent = parent
 
  #gets

  def get_key(self):
    return self._key

  def get_left(self):
    return self._left

  def get_right(self):
    return self._right

  def get_parent(self):
    return self._parent
  
  #sets

  def set_key(self, key):
    self._key = key
  
  def set_left(self, node):
    self._left = node

  def set_right(self, node):
    self._right = node

  def set_parent(self, node):
    self._parent = node

  def print_node(self):
    print("Parent: ",self._parent, " / Key: ", self._key, " / Left: ", self._left, " / Right: ", self._right)