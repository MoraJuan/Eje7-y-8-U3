class Investigador:
    __areaInv = None
    __tipoI = None

    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad, areaInv, tipoI):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__areaInv = areaInv
        self.__tipoI = tipoI

    def mostrardatos(self):
        super().mostrardatos()
        print(self._areaInv)
        print(self.__tipoI)

    def getcarrera(self):
      self.__carrera
    def getarea(self):
        return self.__areaInv

    def gettipo(self):
        return 'Investigador'

    def calcsueldo(self):
        sueldo = self.__basico * (1 + 0.01 * self.__antiguedad)
        return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribInvestigador = dict(
            area = self.__areaInv,
            tipo = self.__tipoI)
        dic['atributos'].update(atribInvestigador)
        return dic
    
