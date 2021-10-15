class Serie:
    entregado = False
    def __init__(self, numTemp = 3):
        self.__numTemp = numTemp
        self.__titulo = None
        self.__genero = None
        self.__creador = None
        self.entregado = False



    def getTitulo(self):
        return self.__titulo
    def getCreador(self):
        return self.__creador
    def getGenero(self):
        return self.__genero
    def getNumTemo(self):
        return self.__numTemp

    def setNumTemo(self, num):
        self.__numTemp = num

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setGenero(self, genero):
        self.__genero = genero

    def setCreador(self, creador):
        self.__creador = creador

    def entregar(self):
        self.entregado = True



    def __str__(self):
        return 'La serie {} de genero {} y con numTemp = {}, su creador  es {}'.format(self.getTitulo(), self.getGenero(), self.getNumTemo(), self.creador())



class Videjuego:
    entregado = False
    def __init__(self, horas_estimidas = 10):
        self.horas_estimidas = horas_estimidas
        self.__titulo = None
        self.__genero = None
        self.__compañia = None
        self.entregado = False



    def getTitulo(self):
        return self.__titulo
    def getCompañia(self):
        return self.__compañia
    def getGenero(self):
        return self.__genero
    def gethoras_estimidas(self):
        return self.horas_estimidas

    def setTitulo(self, titulo):
        self.__titulo = titulo

    def setGenero(self, genero):
        self.__genero = genero

    def entregar(self):
        self.entregado = True

    def sethoras_estimidas(self, horas):
         self.horas_estimidas = horas


    def __str__(self):
        return 'La serie {} de genero {} y con numTemp = {}, su creador  es {}'.format(self.getTitulo(), self.getGenero(), self.getNumTemo(), self.creador())

listaSeries = []
for i in range(5):
    listaSeries.append(Serie())

listaVideojuego = []
for i in range(5):
    listaVideojuego.append(Videjuego())


listaSeries[0].setNumTemo(66)
listaSeries[0].entregar()

listaVideojuego[0].sethoras_estimidas(100)
listaVideojuego[0].entregar()

contador = 0
for i in listaSeries:
    if i.entregado:
        contador += 1
        print("Series entregadas: " + str(contador))


contador = 0
for i in listaVideojuego:
    if i.entregado:
        contador += 1
        print("Videojuegos entregados: " + str(contador))

listaSerieTemp= []
for i in listaSeries:
    listaSerieTemp.append(i.getNumTemo())


for i in listaSeries:
    if max(listaSerieTemp) == i.getNumTemo():
        print(" la serie con mas numero de temps: " + str(max(listaSerieTemp)))


listaVideojuegoHoras = []
for i in listaVideojuego:
    listaVideojuegoHoras.append(i.gethoras_estimidas())


for i in listaVideojuego:
    if max(listaVideojuegoHoras) == i.gethoras_estimidas():
        print(" El videojuego con mas horas estimados tiene: " + str(max(listaVideojuegoHoras)))
