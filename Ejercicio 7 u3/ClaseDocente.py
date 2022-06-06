from ClasePersonal import Personal
class Docente(Personal):
    __carrera = None
    __cargo = None
    __catedra = None

    def __init__(self, cuil , apellido,nombre,basico, antiguedad ,carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre,basico, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def catedra(self):
        return self.__catedra()

    def mostrardatos(self):
       super().mostrardatos()
       print(self.__carrera)
       print(self.__cargo)
       print(self.__catedra)

    def getcarrera(self):
      self.__carrera

    def gettipo(self):
        return 'Docente'
    @classmethod
    def getporcentajesimple(cls):
        return cls.porcentajesimple
    @classmethod
    def getporcentajesemiexclusivo(cls):
        return cls.porcentajesemiexlusivo
    @classmethod
    def getporcentajeexclusivo(cls):
        return cls.porcentajesemiexlusivo
    
    @classmethod
    def setporcentajesimple(cls,porcentaje):
        cls.porcentajesimple = porcentaje
    @classmethod
    def setporcentajesemi(cls,porcentaje):
        cls.porcentajesemiexlusivo = porcentaje
    @classmethod
    def setporcentajeexclusivo(cls,porcentaje):
        cls.porcentajeexclusivo = porcentaje        
    
    def calcsueldo(self):
     sueldo = float(self._basico) * (1.0 + 0.01 * float(self._antiguedad))
     if self._cargo.lower() == 'simple':
      sueldo += float(Docente.getporcentajesimple()) * float(self._basico)
     elif self._cargo.lower() == 'semiexclusivo':
      sueldo += float(Docente.getporcentajesemiexclusivo()) * float(self._basico)
     else:
      sueldo += float(Docente.getporcentajeexclusivo()) * float(self._basico)
     return round(sueldo, 2)

    def toJSON(self):
        dic = super().toJSON()
        dic['clase'] = self.__class__.__name__
        atribDocente = dict(
            carrera=self._carrera,
            cargo=self._cargo,
            catedra=self._catedra)
        dic['atributos'].update(atribDocente)
        return dic


    