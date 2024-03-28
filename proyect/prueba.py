import os
import random

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_WHITE = '\033[97m'
COLOR_RESET = '\033[0m'  

class Fichas():
    amarillo = []
    azul = []
    rojo = []
    verde = []
    comodin = []

    def __init__(self, color, numero):
        self.numero = numero
        self.color = color

class Player():

    def __init__(self, nombre):
        self.nombre = nombre
        self.fichas = []

    def asignar_fichas(self, repartir_fichas):
        self.fichas = repartir_fichas
        
class mesa():
    def __init__(self, jugadores):
        self.jugadores = jugadores

    def mostrar_fichas(self):
        for jugador in self.jugadores:
            print(f"Fichas de {jugador.nombre}: ", end='')
            if jugador == self.jugadores[0]:
                for ficha in jugador.fichas:
                    mostrar_fichas(ficha)
                print()
            else:
                for ficha in jugador.fichas:
                    print("[?]", end='')
                print()





        

def crear_fichas():
    colores = {
        "amarillo": Fichas.amarillo,
        "azul": Fichas.azul,
        "rojo": Fichas.rojo,
        "verde": Fichas.verde,
        "white": Fichas.comodin,
    }
    for color, arreglo in colores.items():
        if color == "white":
            for x in range(2):
                ficha = Fichas(color, '*')
                arreglo.append(ficha)
        else:
            for i in range(13):
                for j in range(2):
                    ficha = Fichas(color, i + 1)
                    arreglo.append(ficha)

def mostrar_fichas(ficha):

    color = COLOR_RESET
    if ficha.color == "amarillo":
        color = COLOR_YELLOW
    elif ficha.color == "azul":
        color = COLOR_BLUE
    elif ficha.color == "rojo":
        color = COLOR_RED
    elif ficha.color == "verde":
        color = COLOR_GREEN
    elif ficha.color == "comodin":
        color = COLOR_WHITE
    print('[' + color + f"{ficha.numero}" + COLOR_RESET + ']', end='')

def repartir_fichas(n):

    juntar_fichas = sum([Fichas.amarillo, Fichas.azul, Fichas.rojo, Fichas.verde, Fichas.comodin], [])
    random.shuffle(juntar_fichas)

    # Calcular la cantidad de fichas por jugador
    fichas_por_jugador = 14

    # Repartir las fichas a cada jugador
    fichas_repartidas = [juntar_fichas.pop[i * fichas_por_jugador:(i + 1) * fichas_por_jugador] for i in range(n)]
    print("Despues de repartir en el mazo quedan:" + str(len(juntar_fichas)) + "fichas")
    print("Se repartieron:" + str(len(fichas_repartidas)) + "fichas")
    return fichas_repartidas



def main():
    crear_fichas()
    print("Ingrese el numero de jugadores:")
    n = int(input())
    jugadores = [Player(f"Jugador {i+1}") for i in range(n)]
    tablero = mesa(jugadores)
    

    fichas_asignadas = repartir_fichas(n)

    # Asignar las fichas a cada jugador
    for jugador, fichas in zip(jugadores, fichas_asignadas):
        jugador.asignar_fichas(fichas)

    
    tablero.mostrar_fichas()
    
    
    # # Mostrar las fichas de cada jugador
    # for jugador in jugadores:
    #     print(f"Fichas de {jugador.nombre}: ", end='')
    #     for ficha in jugador.fichas:
    #         mostrar_fichas(ficha)
    #     print()  # Agregar un salto de línea después de mostrar las fichas del jugador

if __name__ == "__main__":
    main()
