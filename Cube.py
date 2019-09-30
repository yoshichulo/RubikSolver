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

    def llamar_movimiento(self, movimiento): 
        letra = movimiento[0]
        posicion = int(movimiento[1:])
        if letra.islower():
            giro = -90
        else:
            giro = 90
        
        if letra == 'B' or letra == 'b':
            self.mover_BX(posicion, giro)
        
        elif letra == 'D' or letra == 'd':
            self.mover_DX(posicion, giro)
            
        elif letra == 'L' or letra == 'l':
            self.mover_LX(posicion, giro)
        
        else:
            print('Letra no válida')

    def mover_BX(self, posicion, giro):
        posicion_max = len(self.BACK) - 1

        # Guardamos una copia de las columnas antes de sustituirlas.
        fila_right = list(self.RIGHT[posicion])
        fila_up = list(self.UP[posicion])
        fila_left = list(self.LEFT[posicion])
        fila_down = list(self.DOWN[posicion])

        # Giro correspondiente a L (90º)
        if giro == 90: # 
            self.LEFT = copy_row(self.LEFT, posicion, fila_up)
            self.DOWN = copy_row(self.DOWN, posicion, fila_left)
            self.RIGHT = copy_row(self.RIGHT, posicion, fila_down)
            self.UP = copy_row(self.UP, posicion, fila_right)
            
            if posicion == 0:
                self.BACK = numpy.rot90(self.BACK, k=3)
            if posicion == posicion_max:
                self.FRONT = numpy.rot90(self.FRONT, k=3)
        
        # Giro correspondiente a l (-90º)
        elif giro == -90: # 
            self.LEFT = copy_row(self.LEFT, posicion, fila_down)
            self.DOWN = copy_row(self.DOWN, posicion, fila_right)
            self.RIGHT = copy_row(self.RIGHT, posicion, fila_up)
            self.UP = copy_row(self.UP, posicion, fila_left)
            
            if posicion == 0:
                self.BACK = numpy.rot90(self.BACK, k=1)
            if posicion == posicion_max:
                self.FRONT = numpy.rot90(self.FRONT, k=1)

    def mover_LX(self, posicion, giro):
        posicion_max = len(self.BACK) - 1
        posicion_inversa = posicion_max - posicion

        # Guardamos una copia de las columnas antes de sustituirlas.
        columna_back = [row[posicion] for row in self.BACK]
        columna_up = [row[posicion_inversa] for row in self.UP]
        columna_front = [row[posicion] for row in self.FRONT]
        columna_down = [row[posicion] for row in self.DOWN]

        # Giro correspondiente a B (90º)
        if giro == 90: # 
            self.UP = copy_column(self.UP, posicion_inversa, list(reversed(columna_back)))
            self.FRONT = copy_column(self.FRONT, posicion, list(reversed(columna_up)))
            self.DOWN = copy_column(self.DOWN, posicion, columna_front)
            self.BACK = copy_column(self.BACK, posicion, columna_down)
            
            if posicion == 0:
                self.LEFT = numpy.rot90(self.LEFT, k=3)
            if posicion == posicion_max:
                self.RIGHT = numpy.rot90(self.RIGHT, k=3)
        
        # Giro correspondiente a b (-90º)
        elif giro == -90: # 
            self.UP = copy_column(self.UP, posicion_inversa, list(reversed(columna_front)))
            self.FRONT = copy_column(self.FRONT, posicion, columna_down)
            self.DOWN = copy_column(self.DOWN, posicion, columna_back)
            self.BACK = copy_column(self.BACK, posicion, list(reversed(columna_up)))
            
            if posicion == 0:
                self.LEFT = numpy.rot90(self.LEFT, k=1)
            if posicion == posicion_max:
                self.RIGHT = numpy.rot90(self.RIGHT, k=1)

    def mover_DX(self, posicion, giro):
        posicion_max = len(self.DOWN) - 1
        posicion_inversa = posicion_max - posicion

        # Guardamos una copia de las columnas y filas antes de sustituirlas.
        fila_back = list(self.BACK[posicion_inversa])
        columna_left = [row[posicion_inversa] for row in self.LEFT]
        fila_front = list(self.FRONT[posicion])
        columna_right = [row[posicion] for row in self.RIGHT]

        # Giro correspondiente a D (90º)
        if giro == 90: # 
            self.LEFT = copy_column(self.LEFT, posicion_inversa, fila_front)
            self.FRONT = copy_row(self.FRONT, posicion, list(reversed(columna_right)))
            self.RIGHT = copy_column(self.RIGHT, posicion, fila_back)
            self.BACK = copy_row(self.BACK, posicion_inversa, list(reversed(columna_left)))
            
            if posicion == 0:
                self.DOWN = numpy.rot90(self.DOWN, k=3)
            if posicion == posicion_max:
                self.UP = numpy.rot90(self.UP, k=3)
        
        # Giro correspondiente a d (-90º)
        elif giro == -90: # 
            self.LEFT = copy_column(self.LEFT, posicion_inversa, list(reversed(fila_back)))
            self.FRONT = copy_row(self.FRONT, posicion, columna_left)
            self.RIGHT = copy_column(self.RIGHT, posicion, list(reversed(fila_front)))
            self.BACK = copy_row(self.BACK, posicion_inversa, columna_right)
            
            if posicion == 0:
                self.DOWN = numpy.rot90(self.DOWN, k=1)
            if posicion == posicion_max:
                self.UP = numpy.rot90(self.UP, k=1)