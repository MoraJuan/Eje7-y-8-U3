import abc
from abc import ABC

class Personal(ABC):
    __cuil = None
    __apellido = None
    __nombre = None
    __sueldoB = None
    __antiguedad = None

    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoB = sueldoB
        self.__antiguedad = antiguedad
    
    def getCuil(self):
        return self.__cuil
    
    def getApellidos(self):
        return self.__apellido
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoB(self):
        return self.__sueldoB
    
    def getAntiguedad(self):
        return self.__antiguedad
    

