class TV:
    __numTV = 0

    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal = 1
        self.__precio = 500
        self.__volumen = 1
        self.__estado = estado  
        self.control = None
        TV._TV__numTV += 1

    def setMarca(self, marca):
        self.__marca = marca

    def getMarca(self):
        return self.__marca
    
    def setCanal(self, canal):
        if self.__estado == True and canal >= 1 and canal <= 120:
            self.__canal = canal

    def getCanal(self):
        return self.__canal
    
    def setPrecio(self, precio):
        self.__precio = precio

    def getPrecio(self):
        return self.__precio
    
    def setVolumen(self, volumen):
        if self.__estado == True and volumen >= 1 and volumen <= 7:
            self.__volumen = volumen

    def getVolumen(self):
        return self.__volumen
    
    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control
    
    def canalUp(self):
        if self.__estado == True and self.__canal < 120:
            self.__canal += 1

        else:
            self.__canal = 1

    def canalDown(self):
        if self.__estado == True and self.__canal > 1:
            self.__canal -= 1

        else:
            self.__canal = 120

    def volumenUp(self):
        if self.__estado == True and self.__volumen < 7:
            self.__volumen += 1

        else:
            pass

    def volumenDown(self):
        if self.__estado == True and self.__volumen > 1:
            self.__volumen -= 1

        else:
            pass

    def turnOn(self):
        self.__estado = True

    def turnOff(self):
        self.__estado = False