import  random
from random import choice
class Electrodomestico:

    def __init__(self, color='blanco', preciobase=100, consumo='F', peso=5):
        self.preciobase = preciobase
        self.__color = self.comprobarColor(color)
        self.__consumo = self.comprobarConsumoEnergetico(consumo)
        self.peso = peso


    def getprecio(self):
        return self.preciobase

    def getcolor(self):
        return self.color

    def getconsumo(self):
        return self.consumo

    def getpeso(self):
        return self.peso

    def comprobarConsumoEnergetico(self, letra):
        upperConsumo = letra.upper()
        listaConsumo = ['A', 'B', 'C', 'D', 'E', 'F']

        if upperConsumo in listaConsumo:
            return upperConsumo

        else:
            return 'F'


    def comprobarColor(self, color):
        lowerColor = color.lower()
        listaColor = ['blanco', 'negro', 'rojo', 'azul']
        if lowerColor in listaColor:
            return lowerColor
        else:
            return "blanco"


    def precioFinal(self):
        if self.getconsumo() == 'A':
            precioConsumo = 100

        elif self.getconsumo() == 'B':
            precioConsumo = 80

        elif self.getconsumo() == 'C':
            precioConsumo = 60

        elif self.getconsumo() == 'D':
            precioConsumo = 50

        elif self.getconsumo() == 'E':
            precioConsumo = 30

        else:
            precioConsumo = 10

        if 0 < self.getpeso() < 19:
            precioPeso = 10

        elif 20 < self.getpeso() < 49:
            precioPeso = 50

        elif 50 < self.getpeso() < 79:
            precioPeso = 80

        elif self.peso > 80:
            precioPeso = 100

        return precioPeso + precioConsumo


class Lavadora(Electrodomestico):

    def __init__(self, carga = 5, color='blanco', preciobase=100, consumo='F', peso=5):
        super().__init__(color, preciobase, consumo, peso)
        self.carga = carga


    def getCarga(self):
        return self.carga

    def precioFinal(self):
        if self.carga > 30:
            self.peso += 50


class Television(Electrodomestico):

    def __init__(self,  color='blanco', preciobase=100, consumo='F', peso=5  ):
        Electrodomestico.__init__(self, color, preciobase, consumo, peso)

        self.resolucion = 40
        self.fourK = False
        self.resolucion = 20

    def precioFinal(self):
        if self.resolucion > (self.preciobase + (self.preciobase*0.3)):
            self.preciobase += 50
        if self.fourK:
            self.preciobase += 50


listaPrecio = [44,77,54,700,456,345,678,321,77,22,12]
listaElec = [Lavadora(preciobase = choice(listaPrecio)), Television(preciobase = choice(listaPrecio))]
lista =  []
for elect in range(10):
    lista.append(choice(listaElec))


for clase in lista:
    clase.precioFinal()
    print(clase.getprecio())

l = Lavadora()