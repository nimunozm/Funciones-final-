class TernaryHeap:
    def __init__(self, capacity):
       self.storage = [0]*capacity
       self.capacity = capacity
       self.size = 0

    def getParentIndex(self, index):
        return (index-1)//3
    
    def getLeftChildIndex(self, index):
        return 3 * index + 1
    
    def getMiddleChildIndex(self, index):
        return 3 * index + 2
    
    def getRightChildIndex(self, index):
        return 3 * index + 3
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) <= self.size - 1
    
    def hasMiddleChild(self, index):
        return self.getMiddleChildIndex(index) <= self.size - 1
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) <= self.size - 1
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def middleChild(self, index):
        return self.storage[self.getMiddleChildIndex(index)] 
    
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size == 0
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if (self.isFull()):
            raise Exception ("El montículo está lleno")
        self.storage[self.size] = data
        self.size += 1
        self.heapifyUp(self.size-1)

    def heapifyUp(self, index):
        if(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.heapifyUp(self.getParentIndex(index))

    def removeMin(self):
        if (self.size == 0):
            raise Exception("Montículo vacío")
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.heapifyDown(0)
        return data
    
    def heapifyDown(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)
        if(self.hasMiddleChild(index) and self.storage[smallest] > self.middleChild(index)):
            smallest = self.getMiddleChildIndex(index)
        if(self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)
        if(smallest!=index):
            self.swap(index, smallest)
            self.heapifyDown(smallest)

    def findIndex(self, value):
        for i in range(self.size):
            if self.storage[i] == value:
                return i
        return -1  # Indica que el valor no se encontra dentro del montículo
    
    def changePriority(self, oldValue, newValue):
        index = self.findIndex(oldValue)
        if index == -1:
            raise Exception("El valor no se encuentra en el montículo")
        self.storage[index] = newValue
        if newValue < oldValue:
            self.heapifyUp(index)
        elif newValue > oldValue:
            self.heapifyDown(index)

def test_ternary_heap():
    print("Iniciando prueba del montículo terciario...")
    
    # Crear un montículo terciario con capacidad para 10 elementos
    heap = TernaryHeap(10)
    
    # Insertar algunos elementos
    print("Insertando elementos:")
    elements = [5, 7, 3, 8, 2, 9, 1, 4, 6, 0]
    for element in elements:
        heap.insert(element)
        print(f"Insertado: {element}, Montículo: {heap.storage[:heap.size]}")
    
    # Eliminar el mínimo (que debería ser 0)
    print("\nEliminando el mínimo:")
    
    while not heap.isEmpty():

        min_element = heap.removeMin()
        print(f"Elemento eliminado: {min_element}, Montículo: {heap.storage[:heap.size]}")

# Ejecutar el test
#test_ternary_heap()