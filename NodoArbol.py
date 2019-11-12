class NodoArbol:
    def __init__(self, id, move, padre, state, cost, d, f):
        self.id = id
        self.move = move
        self.padre = padre
        self.state = state
        self.cost = cost
        self.d = d
        self.f = f
    
    def crear_lista_nodos(self, frontera, l_suc, n_actual, prof_max, estrategia):
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
        if estrategia == 1:
            return n.d
        elif estrategia == 2:
            return 1/(n.d + 1)
        elif estrategia == 3:
            return n.cost