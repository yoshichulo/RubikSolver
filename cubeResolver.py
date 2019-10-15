import json
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado
import copy

data_json = json.load(open('cube5.json'))
cube = Cube(data_json)
print(cube.hash())


movimientos = ['l3', 'D1', 'l1', 'd0', 'B0', 'b5', 'l2', 'd1']

for movimiento in movimientos:
    cube = cube.llamar_movimiento(movimiento)
    print(movimiento + ": " + cube.hash())

estado_inicial = Estado(cube)

#estados = estado_inicial.crear_sucesores()
#for estado in estados:
#    show_cube(estado.cube)