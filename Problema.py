import json
import copy
from rubiktools import show_cube
from Cube import Cube
from Estado import Estado
from EspacioEstados import EspacioEstados
from Frontera import Frontera
from NodoArbol import NodoArbol
from bisect import bisect_left
import time


espacio = EspacioEstados()

start = time.time()
cube = Cube(json.load(open('cube.json')))
# Imprime el estado en el que inicia el cubo
#show_cube(cube)
estado_inicial = (None, Estado(cube))


def print_solucion(n):
    nodos = []
    while n.padre != None:
        nodos.append(n)
        n = n.padre
    nodos.reverse()
    for n in nodos:
        print("[X]([{}]{}, c={}, p={}, f={})".format(n.move, n.state.md5, n.cost, n.d, n.f))

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
    lista_visitados = []
    solucion = False
    
    n_inicial = NodoArbol(None, None, Estado(cube), 0, 0, 0)
    frontera.frontera.append(n_inicial)

    while not solucion and not frontera.esta_vacia():
        n_actual = frontera.seleccionar_nodo()
        lista_visitados.append(n_actual.state.md5)

        if es_solucion(n_actual.state):
            print_solucion(n_actual)
            solucion = True
            
        else:
            l_suc = espacio.sucesores(n_actual)
            l_nod = n_actual.crear_lista_nodos(l_suc, n_actual, prof_max, estrategia)

            for n in l_nod:
                if bisect_left(lista_visitados, n.state.md5):
                    if estrategia == 1: 
                        frontera.insertarLIFO(n)
                    elif estrategia == 2:
                        frontera.insertarFIFO(n)
                    elif estrategia == 3:
                        frontera.insertarCU(n)

busqueda_acotada(2, 6)
print("Tiempo requerido: " + str(time.time() - start) + " segundos")