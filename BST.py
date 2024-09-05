
from node import Node

class BST:
  def __init__(self, root):
    self._root = Node(root, None, None, None)

  def _insert(self, key, root) -> Node:
    if root is None:
      return Node(key, None, None, None)
    elif root._key <= key:
      root._right = self._insert(key, root._right)
      root._right._parent = root
    elif root._key > key:
      root._left = self._insert(key, root._left)
      root._left._parent = root
    return root
    
  def insert(self, key) -> None:
    self._root = self._insert(key, self._root)

  def get_max(self, root):
    if root.get_right() is None:
      return root
    else:
      return self.get_max(root.get_right())

  def find(self, key, root):
    if root._key == key:
      return root
    elif root._key > key:
      return self.find(key, root._left)
    elif root._key < key:
      return self.find(key, root._right)
    else:
      return None

  def lastleft(self, root) -> Node:
    if root._left is None:
      return root
    else:
      return self.lastleft(root._left)

  def keylastleft(self, key):
    root = self.find(key, self._root)
    if root is not None:
      if root._left is None:
        return root
      else:
        return self.lastleft(root._left)
    else:
      return Node(0, None, None, None)
      
  def firstright(self, root) -> Node:
    if root._parent is None:
      return root
    elif root._key < root._parent._key:
      return root._parent
    else:
      return self.firstright(root._parent)

  def next(self, root):
    if root._right is not None:
      return self.lastleft(root._right)
    else:
      return self.firstright(root._parent)
      
  def remove(self, key):
    if key._right is None:
      if key._parent is None:
        self._root = key._left
      elif key._parent._key > key._key:
          key._parent._left = key._left
      else:
        key._parent._right = key._left

  def delete(self, root, key):
    
    # Base case
    if root is None:
        return root

    # If key to be searched is in a subtree
    if root.get_key() > key:
        root.set_left(self.delete(root.get_left(), key))
    elif root.get_key() < key:
        root.set_rigth(self.delete(root.get_right(), key))
        
    else:
        # If root matches with the given key

        # Cases when root has 0 children or 
        # only right child
        if root.get_left() is None:
            return root.get_right()

        # When root has only left child
        if root.get_right() is None:
            return root.get_left()

        # When both children are present
        succ = root.get_parent()
        root.set_key(succ.get_key())
        root.set_rigth(self.delete(root.get_right(), succ.get_key()))
        
    return root
  
  def delete_root(self):
    root = self._root
    if root.get_left() is None:
      new_root = root.get_right()
      new_root.set_parent(None)
      self._root = new_root

    elif root.get_left().get_right() is None:

      new_root = root.get_left()

      new_root.set_right(root.get_right())
      new_root.get_right().set_parent(new_root)
      new_root.set_parent(None)

      self._root = new_root

    else:
      new_root = root.get_left()
      right_subtree = new_root.get_right()

      new_root.set_right(root.get_right())
      new_root.get_right().set_parent(new_root)
      new_root.set_parent(None)

      anchor = self.next(new_root)

      anchor.set_left(right_subtree)
      right_subtree.set_parent(anchor)
      self._root = new_root
    
  def inorder(self, node) -> None:
    if node is None:
      return
    else:
      self.inorder(node.get_left())
      print(node.get_key())
      self.inorder(node.get_right())
  
  def inorder_list(self, node) -> None:
    list = []
    if node is None:
      return
    else:
      self.inorder_list(node.get_left())
      list.append(node.get_key())
      self.inorder_list(node.get_right())

    return list

def test():
  t = BST(1)
  root = t._root
  t.insert(5)
  t.insert(0.5)
  t.insert(20)
  t.insert(70)
  t.insert(2)
  t.insert(60)
  t.insert(17)
  t.insert(35)
  t.delete_root()
  print("root: ", t._root.get_key())
  t.inorder(t._root)

#test()



                            