from Cube import Cube
import rubiktools

class Estado:
    def __init__(self, cube):
        self.cube = cube

    def crear_sucesores(self):
        movimientos_L = ['L' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['l' + str(i) for i in range(0, self.cube.posicion_max + 1)]
        movimientos_B = ['B' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['b' + str(i) for i in range(0, self.cube.posicion_max + 1)]
        movimientos_D = ['D' + str(i) for i in range(0, self.cube.posicion_max + 1)] + ['d' + str(i) for i in range(0, self.cube.posicion_max + 1)]

        movimientos = movimientos_L + movimientos_B + movimientos_D
        print(movimientos)
        for i in movimientos:
            nuevoCubo = self.cube.llamar_movimiento(i)
            rubiktools.show_cube(nuevoCubo)
        return 1

    def imprimir_cubo(self):
        rubiktools.show_cube(self.cube)
