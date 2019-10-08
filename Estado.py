from Cube import Cube
import copy
import rubiktools

class Estado:
    def __init__(self, cube):
        self.cube = copy.deepcopy(cube)

    def crear_sucesores(self):
        movimientos_L = ['L' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['l' + str(i) for i in range(0, self.cube.posicion_max + 1)]
        movimientos_B = ['B' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['b' + str(i) for i in range(0, self.cube.posicion_max + 1)]
        movimientos_D = ['D' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['d' + str(i) for i in range(0, self.cube.posicion_max + 1)]
        movimientos = movimientos_L + movimientos_B + movimientos_D

        return [Estado(self.cube.llamar_movimiento(i)) for i in movimientos]