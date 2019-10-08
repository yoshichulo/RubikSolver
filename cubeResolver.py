import json
import hashlib
import numpy
import rubiktools
from rubiktools import copy_column, copy_row

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


def llamar_movimiento(cube, movimiento): 
    letra = movimiento[0]
    posicion = int(movimiento[1:])
    if letra.islower():
        giro = -90
    else:
        giro = 90
    
    if letra == 'B' or letra == 'b':
        mover_BX(cube, posicion, giro)
    
    elif letra == 'D' or letra == 'd':
        mover_DX(cube, posicion, giro)
        
    elif letra == 'L' or letra == 'l':
        mover_LX(cube, posicion, giro)
    
    else:
        print('Letra no válida')

def mover_BX(cube, posicion, giro):
    print("Giro")

def mover_LX(cube, posicion, giro):
    posicion_max = len(cube.BACK) - 1
    posicion_inversa = posicion_max - posicion

    # Guardamos una copia de las columnas antes de sustituirlas.
    columna_back = [row[posicion] for row in cube.BACK]
    columna_up = [row[posicion_inversa] for row in cube.UP]
    columna_front = [row[posicion] for row in cube.FRONT]
    columna_down = [row[posicion] for row in cube.DOWN]

    # Giro correspondiente a L (90º)
    if giro == 90: # 
        cube.UP = copy_column(cube.UP, posicion_inversa, list(reversed(columna_back)))
        cube.FRONT = copy_column(cube.FRONT, posicion, list(reversed(columna_up)))
        cube.DOWN = copy_column(cube.DOWN, posicion, columna_front)
        cube.BACK = copy_column(cube.BACK, posicion, columna_down)
        
        if posicion == 0:
            cube.LEFT = numpy.rot90(cube.LEFT, k=3)
        if posicion == posicion_max:
            cube.RIGHT = numpy.rot90(cube.RIGHT, k=3)
    
    # Giro correspondiente a l (-90º)
    elif giro == -90: # 
        cube.UP = copy_column(cube.UP, posicion_inversa, list(reversed(columna_front)))
        cube.FRONT = copy_column(cube.FRONT, posicion, columna_down)
        cube.DOWN = copy_column(cube.DOWN, posicion, columna_back)
        cube.BACK = copy_column(cube.BACK, posicion, list(reversed(columna_up)))
        
        if posicion == 0:
            cube.LEFT = numpy.rot90(cube.LEFT, k=1)
        if posicion == posicion_max:
            cube.RIGHT = numpy.rot90(cube.RIGHT, k=1)

    # Mostramos el cubo
    rubiktools.show_cube(cube)

def mover_DX(cube, posicion, giro):
    posicion_max = len(cube.DOWN) - 1
    posicion_inversa = posicion_max - posicion

    # Guardamos una copia de las columnas y filas antes de sustituirlas.
    fila_back = list(cube.BACK[posicion_inversa])
    columna_left = [row[posicion_inversa] for row in cube.LEFT]
    fila_front = list(cube.FRONT[posicion])
    columna_right = [row[posicion] for row in cube.RIGHT]

    # Giro correspondiente a D (90º)
    if giro == 90: # 
        cube.LEFT = copy_column(cube.LEFT, posicion_inversa, fila_front)
        cube.FRONT = copy_row(cube.FRONT, posicion, list(reversed(columna_right)))
        cube.RIGHT = copy_column(cube.RIGHT, posicion, fila_back)
        cube.BACK = copy_row(cube.BACK, posicion_inversa, list(reversed(columna_left)))
        
        if posicion == 0:
            cube.DOWN = numpy.rot90(cube.DOWN, k=3)
        if posicion == posicion_max:
            cube.UP = numpy.rot90(cube.UP, k=3)
    
    # Giro correspondiente a D (-90º)
    elif giro == -90: # 
        cube.LEFT = copy_column(cube.LEFT, posicion_inversa, list(reversed(fila_back)))
        cube.FRONT = copy_row(cube.FRONT, posicion, columna_left)
        cube.RIGHT = copy_column(cube.RIGHT, posicion, list(reversed(fila_front)))
        cube.BACK = copy_row(cube.BACK, posicion_inversa, columna_right)
        
        if posicion == 0:
            cube.DOWN = numpy.rot90(cube.DOWN, k=1)
        if posicion == posicion_max:
            cube.UP = numpy.rot90(cube.UP, k=1)

    # Mostramos el cubo
    rubiktools.show_cube(cube)
data_json = json.load(open('cube.json'))
cube = Cube(data_json)


# Hacemos un movimiento
llamar_movimiento(cube, 'd0')
llamar_movimiento(cube, 'D0')