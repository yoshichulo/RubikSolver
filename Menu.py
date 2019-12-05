from Problema import Problema
import os.path
import time

banner = ''' _____       _         ______                _                
/  __ \     | |        | ___ \              | |               
| /  \/_   _| |__   ___| |_/ /___  ___  ___ | |_   _____ _ __ 
| |   | | | | '_ \ / _ \    // _ \/ __|/ _ \| \ \ / / _ \ '__|
| \__/\ |_| | |_) |  __/ |\ \  __/\__ \ (_) | |\ V /  __/ |   
 \____/\__,_|_.__/ \___\_| \_\___||___/\___/|_| \_/ \___|_|   
                                                              '''
estrategias = ['Anchura', 'Profundidad', 'Coste Uniforme', 'Voraz', 'A*']


def selectPath():
    while True:
        path = input("Introduzca la ruta del archivo .json que contiene el cubo> ")
        if (os.path.exists(path)):
            return path
        else:
            print("La ruta del fichero que ha introducido no es válida.")


def selectStrat():
    while True:
        estrategia = int(input("Introduzca el número de la estrategia a utilizar para resolver el cubo:\n1. Anchura.\n2. Profundidad.\n3. Coste uniforme.\n4. Voraz.\n5. A*.\n> "))
        if (estrategia in [1, 2, 3, 4, 5]):
            return estrategia
        else:
            print("Debe introducir el número correspondiente a una de las opciones.")


def selectProf():
    while True:
        profundidad = input("Introduzca la profundidad> ")
        if (profundidad.isnumeric()):
            return int(profundidad)
        else:
            print("Debe introducir el número correspondiente a la máxima profundidad del problema.")


def menuStart():
    print(banner)
    path = selectPath()
    strat = selectStrat()
    prof = selectProf()
    buscando = "\nSe están calculando los movimientos necesarios para resolver el cubo.\nEstrategia: {}\tProfundidad: {}\n".format(estrategias[strat-1], prof)
    start = time.time()

    print(buscando)
    p = Problema(path)
    p.busqueda_acotada(strat, prof)
    print("---------------------------------------\nTiempo requerido: " +
          str(time.time() - start) + " segundos")


if __name__ == '__main__':
    menuStart()
