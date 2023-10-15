class Deportista():
    def __init__(self, añosPracticando):
        self._deporte = "Futbol"
        self._añosPracticando = añosPracticando
    def getAñosPracticando(self):
        return self._añosPracticando
    def getDeporte(self):
        return self._deporte
    def setAñosPracticando(self, años):
        self._añosPracticando = años
    def setDeporte(self, d):
        self._deporte = d