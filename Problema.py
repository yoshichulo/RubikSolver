import heapq
import json
from bisect import bisect_left

from Cube import Cube
from EspacioEstados import EspacioEstados
from Estado import Estado
from Frontera import Frontera
from NodoArbol import NodoArbol


class Problema:

    def __init__(self, path):
        self.espacio = EspacioEstados()
        self.estado_inicial = Estado(Cube(json.load(open(path))))

    def print_solucion(self, n):
        nodos = []
        while n.padre != None:
            nodos.append(n)
            n = n.padre
        nodos.append(n)
        nodos.reverse()
        for n in nodos:
            print("[{}]([{}]{}, c={}, p={}, f={})".format(n.id, n.move, n.state.md5, n.cost, n.d, n.f))

    def es_solucion(self, estado):
        cube = estado.cube
        faces = [cube.BACK, cube.DOWN, cube.FRONT, cube.LEFT, cube.RIGHT, cube.UP]
        for face in faces:
            a = [i for row in face for i in row]
            if len(list(dict.fromkeys(a))) > 1:
                return False
        return True

    def busqueda_acotada(self, estrategia, prof_max):
        frontera = Frontera()
        lista_visitados = []
        solucion = False
        
        n_inicial = NodoArbol(frontera.next_id, 'Estado inicial', None, self.estado_inicial, 0, 0, 0)
        frontera.insertar_nodo(n_inicial)
        frontera.next_id += 1

        while not solucion and not frontera.esta_vacia():
            n_actual = frontera.seleccionar_nodo()[2]
            lista_visitados.append(n_actual.state.md5)

            if self.es_solucion(n_actual.state):
                self.print_solucion(n_actual)
                solucion = True
                
            else:
                l_suc = self.espacio.sucesores(n_actual)
                l_nod = n_actual.crear_lista_nodos(frontera, l_suc, n_actual, prof_max, estrategia)

                if l_nod != None:
                    for n in l_nod:
                        if bisect_left(lista_visitados, n.state.md5):
                            frontera.insertar_nodo(n)
        
        if solucion == False:
            print('No se ha encontrado ninguna solución')