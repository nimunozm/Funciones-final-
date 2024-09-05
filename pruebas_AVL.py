from AVL import  AVL
import time
import random

'''Tree = AVL(5)
Tree.insert(3.14159265358979323846264338327950288419716939937510582097494459230)
Tree.insert(13)
Tree.insert(17)
Tree.insert(2)
Tree.insert(8)
Tree.insert(11)
Tree.insert(13)
Tree.insert(20)
Tree.insert(20)
Tree.insert(0)
Tree.insert(-3)
Tree.insert(12)
Tree.insert(22)
Tree.insert(21)
Tree.insert(12)
Tree.insert(11)
Tree.insert(9)


Tree.inorder(Tree._root)

node_a = Tree.find(0, Tree._root)
a = node_a._key

node_b = Tree.find(20, Tree._root)
b = node_b._key

node_c = Tree.find(13, Tree._root)
c = node_c._key

node_d = Tree.find(2, Tree._root)
d = node_d._key

node_e = Tree.next(node_a)
e = node_e._key

node_f = Tree.next(node_c)
f = node_f._key

node_g = Tree.next(node_f)
g = node_g._key

node_h = Tree.next(node_d)
h = node_h._key

node_i = Tree.next(node_b)
i = node_i._key

print("-find-")
print('Node A (0):', a)
print('Nodo B (20):', b)
print('Nodo C (13):', c)
print('Nodo D (2):', d)
print("-next-")
print('Node E (a):', e)
print('Nodo F (c)', f)
print('Nodo G (f)', g)
print('Nodo H (d)', h)
print('Node I (b)', i)
print()
print('-alturas-')

min = Tree.left_descendant(Tree._root)
a=1
while a == 1:
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
    min = Tree.next(min)
  else:
    a=0

print()

print('-delete-')
print('root:', Tree._root.get_key())
Tree.delete(9)
Tree.delete(5)
Tree.delete(13)
print('Ahora eliminar el 0')
Tree.delete(0)

print('root:', Tree._root.get_key())
print('inicia for')
print()
#time.sleep(1)
#time.sleep(8)

to_delete = [13, 11, 20]

for i in to_delete:
  #time.sleep(2)
  print('')
  print('Eliminando el nodo ',i)
  print('')
  Tree.delete(i)

print('Terminamos ;3')'''


a=[]
for i in range(10):
    num = random.randint(0, 100)
    a.append(num)
    
print(a)

b = random.choice(a)
print('La raiz inicial será:', b)
a.remove(b)
Tree = AVL(b)
for i in a:
    
    print('está insertando:', i)
    Tree.insert(i)
    Tree.print_tree()

'''arraysss = [73, 30, 80, 15, 37, 20]
Tree= AVL(2)
for i in arraysss:
    print()
    print('está insertando:', i)
    Tree.insert(i)
    Tree.print_tree()'''

print('terminé')