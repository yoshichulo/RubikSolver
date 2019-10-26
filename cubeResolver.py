import json
import copy
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado
from EspacioEstados import EspacioEstados


data_json = json.load(open('cube.json'))
movimientos = ['l3', 'D1', 'l1', 'd0', 'B0', 'b5', 'l2', 'd1']

estado_inicial = Estado(Cube(data_json))

espacio = EspacioEstados('WORK_IN_PROGRESS')

for mov,state,cost in espacio.sucesores(estado_inicial):
    print('({}) {}: {}'.format(cost, mov, state.cube.hash()))
    show_cube(state.cube)