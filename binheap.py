class Minbinheap:
    def __init__(self, capacity):
       self.storage = [0]*capacity
       self.capacity = capacity
       self.size = 0

    def getParentIndex(self, index):
        return (index-1)//2
    
    def getLeftChildIndex(self, index):
        return 2 * index + 1
    
    def getRightChildIndex(self, index):
        return 2 * index + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) <= self.size - 1
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) <= self.size - 1
    
    def parent(self, index):
        return self.storage[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.storage[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.storage[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.size == self.capacity
    
    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def insert(self, data):
        if (self.isFull()):
            raise Exception ("El montículo está lleno")
        
        self.storage[self.size] = data
        self.size += 1
        self.siftup(self.size-1)

    def siftup(self, index):
        if(self.hasParent(index) and self.parent(index) > self.storage[index]):
            self.swap(self.getParentIndex(index), index)
            self.siftup(self.getParentIndex(index))

    def removeMin(self):
        if (self.size == 0):
            raise Exception("Montículo vacío")
        
        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        self.siftdown(0)
        return data
    
    def siftdown(self, index):
        smallest = index
        if(self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index)):
            smallest = self.getLeftChildIndex(index)

        if(self.hasRightChild(index) and self.storage[smallest] > self.rightChild(index)):
            smallest = self.getRightChildIndex(index)

        if(smallest!=index):
            self.swap(index, smallest)
            self.siftdown(smallest)

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
            self.siftup(index)
        elif newValue > oldValue:
            self.siftdown(index)

    def remove(self, key):
        index = self.findIndex(key)
        if index == -1:
            raise Exception("El valor no se encuentra en el montículo")
        self.storage[index] = float("-inf")
        self.siftup(index)
        self.removeMin()

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

    def print_binheap(self):
        for i in self.storage:
            print(i)

def run_tests():
    print("Iniciando pruebas...")

    # Crear un binheap con capacidad de 10
    binheap = Minbinheap(10)

    # Prueba de inserción
    print("Prueba de inserción:")
    binheap.insert(10)
    binheap.insert(5)
    binheap.insert(20)
    binheap.insert(1)
    binheap.insert(67)
    binheap.insert(66)
    binheap.insert(23)
    binheap.insert(11)
    binheap.insert(78)
    binheap.insert(78)
    binheap.print_binheap()
    print(f"binheap después de inserciones: {binheap.storage[:binheap.size]}")  # Esperado: [1, 5, 20, 10]
    binheap.remove(1)
    print(f"binheap después de inserciones: {binheap.storage[:binheap.size]}")
    # Prueba de removeMin
    print("\nPrueba de removeMin:")
    print(f"Elemento removido: {binheap.removeMin()}")  # Esperado: 1
    print(f"binheap después de removeMin: {binheap.storage[:binheap.size]}")  # Esperado: [5, 10, 20]

    # Prueba de inserción adicional
    print("\nPrueba de inserción adicional:")
    binheap.insert(3)
    binheap.insert(8)
    print(f"binheap después de más inserciones: {binheap.storage[:binheap.size]}")  # Esperado: [3, 5, 20, 10, 8]

    # Prueba de múltiples removals
    print("\nPrueba de múltiples removeMin:")
    while binheap.size > 0:
        print(f"Elemento removido: {binheap.removeMin()}")
        print(f"binheap después de removeMin: {binheap.storage[:binheap.size]}")
    binheap.removeMin()

# Ejecutar las pruebas
#run_tests()