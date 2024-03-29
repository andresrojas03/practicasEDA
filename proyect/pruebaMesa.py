import random

COLOR_RED = '\033[91m'
COLOR_GREEN = '\033[92m'
COLOR_YELLOW = '\033[93m'
COLOR_BLUE = '\033[94m'
COLOR_WHITE = '\033[97m'
COLOR_RESET = '\033[0m'
fichas_jugador = 14
nJugadores = 2


class fichas():
    #crear mazos de los distintos colores y los comodines 
    amarillo =  []
    azul = []
    rojo = []
    verde = []
    comodin = []
    def __init__(self, numero, color):
        self.numero = numero
        self.color = color
        # self.deck = [] #el mazo de todas las piezas que se va a llenar despues de haber mezclado las fichas

    # def llenar_deck(self):
    #     return self.deck
    
    # def agregar_ficha(self, ficha):
    #     self.deck.append(ficha)
    
    # def mostrar_deck(self):
    #     for ficha in self.deck:
    #         print(f"Ficha: {ficha.numero} de color {ficha.color}")

    # def mostrar_deck(self):
    #     print("Mazo de fichas:")
    #     for ficha in self.deck:
    #         color = COLOR_RESET
    #         if ficha.color == "amarillo":
    #             color = COLOR_YELLOW
    #         elif ficha.color == "azul":
    #             color = COLOR_BLUE
    #         elif ficha.color == "rojo":
    #             color = COLOR_RED
    #         elif ficha.color == "verde":
    #             color = COLOR_GREEN
    #         elif ficha.color == "comodin":
    #             color = COLOR_WHITE
    #         print('[' + color + f"{ficha.numero}" + COLOR_RESET + ']', end=' ')
    #     print()

    
class jugador():

    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.jugadas = []

    def llenar_mano(self):
        return self.mano
    
    def mostrar_mano(self, fichas):
        for ficha in fichas:
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

    def mostrar_jugadas(self, fichas):
        #para mostrar las jugadas que tiene el jugador 
        #usar esta funcion en la clase mesa para mostrar las jugadas de todos los players
        print("Tu(s) jugadas:")
        for ficha in fichas:
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
        print()
        
    def comer(self, ficha):
        print(f"Has agarrado la ficha {ficha[-1].numero} de color {ficha[-1].color}")
        print(f"Quedan: {len(ficha)} fichas en el pozo")
        self.mano.append(ficha.pop())
    
    def armar_jugada(self, pozo):
        tomar = True
        #bucle por si el jugador necesita tomar mas de una ficha
        while tomar:
            print("Tu mano:")
            self.mostrar_mano(self.mano)
            print()
            take = int(input("Desea agarrar una ficha? 1.Si 2.No"))
            if take == 1:
                self.comer(pozo)
            elif take == 2:
                break

        print("Seleccione al menos 3 fichas de su mano de juego:")
        jugada = []
        
        while len(jugada) < 3 or len(jugada)< 14:
            # Solicitar al jugador que ingrese el índice de la ficha
            print("Tu mano:")
            self.mostrar_mano(self.mano)
            print()
            while True:
                try:
                    indice = int(input("Ingrese el índice de la ficha: ")) - 1  # Restar 1 para ajustar al índice base 0
                    if 0 <= indice < len(self.mano):
                        break
                    else:
                        print("Índice fuera de rango. Inténtelo de nuevo.")
                except ValueError:
                    print("Entrada no válida. Inténtelo de nuevo.")
            
            # Obtener la ficha seleccionada por el jugador y agregarla a la lista de fichas seleccionadas
            ficha_seleccionada = self.mano.pop(indice)
            jugada.append(ficha_seleccionada)
            print(f"Ha seleccionado la ficha [{ficha_seleccionada.color} {ficha_seleccionada.numero}]")
            if len(jugada) >= 3:
                comprobacion = input("Deseas agregar mas fichas a tu jugada? 1.Si 2.No")
                if comprobacion == "1":
                    pass
                elif comprobacion == "2":
                    return jugada
        
    def validar_jugada(self, jugada):
        if len(jugada) < 3:
            print("Jugada inválida: Se requieren al menos 3 fichas.")
            return False
        
        # Comprobación de secuencia ascendente
        if all(jugada[i].numero == jugada[i+1].numero - 1 and jugada[i].color == jugada[i+1].color for i in range(len(jugada) - 1)):
            while jugada:
                ag_jugada = jugada.pop()
                self.jugadas.append(ag_jugada)
            self.mostrar_jugadas(self.jugadas)
            return True
        
        # Comprobación de secuencia descendente
        if all(jugada[i].numero == jugada[i+1].numero + 1 and jugada[i].color == jugada[i+1].color for i in range(len(jugada) - 1)):
            while jugada:
                ag_jugada = jugada.pop()
                self.jugadas.append(ag_jugada)
            self.mostrar_jugadas(self.jugadas)
            return True
        
        # Comprobación de grupo de colores diferentes con el mismo número
        if all(jugada[i].numero == jugada[i+1].numero and jugada[i].color != jugada[i+1].color for i in range(len(jugada) - 1)):
            while jugada:
                ag_jugada = jugada.pop()
                self.jugadas.append(ag_jugada)
            self.mostrar_jugadas(self.jugadas)
            return True
        
        # Comprobación de grupo de números diferentes con el mismo color
        if all(jugada[i].color == jugada[i+1].color and jugada[i].numero != jugada[i+1].numero for i in range(len(jugada) - 1)):
            #bucle para vaciar el arreglo "jugada" dentro del arreglo de jugadas del player
            while jugada:
                ag_jugada = jugada.pop()
                self.jugadas.append(ag_jugada)
            self.mostrar_jugadas(self.jugadas)
            return True
        
        print("Jugada inválida: Las fichas no forman una secuencia o grupo válido.")
        print("Regresando fichas a su mano")
        while jugada:
            reg = jugada.pop()
            self.mano.append(reg)
        return False

    def ganar(self):
        if len(self.mano) != 0:
            return False
        elif len(self.mano) == 0:
            print("El jugador ha ganado")
            return True     
     
class mesa():
    def __init__(self, jugadores):
        self.jugadores = jugadores#un arreglo con los jugadores en la mesa
        # self.jugadas = jugadas #arreglo con las jugadas de cada jugador
    def mostrar_jugadores(self):
        print("Jugadores activos en la mesa:")
        for jugador in self.jugadores:
            print(f"{jugador.nombre} ", end='')
        print()
    
def crear_fichas():
    print("Creando las fichas...")
    #creando un diccionario con los colores para asignarlos
    colores = {
        "amarillo": fichas.amarillo,
        "azul": fichas.azul,
        "rojo": fichas.rojo,
        "verde": fichas.verde,
        "comodin": fichas.comodin,
    }
    #creando las fichas y asignandolas en su arreglo
    for color, arreglo in colores.items():
        if color == "comodin":
            for x in range(2):
                ficha = fichas("*", color)
                arreglo.append(ficha)
        else:
            for i in range(13):
                for j in range(2):
                    ficha = fichas(i + 1, color)
                    arreglo.append(ficha)

def crear_jugadores(num_jugadores):
    nombre_jugador = [f"Jugador{i+1}" for i in range(num_jugadores)]
    jugadores = [jugador(nombre) for nombre in nombre_jugador]
    return jugadores

def mezclar_fichas(n,jugadores):
    pozo = sum([fichas.amarillo, fichas.azul, fichas.rojo, fichas.verde, fichas.comodin], []) #este es el pozo de las fichas
    random.shuffle(pozo)
    
    #para llenar el arreglo del jugador con sus fichas
    for j in range(n):
        mano_jugador = jugadores[j].llenar_mano() #llamando el arreglo del jugador
        for i in range(fichas_jugador):
            ficha = pozo.pop()
            mano_jugador.append(ficha) #llenando la mano del jugador


    return pozo
       
def main():
    crear_fichas()
    
    jugadores = crear_jugadores(nJugadores)
    
    # Llenar el deck con la función mezclar_fichas()
    pozo = mezclar_fichas(nJugadores, jugadores)
    
    table= mesa(jugadores)

    

    print(f"En el pozo hay: {len(pozo)} fichas")
    #mostrar el contenido hasta que el jugador gane
    while not jugadores[0].ganar():
        table.mostrar_jugadores()
        #pruebas con el jugador 1
        play = jugadores[0].armar_jugada(pozo)
        jugadores[0].validar_jugada(play)
    

    
    
    #jugadores[0].mostrar_mano(jugadores[0].mano)
    # for i in range(3):
    #     jugadores[0].mano.pop()




    # print("El jugador1 va a comer")
    # jugadores[0].comer(pozo.pop())
    # jugadores[0].mostrar_mano(jugadores[0].mano)
    
    


if __name__ == "__main__": 
    main()
