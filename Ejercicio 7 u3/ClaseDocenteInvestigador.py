from tkinter.messagebox import NO

from ClaseDocente import Docente
from ClaseInvestigador import Investigador


class DocInvestigador(Docente, Investigador):
    __clases = None
    __cargo = None
    __catedra = None
    __areaInv = None
    __tipoI = None
    __categoria = None
    __impExtra = None

    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad,clases, cargo, catedra, areaInv, tipoI, categoria, impExtra):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__categoria = categoria
        
    
    def mostrardatos(self):
     super().mostrardatos()
     print(self.__categoria)
     print(self.__extra)
    def getcarrera(self):
     return self._carrera
    def getcate(self):
        return self.__categoria
    def gettipo(self):
        return 'Docente Investigador'
    def getextra(self):
        return self.__extra
    def setextra(self,importe):
        self.__extra = importe

    def calcsueldo(self):
        sueldo = Docente.calcsueldo(self)
        sueldo += self.__extra
        return round(sueldo, 2)
    

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocenteInvestigador = dict(
            categoria=self.__categoria,
            extra=self.__extra)
        dic['atributos'].update(atribDocenteInvestigador)
        return dic
    
    
    
    