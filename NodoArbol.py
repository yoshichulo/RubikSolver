from Estado import Estado

class NodoArbol:
    def __init__(self, id, id_padre, state, cost, action, d, f):
        self.id = id
        self.id_padre = id_padre
        self.state = state
        self.cost = cost
        self.action = action
        self.d = d
        self.f = f