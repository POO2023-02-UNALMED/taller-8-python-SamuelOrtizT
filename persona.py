class Persona(): 
    def __init__(self, nombre, edad, altura, sexo):
        self._nombre = nombre
        self._edad = edad
        self._altura = altura
        self._sexo = sexo
    def getNombre(self):
        return self._nombre
    def getEdad(self):
        return self._edad
    def getAltura(self):
        return self._altura
    def getSexo(self):
        return self._sexo
    def setNombre(self, n):
        self._nombre = n
    def setEdad(self, e):
        self._edad = e
    def setAltura(self, a):
        self._altura = a
    def setSexo(self, s):
        self._sexo = s