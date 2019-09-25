import json
import hashlib
import numpy
import rubiktools
from rubiktools import copy_column

class Cube:
    def __init__(self, data_json):
        self.BACK = data_json["BACK"]
        self.DOWN = data_json["DOWN"]
        self.FRONT = data_json["FRONT"]
        self.LEFT= data_json["LEFT"]
        self.RIGHT = data_json["RIGHT"]
        self.UP = data_json["UP"]
        self.hash = hashlib.md5(self.toString().encode()).hexdigest()
    
    def toString(self):
        cube_array = self.BACK + self.DOWN + self.FRONT + self.LEFT + self.RIGHT + self.UP
        return ''.join(str(n) for row in cube_array for n in row)


data_json = json.load(open('cube.json'))
cube = Cube(data_json)


def llamar_movimiento(cube, movimiento): 
    letra = movimiento[0]
    numero = int(movimiento[1:])
    if letra.islower():
        giro = -90
    else:
        giro = 90
    
    if letra == 'B' or letra == 'b':
        mover_BX(cube, numero, giro)
    
    elif letra == 'D' or letra == 'd':
        mover_DX(cube, numero, giro)
        
    elif letra == 'L' or letra == 'l':
        mover_LX(cube, numero, giro)
    
    else:
        print('Letra no válida')

def mover_BX(cube, posicion, giro):
    print("Giro")

def mover_DX(cube, posicion, giro):
    print("Giro")

def mover_LX(cube, posicion, giro):
    n = len(cube.BACK)
    posicion_inversa = n - posicion - 1

    if giro == 90:
        columna_back = list(reversed([row[posicion] for row in cube.BACK]))
        columna_up = list(reversed([row[posicion_inversa] for row in cube.UP]))
        columna_front = [row[posicion] for row in cube.FRONT]
        columna_down = [row[posicion] for row in cube.DOWN]

        cube.UP = copy_column(cube.UP, posicion_inversa, columna_back)
        cube.FRONT = copy_column(cube.FRONT, posicion, columna_up)
        cube.DOWN = copy_column(cube.DOWN, posicion, columna_front)
        cube.BACK = copy_column(cube.BACK, posicion, columna_down)
        
        if posicion == 0:
            cube.LEFT = numpy.rot90(cube.LEFT, k=3)
        if posicion == n -1:
            cube.RIGHT = numpy.rot90(cube.RIGHT, k=3)
    
    rubiktools.save_cube(cube)

llamar_movimiento(cube, 'L0')

#rubiktools.save_cube(cube)


    
'''
1  2  3         7 4 1
4  5  6   ===>  8 5 2
7  8  9         9 6 3
'''