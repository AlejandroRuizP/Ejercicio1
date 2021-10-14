
import random
class Persona:
    def __init__(self, nombre = '', edad = 0, dni = '', sexo = 'H', peso = 0, altura = 1):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura
        self.__dni = self.generarDNI()


    def getnombre(self):
        return self.__nombre

    def getedad(self):
        return self.__edad

    def getpeso(self):
        return self.__peso

    def getaltura(self):
        return self.__altura

    def getasexo(self):
        return self.__sexo

    def getdni(self):
        return self.__dni



    def setnombre(self, nombre):
        self.__nombre = nombre


    def setedad(self, edad):
        self.__edad = edad

    def setsexo(self, sexo):
        self.__sexo = sexo

    def setpeso(self, peso):
        self.__peso = peso

    def setaltura(self, altura):
        self.__altura = altura


    def calcularIMC(self):



        imc = self.getpeso() / (self.getaltura() ** 2)

        if imc <= 18.5:
            resultado = -1
        elif 18.5 < imc < 24.9:
            resultado = 0
        elif imc > 25.9:
            resultado = 1


        return 'El IMC es: {} y con un valor de: {}'.format(round(imc, 2), resultado)


    def esMayorEdad(self):

        return self.getedad() > 18


    def introducirSexo(self, sexo):
        if sexo != 'M' or sexo != 'H':
            self.__sexo = 'M'
        else:
            self.__sexo = sexo


    def toString(self):
        string = '{} con una edad de {}, pesa: {} y mide: {}'.format(self.getnombre(), self.getedad(), self.getpeso(), self.getaltura())

        return string



    def generarDNI(self):
        numeros = random.randint(11111111, 99999999)
        resto = numeros % 23

        if resto == 0:
            letra = 'T'

        elif resto == 1:
            letra = 'R'
        elif resto == 2:
            letra = 'W'
        elif resto == 3:
            letra = 'A'
        elif resto == 4:
            letra = 'G'
        elif resto == 5:
            letra = 'M'
        elif resto == 6:
            letra = 'Y'
        elif resto == 7:
            letra = 'P'
        elif resto == 8:
            letra = 'D'
        elif resto == 9:
            letra = 'X'
        elif resto == 10:
            letra = 'B'
        elif resto == 11:
            letra = 'N'
        elif resto == 12:
            letra = 'J'
        elif resto == 13:
            letra = 'Z'
        elif resto == 14:
            letra = 'S'
        elif resto == 15:
            letra = 'Q'
        elif resto == 16:
            letra = 'V'
        elif resto == 17:
            letra = 'V'
        elif resto == 18:
            letra = 'H'
        elif resto == 19:
            letra = 'L'
        elif resto == 20:
            letra = 'C'
        elif resto == 21:
            letra = 'K'
        elif resto == 22:
            letra = 'E'


        return str(numeros) + letra














"""
nombre = input("Introduce el nombre de la persona: ")
edad = int(input("Introduce la edad de la persona: "))
sexo = input("Introduce el sexo de la persona: ")
peso = int(input("Introduce el peso de la persona: "))
altura = int(input("Introduce la altura de la persona: "))
"""
nombre = "alex"
edad =  23
sexo = "M"
peso = 65
altura = 1.70

p = Persona(peso = 64, altura= 1.70)

p1 = Persona(nombre, edad, sexo, peso, altura)
p2 = Persona(nombre, edad, sexo)
p3 = Persona()

p3.setnombre("Pepe")
p3.setedad(22)
p3.setsexo("M")
p3.setpeso(80)
p3.setaltura(1.90)

print(p1.calcularIMC())
print(p2.calcularIMC())
print(p3.calcularIMC())

print(p1.esMayorEdad())
print(p2.esMayorEdad())
print(p3.esMayorEdad())

print(p1.toString())
print(p2.toString())
print(p3.toString())













