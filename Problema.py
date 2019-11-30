import json
from bisect import bisect_left

from Cube import Cube
from EspacioEstados import EspacioEstados
from Estado import Estado
from Frontera import Frontera
from NodoArbol import NodoArbol


class Problema:
    """
    Esta clase contiene nuestro Problema, que será el encargado de resolver el cubo de Rubikk en función
    de la estrategia elegida.
    """
    def __init__(self, path):
        """ Constructor de la clase Problema """
        self.cube = Cube(json.load(open(path)))
        self.espacio = EspacioEstados()
        self.estado_inicial = Estado(self.cube)

    def print_solucion(self, n): 
        """ Función encargado de imprimir la lista de nodos que llevan a la solución """
        nodos = []
        while n.padre != None:
            nodos.append(n)
            n = n.padre
        nodos.append(n)
        nodos.reverse()
        for n in nodos:
            print("[{}]([{}]{}, c={}, p={}, h={}, f={})".format(n.id, n.move, n.state.md5, n.cost, n.d, round(n.h,2), round(n.f,2)))

    def es_solucion(self, estado):
        """
        Función encargada de comprobar si el estado parámetro es la solución del cubo. 
        Retornara true si es solución y false si no lo es.
        """
        cube = estado.cube
        faces = [cube.BACK, cube.DOWN, cube.FRONT, cube.LEFT, cube.RIGHT, cube.UP]
        for face in faces:
            a = [i for row in face for i in row]
            if len(list(dict.fromkeys(a))) > 1:
                return False
        return True

    def busqueda_acotada(self, estrategia, prof_max):
        """
        Función encargada de encontrar la solución dada una estrategia y una profundidad
        máxima de busqueda.
        """
        frontera = Frontera()
        lista_visitados = set()
        solucion = False
        
        # Creamos el nodo inicial, cuyo estado va a ser el estado inicial del cubo
        n_inicial = NodoArbol(frontera.next_id, 'None', None, self.estado_inicial, 0, 0, 0)
        n_inicial.f = n_inicial.calcular_f(estrategia, n_inicial)
        frontera.insertar_nodo(n_inicial)
        frontera.next_id += 1

        while not solucion and not frontera.esta_vacia():
            n_actual = frontera.seleccionar_nodo()[2]
            lista_visitados.add(n_actual.state.md5)

            if self.es_solucion(n_actual.state):
                self.print_solucion(n_actual)
                solucion = True
                
            else:
                l_suc = self.espacio.sucesores(n_actual)
                l_nod = n_actual.crear_lista_nodos(frontera, l_suc, n_actual, prof_max, estrategia)

                if l_nod != None:
                    for n in l_nod:
                        # Comprobamos si el estado del nodo n ya ha sido visistado
                        if n.state.md5 not in lista_visitados:
                            frontera.insertar_nodo(n)
        
        if solucion == False:
            print('No se ha encontrado ninguna solución')