from Estado import Estado

class NodoArbol:
    def __init__(self, padre, state, cost, d, f):
        self.padre = padre
        self.state = state
        self.cost = cost
        self.d = d
        self.f = f
    
    def iago_subnormal(self, ls, n_actual, prof_max, estrategia):
        return None