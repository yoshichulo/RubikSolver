class Frontera:
    def __init__(self):
        self.frontera = []

    def insertar(self, nodo):
        self.frontera.append(nodo)

    def seleccionar_nodo(self):
        return self.frontera.pop(0)
    
    def esta_vacia(self):
        return True if len(self.frontera) == 0 else False