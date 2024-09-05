from dynamic_array import array
from BST import BST
from AVL import AVL
from binheap import Minbinheap
from ternheap import TernaryHeap
from dsj_set import DisjointSet
import random as rnd
import time 
import sys

sys.setrecursionlimit(10000)

DATA_RANGE = (0,100)
WIDTH = 500
HEIGHT = 500
DIVISIONS = 5
COLD_TRESHOLD = 3

class map:
    def __init__(self, x, y):
        self._mother = array(y)
        self._width = x
        self._height = y
        for i in range(y):
            self._mother.add(array(x, i))
        self._mother._size = 0


    def get_row(self, pos):
        for i in self._mother._array:
            if i.get_pos() == pos:
                return i
    
    def get_row_array(self, pos):
        for i in self._mother._array:
            if i.get_pos() == pos:
                return i._array

    def get_mother(self):
        return self._mother
    
    def print_map(self):
        for i in range(self._height):
            print(self.get_row_array(i))

    def get(self, x, y):
        row = self.get_row(x)
        return row.get(y)

    def replace(self, key, x, y):
        row = self.get_row(x)
        row.replace(key, y)

    def add(self, key):
        mother = self.get_mother()
        row = self.get_row(mother.get_size())
        if row.about_to_full():
            mother._size += 1
        row.add(key)

    def copy(self):
        new = map(self._width, self._height)
        new._mother = self.get_mother()
        return new

    def to_BST(self):
        mother = self.get_mother()
        tree = BST(self.get(0,0))
        for i in range(self._height):
            row = self.get_row(i)
            counter = 0
            for j in row._array:
                if i == 0 and counter == 0:
                    counter += 1
                else:
                    tree.insert(j)
                    counter += 1 

        #tree.delete_root()
        return tree
    
    def to_AVL(self):
        #print("TO AVL")
        mother = self.get_mother()
        tree = AVL(self.get(0,0))
        for i in range(self._height):
            row = self.get_row(i)
            counter = 0
            for j in row._array:
                if i == 0 and counter == 0:
                   counter += 1
                else:
                    tree.insert(j)
                    counter += 1
        #first = self.get(0,0)
        #print("PRINT TREE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #tree.print_tree()
        #tree.delete(first)
        #print("PRINT TREE >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        #tree.print_tree()
        return tree

    def to_binheap(self):
        WIDTH = self._width
        HEIGHT = self._height
        h = Minbinheap(WIDTH*HEIGHT)
        for i in range(self._height):
            row = self.get_row(i)
            for j in row._array:
               h.insert(j)
        return h
    
    def to_ternheap(self):
        WIDTH = self._width
        HEIGHT = self._height
        h = TernaryHeap(WIDTH*HEIGHT)
        for i in range(self._height):
            row = self.get_row(i)
            for j in row._array:
               h.insert(j)
        return h
    
    def to_range_map(self, divisions):
        new = self.copy()
        n = divisions

        for i in range(n):
            for j in range(new._height):
                counter = 0
                row = new.get_row(j)
                for k in row._array:
                    if i == n-1:
                        if k >= ((100/n)*i) and k <= ((100/n)*(i+1)):
                            lvl = (i+1)
                            #print("mira 1: ", new.get(counter, j))
                            #print("ro counter: ", row._array[counter])
                            new.replace(lvl, j,counter)
                    elif k >= ((100/n)*i) and k < ((100/n)*(i+1)):
                        lvl = (i+1)
                        #print("mira 2: ", new.get(counter, j))
                        #print("ro counter: ", row._array[counter])
                        new.replace(lvl, j, counter)
                    counter += 1

        return new

    def BST_inorder(self):
        tree = self.to_BST()
        tree.inorder_list(tree._root)
    
    def AVL_inorder(self):
        #print("AVL INORDER RESPONSE")
        tree = self.to_AVL()
        #tree.print_tree()
        tree.inorder_list(tree._root)

    def binheap_inorder(self):
        list = []
        cap = self._height * self._width
        h = self.to_binheap()
        i = 0
        while i < (cap):
            list.append(h.removeMin())
            i += 1
        
        return list

    def ternheap_inorder(self):
        list = []
        cap = self._height * self._width
        h = self.to_ternheap()
        i = 0
        while i < (cap):
            list.append(h.removeMin())
            i += 1
        
        return list
    
    def ternheap_inorder_list(self):
        cap = self._height * self._width
        list = array(cap)
        h = self.to_ternheap()
        i = 0
        while i < (cap):
            list.add(h.removeMin())
            i += 1
        
        return list

    
    def bin_ranges(self, divisions, listresult = False):
        list = []
        h = self.to_binheap()
        n = divisions
        cap = self._height * self._width
        arr = array(cap)
        #print(h.storage)
        for i in range(n):
            for j in h.storage:
                if i == n-1:
                    if j >= ((100/n)*i) and j <= ((100/n)*(i+1)):
                        arr.add(i+1)
                else:
                    if j >= ((100/n)*i) and j < ((100/n)*(i+1)):
                        arr.add(i+1)
        #print(arr._array)
        if listresult:
            for k in range(1, n+1):
                cont = 0
                for l in arr._array:
                    if l == k:
                        cont +=1
                list.append(cont)
                        
            #print(list)
        else:
            for k in range(1, n+1):
                cont = 0
                for l in arr._array:
                    if l == k:
                        cont +=1
                print("Number of numbers in range ", k,": ", cont)

    def tern_ranges(self, divisions, listresult = False):
        list = []
        h = self.to_ternheap()
        n = divisions
        cap = self._height * self._width
        arr = array(cap)
        #print(h.storage)
        for i in range(n):
            for j in h.storage:
                if i == n-1:
                    if j >= ((100/n)*i) and j <= ((100/n)*(i+1)):
                        arr.add(i+1)
                else:
                    if j >= ((100/n)*i) and j < ((100/n)*(i+1)):
                        arr.add(i+1)
        #print(arr._array)
        if listresult:
            for k in range(1, n+1):
                cont = 0
                for l in arr._array:
                    if l == k:
                        cont +=1
                list.append(cont)
                        
            #print(list)
        else:
            for k in range(1, n+1):
                cont = 0
                for l in arr._array:
                    if l == k:
                        cont +=1
                print("Number of numbers in range ", k,": ", cont) 

    def coordinates_to_index(self, x, y):
        # Convierte las coordenadas 2D (x, y) a un índice 1D en el array lineal
        return y * self._width + x

    def can_reach(self, x1, y1, x2, y2, n):
        """
        Determina si se puede llegar de (x1, y1) a (x2, y2) en el mapa,
        usando como condición que el valor de las celdas no sea mayor a `n`.
        
        :param x1: Coordenada x de la celda de inicio
        :param y1: Coordenada y de la celda de inicio
        :param x2: Coordenada x de la celda de destino
        :param n: Valor máximo permitido para que las celdas sean transitables
        :return: Booleano indicando si es posible llegar de (x1, y1) a (x2, y2)
        """
        # Inicializa el DisjointSet con el número de celdas en el mapa
        ds = DisjointSet(self._width * self._height)
        
        # Recorre las celdas del mapa
        for y in range(self._height):
            for x in range(self._width):
                # Obtén el valor actual de la celda
                current_value = self.get(x, y)
                
                # Verifica si la celda derecha está dentro del mapa
                if x + 1 < self._width:
                    right_value = self.get(x + 1, y)
                    # Condición: ambas celdas deben ser menores o iguales a n
                    if current_value <= n and right_value <= n:
                        ds.union(self.coordinates_to_index(x, y), self.coordinates_to_index(x + 1, y))
                
                # Verifica si la celda de abajo está dentro del mapa
                if y + 1 < self._height:
                    down_value = self.get(x, y + 1)
                    # Condición: ambas celdas deben ser menores o iguales a n
                    if current_value <= n and down_value <= n:
                        ds.union(self.coordinates_to_index(x, y), self.coordinates_to_index(x, y + 1))
        
        # Verifica si los puntos (x1, y1) y (x2, y2) están conectados
        return ds.find(self.coordinates_to_index(x1, y1)) == ds.find(self.coordinates_to_index(x2, y2))
    
def can_connect_refuges(map, refugios, n):
        # Tamaño del mapa
        height = map._height
        width = map._width
    
        # Inicializar Disjoint Set
        ds = DisjointSet(height * width)
    
        # Unión de casillas válidas (alturas <= n)
        for y in range(height):
            for x in range(width):
                if map.get(x, y) <= n:  # La celda actual es "segura"
                    # Verificar las casillas adyacentes que también sean seguras
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # Movimientos: izquierda, derecha, arriba, abajo
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < width and 0 <= ny < height and map.get(nx, ny) <= n:
                            # Unir las casillas en el DisjointSet
                            ds.union(y * width + x, ny * width + nx)
    
        # Ahora, verificar si los refugios están conectados
        first_refuge = refugios[0][1] * width + refugios[0][0]  # Convertir coordenada a índice lineal
        for refuge in refugios[1:]:
            refuge_idx = refuge[1] * width + refuge[0]
            if ds.find(first_refuge) != ds.find(refuge_idx):
                return False  # Hay al menos un refugio no conectado
    
        return True  # Todos los refugios están conectados


    
         

def run_random_map(WIDTH, HEIGHT):

    m = map(WIDTH, HEIGHT)

    i = 0
    while i < ((WIDTH*HEIGHT)):
        a = rnd.randint(DATA_RANGE[0], DATA_RANGE[1])
        m.add(a)
        i += 1

    return m

def bin_ranges_test(WIDTH, HEIGHT, n, listresult = False):

    m = run_random_map(WIDTH, HEIGHT)

    INICIO = time.time()
    m.bin_ranges(n, listresult)
    FIN = time.time()

    print("time taken: ", (FIN - INICIO))

def tern_ranges_test(WIDTH, HEIGHT, n, listresult = False):

    m = run_random_map(WIDTH, HEIGHT)

    INICIO = time.time()
    result = m.tern_ranges(n, listresult)
    FIN = time.time()

    print("time taken: ", (FIN - INICIO))

def tree_test(WIDTH, HEIGHT):
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO = time.time()
    m.BST_inorder()
    FIN = time.time()
    
    print("time taken: ", (FIN - INICIO))

def AVL_test(WIDTH, HEIGHT):
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO = time.time()
    #print("AVL INORDER ASK")
    m.AVL_inorder()
    FIN = time.time()
    
    print("time taken: ", (FIN - INICIO))

def binheap_test(WIDTH, HEIGHT):
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO = time.time()
    m.binheap_inorder()
    FIN = time.time()

    print("time taken: ", (FIN - INICIO))

def ternheap_test(WIDTH, HEIGHT):
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO = time.time()
    m.ternheap_inorder()
    FIN = time.time()

    print("time taken: ", (FIN - INICIO))

def ternheap_test_array(WIDTH, HEIGHT): #>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>><<
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO = time.time()
    m.ternheap_inorder_list()
    FIN = time.time()

    print("time taken: ", (FIN - INICIO)) 

def test1(WIDTH, HEIGHT):
    print("Running test 1")
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO_BST  = time.time()
    m.BST_inorder()
    FIN_BST = time.time()
    
    print("time taken (BST): ", (FIN_BST - INICIO_BST))

    INICIO_BIN = time.time()
    m.  binheap_inorder()
    FIN_BIN = time.time()
    
    print("time taken (BIN): ", (FIN_BIN - INICIO_BIN))

    INICIO_TERN = time.time()
    m.ternheap_inorder()
    FIN_TERN = time.time()
    
    print("time taken (TERN): ", (FIN_TERN - INICIO_TERN))

    INICIO_AVL = time.time()
    #print("AVL INORDER ASK")
    m.AVL_inorder()
    FIN_AVL = time.time()
    
    print("time taken (AVL): ", (FIN_AVL - INICIO_AVL))

def test2(WIDTH, HEIGHT):
    print("Running test 2")
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO_AVL = time.time()
    #print("AVL INORDER ASK")
    m.AVL_inorder()
    FIN_AVL = time.time()
    
    print("time taken (AVL): ", (FIN_AVL - INICIO_AVL))

    INICIO_TERN = time.time()
    m.ternheap_inorder()
    FIN_TERN = time.time()
    
    print("time taken (TERN): ", (FIN_TERN - INICIO_TERN))

    INICIO_BST  = time.time()
    m.BST_inorder()
    FIN_BST = time.time()
    
    print("time taken (BST): ", (FIN_BST - INICIO_BST))

    INICIO_BIN = time.time()
    m.binheap_inorder()
    FIN_BIN = time.time()
    
    print("time taken (BIN): ", (FIN_BIN - INICIO_BIN))

    

def test3(WIDTH, HEIGHT):
    print("Running test 3")
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO_BIN = time.time()
    m.binheap_inorder()
    FIN_BIN = time.time()
    
    print("time taken (BIN): ", (FIN_BIN - INICIO_BIN))

    INICIO_AVL = time.time()
    #print("AVL INORDER ASK")
    m.AVL_inorder()
    FIN_AVL = time.time()
    
    print("time taken (AVL): ", (FIN_AVL - INICIO_AVL))

    INICIO_TERN = time.time()
    m.ternheap_inorder()
    FIN_TERN = time.time()
    
    print("time taken (TERN): ", (FIN_TERN - INICIO_TERN))

    INICIO_BST  = time.time()
    m.BST_inorder()
    FIN_BST = time.time()
    
    print("time taken (BST): ", (FIN_BST - INICIO_BST))

def multiple_inorder_tests(num):

    g = 0

    while g < num:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST ", g + 1, ": ")

        test1(WIDTH, HEIGHT)       
        test2(WIDTH, HEIGHT)  
        test3(WIDTH, HEIGHT)  

        g += 1

def ranges_tests1(WIDTH, HEIGHT, divisions, listresult = False):
    print("test 1")
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO_BIN  = time.time()
    m.bin_ranges(divisions, listresult)
    FIN_BIN = time.time()

    print("time taken (BIN): ", (FIN_BIN - INICIO_BIN)) 

    INICIO_TERN  = time.time()
    m.tern_ranges(divisions, listresult)
    FIN_TERN = time.time()

    print("time taken (TERN): ", (FIN_TERN - INICIO_TERN)) 

def ranges_tests2(WIDTH, HEIGHT, divisions, listresult = False):
    print("Test 2")
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    INICIO_TERN  = time.time()
    m.tern_ranges(divisions, listresult)
    FIN_TERN = time.time()

    print("time taken (TERN): ", (FIN_TERN - INICIO_TERN)) 

    INICIO_BIN  = time.time()
    m.bin_ranges(divisions, listresult)
    FIN_BIN = time.time()

    print("time taken (BIN): ", (FIN_BIN - INICIO_BIN)) 

def multiple_ranges_tests(num, listresult = True):

    g = 0

    while g < num:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST ", g + 1, ": ")

        ranges_tests1(WIDTH, HEIGHT, DIVISIONS, listresult)
        ranges_tests2(WIDTH, HEIGHT, DIVISIONS, listresult)  

        g += 1

    


#tree_test(WIDTH, HEIGHT)
#binheap_test(WIDTH, HEIGHT)
#ternheap_test(WIDTH, HEIGHT)
#ternheap_test_array(WIDTH, HEIGHT)
#AVL_test(WIDTH, HEIGHT)

#multiple_inorder_tests(2)

#ranges_tests(WIDTH, HEIGHT, 5)

#multiple_ranges_tests(1, False)

#m = run_random_map(WIDTH, HEIGHT)

#m.print_map()

#rngmap = m.to_range_map(DIVISIONS)

#rngmap.print_map()

#coordenadas

def test_reach():
    m = run_random_map(WIDTH, HEIGHT)

    rngmap = m.to_range_map(DIVISIONS)

    x1 = 0
    y1 = 0
    x2 = 1
    y2 = 1

    INICIO = time.time()
    if rngmap.can_reach(x1, y1, x2, y2, COLD_TRESHOLD):
        pass
    FIN = time.time()
        #print(f"Puedes llegar de ({x1}, {y1}) a ({x2}, {y2}) con celdas de valor menor o igual a {COLD_TRESHOLD}")
    #else:
        #print(f"No puedes llegar de ({x1}, {y1}) a ({x2}, {y2}) con celdas de valor menor o igual a {COLD_TRESHOLD}")
    print("time taken: ", (FIN - INICIO))

def test_ref():
    #Coordenadas de los refugios
    refugios = [(0,0), (1, 1), (0, 1)]
    m = run_random_map(WIDTH, HEIGHT)

    #m.print_map()

    rngmap = m.to_range_map(DIVISIONS)

    INICIO = time.time()
    if can_connect_refuges(rngmap, refugios, COLD_TRESHOLD):
        pass
    FIN = time.time()
        #print("Todos los refugios están conectados.")
    #else:
        #print("No se puede llegar de un refugio a otro.")
    print("time taken: ", (FIN - INICIO))

def test_sets1():
    print("Test 1")
    m = run_random_map(WIDTH, HEIGHT)

    rngmap = m.to_range_map(DIVISIONS)

    x1 = 0
    y1 = 0
    x2 = HEIGHT - 1
    y2 = WIDTH - 1
    a = int(WIDTH/2)
    b= int(HEIGHT/2)
    refugios = [(0,0), (a, b), (x2, y2)]

    INICIO_REACH = time.time()
    rngmap.can_reach(x1, y1, x2, y2, COLD_TRESHOLD)
    FIN_REACH = time.time()

    print("time taken (REACH): ", (FIN_REACH - INICIO_REACH))

    INICIO_REF = time.time()
    can_connect_refuges(rngmap, refugios, COLD_TRESHOLD)
    FIN_REF = time.time()

    print("time taken (REF): ", (FIN_REF - INICIO_REF))

def test_sets2():
    print("Test 2")
    m = run_random_map(WIDTH, HEIGHT)

    rngmap = m.to_range_map(DIVISIONS)

    x1 = 0
    y1 = 0
    x2 = HEIGHT - 1
    y2 = WIDTH - 1
    a = int(WIDTH/2)
    b= int(HEIGHT/2)
    refugios = [(0,0), (a, b), (x2, y2)]

    INICIO_REF = time.time()
    can_connect_refuges(rngmap, refugios, COLD_TRESHOLD)
    FIN_REF = time.time()

    print("time taken (REF): ", (FIN_REF - INICIO_REF))

    INICIO_REACH = time.time()
    rngmap.can_reach(x1, y1, x2, y2, COLD_TRESHOLD)
    FIN_REACH = time.time()

    print("time taken (REACH): ", (FIN_REACH - INICIO_REACH))

    

def multiple_sets_tests(num):

    g = 0

    while g < num:

        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>TEST ", g + 1, ": ")

        test_sets1()
        test_sets2()

        g += 1

#multiple_sets_tests(3)
#test_sets1()
multiple_ranges_tests(3)








