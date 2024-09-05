from node_AVL import Node
import time 
from typing import Optional, Union
import sys

#sys.setrecursionlimit(5000)


class AVL:
  def __init__(self, root):
    self._root = Node(root, None, None, None)

  def get_root(self) -> Node:
    return self._root

  def insert(self, key: float):
    self._insert_(key, self._root)

  def _insert_(self, key:float, node:Optional[Node]) -> Node :
    if node is None:
      return Node(key, None, None, None)
    
    elif key >= node.get_key():
      node.set_right(self._insert_(key, node.get_right()))
      node.get_right().set_parent(node)

    elif key < node.get_key():
      node.set_left(self._insert_(key, node.get_left()))
      node.get_left().set_parent(node)

    
    height = 1 + max(self.get_height(node.get_left()), self.get_height(node.get_right()))
    node.set_n_height(height)

    balance = self.get_balance(node)

    if balance > 1:
      if key < node.get_left().get_key():
        return self.right_rotate(node)
      else:
        if node.get_left() is Node:
          l_node = self.left_rotate(node.get_left())
          node.set_left(l_node)
          return self.right_rotate(node)
      
    if balance < -1:
      if key > node.get_right().get_key():
        return self.left_rotate(node)
      else:
        if node.get_right() is Node:
          r_node = self.right_rotate(node.get_right())
          node.set_right(r_node)
          return self.left_rotate(node)
    return node
  
  def get_height(self, node:Optional[Node]):
    if not node:
      return 0
    return node.get_height()
  
  def set_height(self, node:Optional[Node]):
    if node is None:
      return 0
    
    if node.get_left() == None and node.get_right() == None:
      height = node.set_n_height(1)
      return height
    
    elif node.get_right() == None:
        height = 1 + max(0, self.set_height(node.get_left()))

    elif node.get_left() == None:
        height = 1 + max(self.set_height(node.get_right()), 0)

    elif node.get_left() != None and node.get_right() != None:
        height = 1 + max(self.set_height(node.get_right()), self.set_height(node.get_left()))
    #print('si llega ')
    return node.set_n_height(height)
    
  def get_balance(self, node:Optional[Node]) -> int:
    if node == None:
      return 0
    else:
      left_height = node.get_left().get_height() if node.get_left() is not None else 0
      right_height = node.get_right().get_height() if node.get_right() is not None else 0

      return left_height - right_height

  def right_rotate(self, node:Node):
    #print('El nodo que está rotando right es:', node._key)
    p = node.get_parent()
    y = node.get_left()
    b = y.get_right()
    y.set_parent(p)
    

    if p is None: 
      self._root = y

    elif p.get_right() == node:
      p.set_right(y)
    
    elif p.get_left() == node:
      p.set_left(y)
      
    node.set_parent(y)
    y.set_right(node)

    if b is not None: 
        b.set_parent(node)
        node.set_left(b)

    if node.get_right() == y:
      node.set_right(None)
    elif node.get_left() == y: 
      node.set_left(None)
    #print('raiz:', self._root.get_key())
    self.set_height(self._root)
    return y

  def left_rotate(self, node:Node):
    #print('El nodo que está rotando left es:', node._key)
    p = node.get_parent()
    y = node.get_right()
    b = y.get_left()
    
    y.set_parent(p)

    if p is None: 
      self._root = y

    elif p.get_right() == node:
      p.set_right(y)
    
    elif p.get_left() == node:
      p.set_left(y)

    node.set_parent(y)
    
    y.set_left(node)
    
    if b is not None: 
      b.set_parent(node)
      node.set_right(b) 
      
    if node.get_right() == y:
      node.set_right(None)
    elif node.get_left() == y: 
      node.set_left(None)
    #print('raiz:', self._root.get_key())
    self.set_height(self._root)
    return y

  def rebalance(self, node:Node):
    #print('rebalance')
    if node.get_left() == None and node.get_right() == None:
        balance = 0
    
    else:
      balance = self.get_balance(node)

    if balance < -2 or balance > 2:
      #print('va a rebalance root')
      #time.sleep(3)
      self.rebalance_root(node)

    if balance == 2:

      if self.get_balance(node.get_left()) < 0:
        self.left_rotate(node.get_left())

      self.right_rotate(node)

    if balance == -2:

      if self.get_balance(node.get_right()) > 0:
        self.right_rotate(node.get_right())

      self.left_rotate(node)
    
    if node.get_parent() is not None:
      self.rebalance(node.get_parent())

    return None
    
  def rebalance_root(self, root:Optional[Node]):
    #print('rebalance root')
    if root == None:
      #print('es nulo')
      return None
    #print('ya entró')
    #time.sleep(1)
    #print('Nodo:', root.get_key(), 'Altura:', root.get_height())
    #time.sleep(1)
    #p = root.get_parent()
    #l = root.get_left()
    #r = root.get_right()
    #nodes = [p, l, r]
    #num = []
    #for i in nodes:
      #if i == None:
        #num.append(None)
      #else: 
        #num.append(i.get_key())
    
    #print('Parent:', num[0], 'Left:', num[1], 'Right:', num[2])
    #time.sleep(1)
    #time.sleep(1)

    if root.get_left() == None and root.get_right() == None:
        #print('es una hoja')
        #time.sleep(1)
        self.rebalance(root)
    
    else:
      #print('no es una hoja')
      #time.sleep(1)
      balance = self.get_balance(root)

      if balance > 2 or balance < -2:
      #print('está de más')
      #time.sleep(1)
        self.rebalance_root(root.get_left())
      #print('siguiente')
        self.rebalance_root(root.get_right())

      if balance == 2 or balance == -2:
      #print('vuelve a rebalance ')
      #time.sleep(1)
        self.rebalance(root)

      return None

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
    

  def find(self, key:float, temp_root:Node) -> Optional[Node]:
    if temp_root.get_key() == key:
      return temp_root
    elif temp_root.get_key() < key:
      return self.find(key, temp_root.get_right())
    elif temp_root.get_key() > key:
      return self.find(key, temp_root.get_left())
    else: 
      return None

  def left_descendant(self, node:Optional[Node]) -> Optional[Node]:
    if node.get_left() is None:
      return node
    else:
      return self.left_descendant(node.get_left())
    
  def right_descendant(self, node:Optional[Node]) -> Optional[Node]:
    if node.get_right() is None:
      return node
    else:
      return self.right_descendant(node.get_right()) 

  def right_ancestor(self, node:Optional[Node]) -> Optional[Node]:
    if node.get_parent() == None:
      return None    
    elif node.get_key() < node.get_parent().get_key():
      return node.get_parent()
    else:
      return self.right_ancestor(node.get_parent())

  def next(self, node:Optional[Node]) -> Optional[Node]:
    if node.get_right() is not None:
      return self.left_descendant(node.get_right())
    else:
      return self.right_ancestor(node)

  def range_search(self, a:float, b:float, root:Node) -> list:
    recurrences_list = []
    node = self.find(a, self.get_root())
    while node.get_key() <= b:
      if node.get_key() >= a:
        recurrences_list += node
      node = self.next(node)
    return recurrences_list
  
  def replace(self, replacer:Node, replaced:Node) -> None:
    #Se elimina la referencia en el padre del replacer
    parent = replacer.get_parent()
    if parent.get_right() == replacer:
        parent.set_right(None)

    elif parent.get_left() == replacer:
        parent.set_left(None)
    
    #Se reemplaza el nuevo parent
    if replaced == self.get_root():
      replacer.set_parent(None)
      self._root = replacer
      
    else: 
      replacer.set_parent(replaced.get_parent())

      #Se evalua a que lado del parent esta el replaced y se reemplaza por el replacer
      if replaced.get_parent().get_left() == replaced:
        replaced.get_parent().set_left(replacer)
    
      elif replaced.get_parent().get_right() == replaced:
        replaced.get_parent().set_right(replacer)

    #Ahora se gestiona lo que hay debajo de replaced y replacer
    right_replacer = replacer.get_right()
    left_replacer = replacer.get_left()

    if replaced.get_right() is not None:
        replaced.get_right().set_parent(replacer)
        replacer.set_right(replaced.get_right())

    if replaced.get_left() is not None:
        replaced.get_left().set_parent(replacer)
        replacer.set_left(replaced.get_left())

    if right_replacer is not None:
          next = self.next(replacer)
          next.set_left(right_replacer)
          right_replacer.set_parent(next)

    if left_replacer is not None:
      if replacer.get_left() is not None:
        before= self.right_descendant(replacer.get_left()) 
        before.set_left(left_replacer)
        left_replacer.set_parent(before)
      else:
        replacer.set_left(left_replacer)

    replaced.set_parent(None)
    replaced.set_left(None)
    replaced.set_right(None)

  def delete(self, key:float):
    node:Optional[Node] = self.find(key, self.get_root())
    p = node.get_parent()
    if node == None:
      raise KeyError("No existe ese nodo, entonces no se puede eliminar, dah")
    else:
      if node.get_right() == None and node.get_left() == None:
        p = node.get_parent()

        if p.get_left() == node:
          p.set_left(None)
          node.set_parent(None)

        elif p.get_right() == node:
          p.set_right(None)
          node.set_parent(None)

        self.set_height(self._root)
        self.rebalance(p)
        
      elif node.get_left() == None:
        r_node = node.get_right()
        self.replace(node.get_right(), node)
        self.set_height(self._root)
        self.rebalance(self.left_descendant(r_node))
        self.rebalance(self.right_descendant(r_node))

      else:
        l_node = self.right_descendant(node.get_left())

        self.replace(l_node, node)

        self.set_height(self._root)

        self.rebalance(l_node)

  def print_tree(self):
    min = self.left_descendant(self._root)
    a=1
    while a == 1:
      #time.sleep(0.25)
      if min is not None:
        print()
        print('Nodo:', min.get_key(), 'Altura:', min.get_height())
        p = min.get_parent()
        l = min.get_left()
        r = min.get_right()
        nodes = [p, l, r]
        num = []
        for i in nodes:
          if i == None:
            num.append(None)
          else: 
            num.append(i.get_key())
    
        print('Parent:', num[0], 'Left:', num[1], 'Right:', num[2])
        min = self.next(min)
      else:
        a=0
