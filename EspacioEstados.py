from Cube import Cube
from Estado import Estado
from copy import deepcopy

class EspacioEstados:
    
    def sucesores(self, nodo):
        '''
        Function that creates all the possibles successor states given a state.
        It returns a tupple (action, newState, cost), where:
        - action: the movement done
        - newState: the new state of the Cube once the action has been applied
        - cost: the cost of the action (1)
        '''
        estado = nodo.state
        movimientos_L = ['L' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['l' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_B = ['B' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['b' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos_D = ['D' + str(i) for i in range(0, estado.cube.posicion_max + 1)] + ['d' + str(i) for i in range(0, estado.cube.posicion_max + 1)]
        movimientos = movimientos_L + movimientos_B + movimientos_D
        
        
        if nodo.move != None:
            movimientos.remove(self.opposite_move(nodo.move))

        return [(mov, Estado(estado.cube.llamar_movimiento(mov))) for mov in movimientos]
    
    def opposite_move(self, move):
        return move.upper() if move.islower() else move.lower()