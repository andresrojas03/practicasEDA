class paises : 
    def __init__(self, nombre,moneda,capital):
        self.nombre = nombre
        self.moneda = moneda
        self.idiomas = []
        self.ciudadesFamosas = []
        self.capital = capital

    def agregarIdioma(self,idiomas):
        self.idiomas.append(idiomas)

    def agregarCiudades(self,ciudadesFamosas):
        self.ciudadesFamosas.append(ciudadesFamosas)

    def imprimir(self):
        print("El pais es: ", self.nombre)
        print("La moneda es: ", self.moneda)
        for y in range (0,2):
            print("Los idiomas del pais son: ", self.idiomas[y])
        for x in range (0,3):
            print("Las ciudades famosas del pais son: ", self.ciudadesFamosas[x])
        print("La capital del pais es: ", self.capital)

def llenarPaises(paises):
    pais = paises('','','')
    pais.nombre = input(f"Ingrese el nombre de su pais: ")
    pais.moneda = input(f"Ingrese la moneda de su pais: ")
    #llenar la lista de idiomas
    for i in range(0,2):
        pais.agregarIdioma(input(f"Ingrese el idioma de su pais: "))
    #llenar la lista de ciudades
    for j in range(0,3):
        pais.agregarCiudades(input(f"Ingrese las ciudades mas famosas de su pais empezando por la capital: "))
    pais.capital = pais.ciudadesFamosas[0]

    pais.imprimir()

llenarPaises(paises)
