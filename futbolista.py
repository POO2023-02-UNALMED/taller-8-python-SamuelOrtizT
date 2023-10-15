from deportista import Deportista
from persona import Persona
class Futbolista(Persona, Deportista):
    listaFutbolistas = []
    def __init__(self, nombre, edad, altura, sexo, añosPracticando, golesMarcados, tarjetasRojas, piernaHabil):
        super().__init__(nombre, edad, altura, sexo)
        Deportista.__init__(añosPracticando)
        self._golesMarcados = golesMarcados
        self._tarjetasRojas = tarjetasRojas
        self._piernaHabil = piernaHabil
        Futbolista.listaFutbolistas.append(self)
    def getGolesMarcados(self):
        return self._golesMarcados
    def getTarjetasRojas(self):
        return self._tarjetasRojas
    def getPiernaHabil(self):
        return self._piernaHabil
    def setGolesMarcados(self, g):
        self._golesMarcados = g
    def setTarjetasRojas(self, t):
        self._tarjetasRojas = t
    def setPiernaHabil(self, p):
        self._piernaHabil = p
    def __str__(self):
        return "Mi nombre es" + self.getNombre() + "soy profesional en el deporte" + self.getDeporte() + "Tengo" + str(self.getEdad()) + "años de edad y llevo" + str(self.getAñosPracticando()) + "años en el deporte"