class TV:
    __numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._canal = 1
        self._precio = 500
        self._volumen = 1
        self._estado = estado  
        self.control = None
        TV._TV__numTV += 1

    def setMarca(self, marca):
        self._marca = marca

    def getMarca(self):
        return self._marca
    
    def setCanal(self, canal):
        if self._estado == True and canal >= 1 and canal <= 120:
            self._canal = canal

        else:
            pass

    def getCanal(self):
        return self._canal
    
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio
    
    def setVolumen(self, volumen):
        if self._estado == True and volumen >= 1 and volumen <= 7:
            self._volumen = volumen
        else:
            pass

    def getVolumen(self):
        return self._volumen
    
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
    
    def canalUp(self):
        if self._estado == True and self._canal < 120:
            self._canal += 1

        else:
            pass

    def canalDown(self):
        if self._estado == True and self._canal > 1:
            self._canal -= 1

        else:
            pass

    def volumenUp(self):
        if self._estado == True and self._volumen < 7:
            self._volumen += 1

        else:
            pass

    def volumenDown(self):
        if self._estado == True and self._volumen >= 1:
            self._volumen -= 1

        else:
            pass

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def getEstado(self):
        return self._estado
    
    @classmethod
    def setNumTV(self, numTV):
        TV._TV__numTV = numTV

    @classmethod
    def getNumTV(self):
        return TV._TV__numTV