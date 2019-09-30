import json
from rubiktools import show_cube
from Cube import Cube

data_json = json.load(open('cube.json'))
cube = Cube(data_json)


# Hacemos un movimiento
cube.llamar_movimiento('b2')
show_cube(cube)
cube.llamar_movimiento('B2')
show_cube(cube)