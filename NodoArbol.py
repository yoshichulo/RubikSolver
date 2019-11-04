from Estado import Estado

class NodoArbol:
    def __init__(self, move, padre, state, cost, d, f):
        self.move = move
        self.padre = padre
        self.state = state
        self.cost = cost
        self.d = d
        self.f = f
    
    def crear_lista_nodos(self, l_suc, n_actual, prof_max, estrategia):
        if n_actual.d < prof_max:
            array_suc = []
            for suc in l_suc:
                move, state  = suc
                array_suc.append(NodoArbol(move, n_actual, state, n_actual.cost + 1, n_actual.d + 1, n_actual.f + 1))
            return array_suc