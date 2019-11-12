import json
import hashlib
import numpy
import copy
from rubiktools import copy_column, copy_row

class Cube:
    """
    Esta clase contiene nuestro Cubo, en función del .json que le hayamos suministrado en el constructor.
    Los distintos atributos que tendrá son:
        - Cube.BACK: parte trasera del cubo.
        - Cube.DOWN: parte inferior del cubo.
        - Cube.FRONT: parte delantera del cubo.
        - Cube.LEFT: parte izquierda del cubo.
        - Cube.RIGHT: parte derecha del cubo.
        - Cube.posicion_max: posición máxima del movimiento que podrá hacer el cubo.
    """
    def __init__(self, data_json):
        """ Consructor de la clase Cubo """
        self.BACK = numpy.array(data_json["BACK"], dtype=numpy.int8)
        self.DOWN =  numpy.array(data_json["DOWN"], dtype=numpy.int8)
        self.FRONT =  numpy.array(data_json["FRONT"], dtype=numpy.int8)
        self.LEFT=  numpy.array(data_json["LEFT"], dtype=numpy.int8)
        self.RIGHT =  numpy.array(data_json["RIGHT"], dtype=numpy.int8)
        self.UP =  numpy.array(data_json["UP"], dtype=numpy.int8)
        self.posicion_max = len(self.DOWN) - 1
    
    def __str__(self):
        """ Función que devolverá el cubo en formato de string """
        cube_array = numpy.concatenate((self.BACK,self.DOWN,self.FRONT,self.LEFT,self.RIGHT,self.UP))
        return ''.join(str(n) for row in cube_array for n in row)

    def hash(self):
        """ Función que devolverá el cubo en formato de md5 """
        return hashlib.md5(self.__str__().encode()).hexdigest()

    def llamar_movimiento(self, movimiento):
        """
        Función que retornará un cubo al que se le ha realizado el movimiento pasado como parámetro .
        Los posibles movimientos serán BX, bX, DX, dX, LX, lX, donde X es un número entre 0 y Cube.posicion_max.
        La diferencia entre los movimientos en mayúsculas y su equivalente en minúsculas es la dirección del giro.
        """
        letra = movimiento[0]
        posicion = int(movimiento[1:])

        if posicion > self.posicion_max:
            print("La posición excede el máximo posible")
        else:
            if letra.islower():
                giro = -90
            else:
                giro = 90
            
            if letra == 'B' or letra == 'b':
                return self.mover_BX(posicion, giro)
            
            elif letra == 'D' or letra == 'd':
                return self.mover_DX(posicion, giro)
                
            elif letra == 'L' or letra == 'l':
                return self.mover_LX(posicion, giro)
            
            else:
                print('Letra no válida')

    def mover_BX(self, posicion, giro):
        """ Función correspondiente al movimiento BX """
        cube = copy.deepcopy(self)

        # Guardamos una copia de las columnas antes de sustituirlas.
        fila_right = list(self.RIGHT[posicion])
        fila_up = list(self.UP[posicion])
        fila_left = list(self.LEFT[posicion])
        fila_down = list(self.DOWN[posicion])

        # Giro correspondiente a B (90º)
        if giro == 90: # 
            cube.LEFT = copy_row(cube.LEFT, posicion, fila_up)
            cube.DOWN = copy_row(cube.DOWN, posicion, fila_left)
            cube.RIGHT = copy_row(cube.RIGHT, posicion, fila_down)
            cube.UP = copy_row(cube.UP, posicion, fila_right)
            
            if posicion == 0:
                cube.BACK = numpy.rot90(cube.BACK, k=3)
            if posicion == self.posicion_max:
                cube.FRONT = numpy.rot90(cube.FRONT, k=3)
        
        # Giro correspondiente a b (-90º)
        elif giro == -90: # 
            cube.LEFT = copy_row(cube.LEFT, posicion, fila_down)
            cube.DOWN = copy_row(cube.DOWN, posicion, fila_right)
            cube.RIGHT = copy_row(cube.RIGHT, posicion, fila_up)
            cube.UP = copy_row(cube.UP, posicion, fila_left)
            
            if posicion == 0:
                cube.BACK = numpy.rot90(cube.BACK, k=1)
            if posicion == self.posicion_max:
                cube.FRONT = numpy.rot90(cube.FRONT, k=1)

        return cube


    def mover_LX(self, posicion, giro):
        """ Función correspondiente al movimiento LX """
        posicion_inversa = self.posicion_max - posicion
        cube = copy.deepcopy(self)

        # Guardamos una copia de las columnas antes de sustituirlas.
        columna_back = [row[posicion] for row in self.BACK]
        columna_up = [row[posicion_inversa] for row in self.UP]
        columna_front = [row[posicion] for row in self.FRONT]
        columna_down = [row[posicion] for row in self.DOWN]

        # Giro correspondiente a L (90º)
        if giro == 90: # 
            cube.UP = copy_column(cube.UP, posicion_inversa, list(reversed(columna_back)))
            cube.FRONT = copy_column(cube.FRONT, posicion, list(reversed(columna_up)))
            cube.DOWN = copy_column(cube.DOWN, posicion, columna_front)
            cube.BACK = copy_column(cube.BACK, posicion, columna_down)
            
            if posicion == 0:
                cube.LEFT = numpy.rot90(cube.LEFT, k=3)
            if posicion == self.posicion_max:
                cube.RIGHT = numpy.rot90(cube.RIGHT, k=3)
        
        # Giro correspondiente a l (-90º)
        elif giro == -90: # 
            cube.UP = copy_column(cube.UP, posicion_inversa, list(reversed(columna_front)))
            cube.FRONT = copy_column(cube.FRONT, posicion, columna_down)
            cube.DOWN = copy_column(cube.DOWN, posicion, columna_back)
            cube.BACK = copy_column(cube.BACK, posicion, list(reversed(columna_up)))
            
            if posicion == 0:
                cube.LEFT = numpy.rot90(cube.LEFT, k=1)
            if posicion == self.posicion_max:
                cube.RIGHT = numpy.rot90(cube.RIGHT, k=1)

        return cube


    def mover_DX(self, posicion, giro):
        """ Función correspondiente al movimiento DX """
        posicion_inversa = self.posicion_max - posicion
        cube = copy.deepcopy(self)

        # Guardamos una copia de las columnas y filas antes de sustituirlas.
        fila_back = list(self.BACK[posicion_inversa])
        columna_left = [row[posicion_inversa] for row in self.LEFT]
        fila_front = list(self.FRONT[posicion])
        columna_right = [row[posicion] for row in self.RIGHT]

        # Giro correspondiente a D (90º)
        if giro == 90: # 
            cube.LEFT = copy_column(cube.LEFT, posicion_inversa, fila_front)
            cube.FRONT = copy_row(cube.FRONT, posicion, list(reversed(columna_right)))
            cube.RIGHT = copy_column(cube.RIGHT, posicion, fila_back)
            cube.BACK = copy_row(cube.BACK, posicion_inversa, list(reversed(columna_left)))
            
            if posicion == 0:
                cube.DOWN = numpy.rot90(cube.DOWN, k=3)
            if posicion == self.posicion_max:
                cube.UP = numpy.rot90(cube.UP, k=3)
        
        # Giro correspondiente a d (-90º)
        elif giro == -90: # 
            cube.LEFT = copy_column(cube.LEFT, posicion_inversa, list(reversed(fila_back)))
            cube.FRONT = copy_row(cube.FRONT, posicion, columna_left)
            cube.RIGHT = copy_column(cube.RIGHT, posicion, list(reversed(fila_front)))
            cube.BACK = copy_row(cube.BACK, posicion_inversa, columna_right)
            
            if posicion == 0:
                cube.DOWN = numpy.rot90(cube.DOWN, k=1)
            if posicion == self.posicion_max:
                cube.UP = numpy.rot90(cube.UP, k=1)

        return cube