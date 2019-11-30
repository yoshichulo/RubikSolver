import math


class NodoArbol:
    """
    Esta clase contiene un Nodo del árbol de búsqueda. 
    Los distintos atributos que tendrá son:
        - NodoArbol.id: id del nodo
        - NodoArbol.move: movimiento que se le ha aplicado al cubo para llegar hasta el nodo
        - NodoArbol.padre: contiene el padre del nodo
        - NodoArbol.state: contiene el estado actual del nodo
        - NodoArbol.cost: costo de llegar hasta el nodo
        - NodoArbol.d: profundidad del nodo
        - NodoArbol.f: valor f del nodo
    """
    def __init__(self, id, move, padre, state, cost, d, f):
        """ Constructor de la clase NodoArbol """
        self.id = id
        self.move = move
        self.padre = padre
        self.state = state
        self.cost = cost
        self.d = d
        self.f = f
        self.h = self.calcular_h()
    
    def crear_lista_nodos(self, frontera, l_suc, n_actual, prof_max, estrategia):
        """ Función encargada de crear la lista de nodos en función de una lista de sucesores """
        if n_actual.d < prof_max:
            array_suc = []
            for suc in l_suc:
                move, state = suc
                nodo_suc = NodoArbol(frontera.next_id, move, n_actual, state, n_actual.cost + 1, n_actual.d + 1, None)
                nodo_suc.f = self.calcular_f(estrategia, nodo_suc)
                array_suc.append(nodo_suc)
                frontera.next_id += 1

            return array_suc

    def calcular_f(self, estrategia, n):
        """ Función encargada de retornar un valor de f en función del nodo y la estrategia elegidas """
        if estrategia == 1:
            return n.d
        elif estrategia == 2:
            return 1/(n.d + 1)
        elif estrategia == 3:
            return n.cost
        elif estrategia == 4:
            return n.h
        elif estrategia == 5:
            return n.h + n.cost

    def calcular_h(self):
        cube = self.state.cube
        heuristica = 0
        faces = [cube.BACK, cube.DOWN, cube.FRONT, cube.LEFT, cube.RIGHT, cube.UP]
        for face in faces:
            entropia = 0
            contador = self.calcular_color(face)
            for c in range(6):
                if contador[c] > 0.0:
                    entropia += contador[c]/(len(face)**2) * math.log(contador[c]/(len(face)**2), 6)
            heuristica += -entropia
        return heuristica

    def calcular_color(self, face):
        contador = [0,0,0,0,0,0]
        for row in face:
            for column in row:
                contador[column] += 1
        return contador
