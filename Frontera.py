import bisect
from heapq import heappop, heappush
from collections import deque

class Frontera:
    def __init__(self):
        self.frontera = []
        self.next_id = 0

    def insertar_nodo(self, nodo):
        heappush(self.frontera, (nodo.f, nodo.id, nodo))

    def seleccionar_nodo(self):
        return heappop(self.frontera)
    
    def esta_vacia(self):
        return True if len(self.frontera) == 0 else False