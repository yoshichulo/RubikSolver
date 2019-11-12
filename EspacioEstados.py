from Estado import Estado

class EspacioEstados:
    """
    Esta clase contiene nuestro Espacio de Estados, que será el responsable de generar todos los sucesores
    para los nodos que le pasemos como parámetro.
    """
    def sucesores(self, nodo):
        """
        Función encargada de crear todos los sucesores de un nodo pasado como parámetro.
        Retorna una tupla (mov, nuevoEstado), donde:
        - mov: es el movimiento que se le aplicará al Cubo.
        - nuevoEstado: el nuevo Estado que tendrá el cubo tras aplicarle el movimiento.
        """
        estado = nodo.state
        movimientos_B = ['B' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['b' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_D = ['D' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['d' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_L = ['L' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['l' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos = movimientos_B + movimientos_D + movimientos_L

        return [(mov, Estado(estado.cube.llamar_movimiento(mov))) for mov in movimientos]