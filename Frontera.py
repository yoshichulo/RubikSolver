class Frontera:
    def __init__(self):
        self.frontera = []
        self.orden = ""

    def crear_frontera(self, orden):
        self.orden = orden

    def insertar(self, nodo):
        self.frontera.append(nodo)

    def eliminar(self):
        self.frontera.pop()
    
    def esta_vacia(self):
        return True if len(self.frontera) == 0 else False