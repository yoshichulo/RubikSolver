import json
import copy
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado
from EspacioEstados import EspacioEstados
from Frontera import Frontera
from NodoArbol import NodoArbol


espacio = EspacioEstados()
estado_inicial = Estado(Cube(json.load(open('cube.json'))))

'''
for mov,state,cost in espacio.sucesores(estado_inicial):
    print('({}) {}: {}'.format(cost, mov, state.cube.hash()))
    show_cube(state.cube)
'''

def es_solucion(estado):
    cube = estado.cube
    faces = [cube.BACK, cube.DOWN, cube.FRONT, cube.LEFT, cube.RIGHT, cube.UP]
    for face in faces:
        a = [i for row in face for i in row]
        if len(list(dict.fromkeys(a))) > 1:
            return False
    return True

def busqueda_acotada(estrategia, prof_max):
    frontera = Frontera()
    n_inicial = NodoArbol(None, estado_inicial, 0, 0, 0)
    frontera.insertar(n_inicial)
    solucion = False

    while not solucion and not frontera.esta_vacia():
        n_actual = frontera.seleccionar_nodo()
        if es_solucion(n_actual.state):
            solucion = True
        else:
            l_suc = espacio.sucesores(n_actual.estado)

