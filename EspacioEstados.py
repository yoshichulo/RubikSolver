from Cube import Cube
from Estado import Estado
from copy import deepcopy

class EspacioEstados:
    def __init__(self, path):
        '''
        States space constructor
        - path: JSON file path
        '''
        self.path = path
    
    def sucesores(self, estado):
        '''
        Function that creates all the possibles successor states given a state.
        It returns a tupple (action, newState, cost), where:
        - action: the movement done
        - newState: the new state of the Cube once the action has been applied
        - cost: the cost of the action (1)
        '''
        movimientos_L = ['L' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['l' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_B = ['B' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['b' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_D = ['D' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['d' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos = movimientos_L + movimientos_B + movimientos_D

        return [(mov, Estado(estado.cube.llamar_movimiento(mov)), 1) for mov in movimientos]