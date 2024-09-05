class array:
  def __init__(self, capacity, opcional_pos = None):
    self._size = 0
    self._capacity = capacity
    self._array = []
    self._opcional_pos = opcional_pos
    i = 0
    while i < capacity:
      self._array = self._array + [None]
      i+= 1

  def get_size(self):
    return self._size

  def get_cap(self):
    return self._capacity 

  def get_pos(self):
    return self._opcional_pos
  
  def get(self, index):
    if index < 0 or index >= self._capacity:
      raise Exception("Papi, no hay nada ahí, de hecho ni siquiera hay nada")
    return self._array[index]
  
  def is_empty(self):
    return self._array[0] == None
  
  def is_full(self):
    return self._size == self._capacity
  
  def about_to_full(self):
    return self._size == self._capacity - 1
    
  def replace(self, value, index):
    if index < 0 or index >= self._capacity:
      raise Exception("Papi, no hay nada ahí, de hecho ni siquiera hay nada")
    self._array[index] = value
  
  def add(self, value):
    if self._size == self._capacity:
      new_array = array(self._capacity * 2)
      for i in range(self._size):
        new_array._array[i] = self._array[i]
      self._array = new_array._array
      self._capacity *= 2
    self._array[self._size] = value
    self._size += 1

  def remove(self, index):
    if index < 0 or index >= self._size:
      raise Exception("Papi, no hay nada ahí, de hecho ni siquiera hay nada")
    for i in range(index, self._size -1):
      self._array[i] = self._array[i + 1]
    self._size -= 1

  def print_array(self):
    array = []
    i = 0
    while i < self._size:
      array = array + [None]
      i+= 1
    for j in range(self._size):
      array[j] = self._array[j] 
    print(array)
  
  def copy(self):
    new_array = array(self._capacity)
    for i in range(self._size):
      new_array._array[i] = self._array[i]
    return new_array


   
h = (array(2))
h.add(3)
h.add(5)


