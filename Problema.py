import json
import copy
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado
from EspacioEstados import EspacioEstados
from Frontera import Frontera
from NodoArbol import NodoArbol
import time

espacio = EspacioEstados()


cube = Cube(json.load(open('cube.json')))
cube = cube.llamar_movimiento('L1')
cube = cube.llamar_movimiento('B2')
cube = cube.llamar_movimiento('D0')

# Imprime el estado en el que inicia el cubo
show_cube(cube)
estado_inicial = (None, Estado(cube))

def print_solucion(n):
    nodos = []
    while n.padre != None:
        nodos.append(n)
        n = n.padre
    nodos.reverse()
    print('-'.join([nodo.move for nodo in nodos if nodo.move != None]))

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
    n_inicial = NodoArbol(None, None, Estado(cube), 0, 0, 0)
    frontera.insertar(n_inicial)
    solucion = False

    while not solucion and not frontera.esta_vacia():
        n_actual = frontera.seleccionar_nodo()

        if es_solucion(n_actual.state):
            print_solucion(n_actual)
            solucion = True
        else:
            l_suc = espacio.sucesores(n_actual.state)
            l_nod = n_actual.crear_lista_nodos(l_suc, n_actual, prof_max, None)
            for n in l_nod:
                frontera.insertar(n)

busqueda_acotada(None, 5)
