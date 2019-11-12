import copy

class Estado:
    """
    Esta clase contiene el Estado de un nodo, creado a partir de un cubo que le han pasado como parámetro.
    Los distintos atributos que tendrá son:
        - Estado.cube: contendrá una copia del cubo.
        - Estado.md5: contendrá el cubo en formato md5
    """
    def __init__(self, cube):
        """ Constructor de la clase Estado """
        self.cube = copy.deepcopy(cube)
        self.md5 = cube.hash()
