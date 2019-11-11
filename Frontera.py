import bisect
from collections import deque

class Frontera:
    def __init__(self):
        self.frontera = deque()

    def insertarFIFO(self, nodo):
        self.frontera.append(nodo)

    def insertarLIFO(self, nodo):
        self.frontera.appendleft(nodo)

    def insertarCU(self, nodo):
        aux = []
        pos = 0
        for n in self.frontera:
            bisect.insort(aux, n.cost)
            pos = aux.index(n.cost)
        self.frontera.insert(pos, nodo)

    def seleccionar_nodo(self):
        return self.frontera.popleft()
    
    def esta_vacia(self):
        return True if len(self.frontera) == 0 else False