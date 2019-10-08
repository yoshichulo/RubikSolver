import json
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado

data_json = json.load(open('cube.json'))
cube = Cube(data_json)


estado_inicial = Estado(cube)

estados = estado_inicial.crear_sucesores()
for estado in estados:
    show_cube(estado.cube)