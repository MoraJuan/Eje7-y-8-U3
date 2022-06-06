from ClasePersonal import Personal

class PersonalA(Personal):
    __categoria = None
    porcentajeCat1a10 = 10
    porcentajeCat11a20 = 20
    porcentajeCat21a22 = 30

    def __init__(self,cuil, apellido, nombre, sueldoB, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoB, antiguedad)
        self.__categoria = categoria
    
    def getCategoria(self):
        return self.__categoria
    
    def mostrardatos(self):
        super().mostrardatos()
        print(self.__categoria)

    def gettipo(self):
        return 'Personal de apoyo'

    @classmethod
    def getPorcentajeCategoria(cls, op):
        assert isinstance(op, int)
        porcentaje = None
        if op == 1:
            porcentaje = cls.porcentajeCat1a10
        elif op == 2:
            porcentaje = cls.porcentajeCat11a20
        elif op == 3:
            porcentaje = cls.porcentajeCat21a22
        return porcentaje
    @classmethod
    def setPorecentajeCat(cls,op,nuevo):
        assert isinstance(op, int)
        if op == 1:
            cls.porcentajeCat1a10 = int(nuevo)
            print('Porcentaje modificado')
        elif op == 2:
            cls.porcentajeCat11a20 = int(nuevo)
            print('Porcentaje modificado')
        elif op == 3:
            cls.porcentajeCat21a22 = int(nuevo)
            print('Porcentaje modificado')
        else:
            print('opcion incorrecta')

    def calcsueldo(self):
        sueldo = self.getbasico() * (1 + 0.01 * self._antiguedad)
        if self.__categoria >= 1 and self.__categoria <= 10:
            sueldo += self.getbasico() * PersonalA.getPorcentajeCategoria(1)
        elif self.__categoria >= 11 and self.__categoria <= 20:
            sueldo += self.getbasico() * PersonalA.getPorcentajeCategoria(2)
        else:
            sueldo += self.getbasico() * PersonalA.getPorcentajeCategoria(3)
        return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribPersonalApoyo = dict(
            categoria=self.__categoria)
        dic['atributos'].update(atribPersonalApoyo)
        return dic
    
