from ClaseLista import Lista
from ClaseDocente import Docente
from ClaseDocenteInvestigador import DocInvestigador
from ClaseInvestigador import Investigador
from ClaseObject import ObjectEncoder
from ClasePersonal import Personal
from ClasesPersonalApoyo import PersonalA
from ClaseDirector import IDirector
from ClaseTesorero import ITesorero
from zope.interface import implementer
@implementer(IDirector)
@implementer(ITesorero)
class Manejador:
    __lista = None

    def __init__(self):
        self.__lista = Lista()

    def LLenar(self, Lista):
        for i in range(len(Lista)):
            xlista = Lista[i]
            class_name = xlista.pop('clase')
            class_=eval(class_name)
            atributos = xlista['atributos']
            UnObjeto = class_(**atributos)
            self.__lista.agregarPersonal(UnObjeto)
      
    
    def mostrar(self):
        Indice=input('Ingrese indice:')
        a = self.__lista.mostrarElemento(Indice)
        if isinstance(a, Docente):
            print('-[Es Docente]')
        if isinstance(a, Investigador):
            print('-[Es Investigador]')
        if isinstance(a, DocInvestigador):
            print('-[Es DocInvestigador]')
        if isinstance(a, PersonalA):
            print('-[Es Personal de Apoyo]')
    

    def Agregar(self, agente):
        if isinstance(agente, Personal):
            self.__lista.agregarPersonal(agente)
        else:
            print('NO se pudo AGREGAR')


    
    def Insetar(self, agente, Indice):
        if isinstance(agente, Personal):
            self.__lista.insertarElemento(agente, Indice)
        else:
            print('Error: no se puede agregar')
    

    def CrearAgente(self):
        print('--INGRESE DATOS DE AGENTE--')
        cuil = input('CUIL: ')
        apellido = input('APELLIDO: ')
        nombre = input('NOMBRE: ')
        basico = input('BASICO: ')
        antiguedad = input('ANTIGUEDAD: ')
        band= True
        while band == True:
            print('Eliga tipo de AGENTE')
            opcion = input('[1]- DOCENTE // [2]-INVESTIGADOR // [3]-iNVESTIGADOR DOCENTE // [4]-APOYO')
            if opcion == '1':
                carrera = input('CARRERA:')
                cargo = input('CARGO:')
                catedra = input('CATEDRA:')
                agente = Docente(cuil, apellido, nombre, basico, antiguedad,carrera,cargo,catedra)
                band = False
            elif opcion == '2':
                area = input('Area:')
                tipo = input('Tipo:')
                agente = Docente(cuil, apellido, nombre, basico, antiguedad, area, tipo)

            elif opcion =='3':
                categoria = input('CATEGORIA:')
                extra = input('Extra:')
                agente = Docente(cuil, apellido, nombre, basico, antiguedad, categoria, extra)

            elif opcion =='4':
                categoria = input('CATEGORIA:')
                agente = Docente(cuil, apellido, nombre, basico, antiguedad, categoria)

            else:
                print('Opcion Incorrecta')
                opcion = input(' 1- Docente, 2-Investigador, 3 Investigador Docente, 4-Apoyo') 
            return agente
    def ordenar(self):
        cota = self.__lista.max() - 1
        k = 1
        while k != -1:
            k = -1
            for i in range(cota):
                agente1 = self.__lista.mostrarElemento(i)
                agente2 = self.__lista.mostrarElemento(i + 1)
                dato1 = agente1.getApellido()
                dato2 = agente2.getApellido()
                if dato1 > dato2:
                    self.__lista.cambiarelemento(agente2, i)
                    self.__lista.cambiarelemento(agente1, i + 1)
                    k = i
            cota = k
    def mostraerareas(self):
        areas = []
        for agente in self.__lista:
            if isinstance(agente, Investigador):
                area = agente.getarea()
                if area not in areas:
                    areas.append(area)
        print('-'*50)
        for area in areas:
            print(area)
    def contararea(self,area):
        invest=0
        doceninv=0
        for agente in self.__lista:
            if isinstance(agente, Investigador):
                if agente.getarea() == area:
                 invest =1+invest
            if isinstance(agente,DocInvestigador):
                if agente.getarea() == area:
                    doceninv =1+doceninv
        print('cantidad de investigadores en esta area: ' + str(invest-doceninv))
        print('cantidad de docentes investigadores en esta area: ' + str(doceninv))

    def listado(self):
        self.ordenar()
        for agente in self.__lista:
         print('-'*50)
         print(agente.getNombre())
         print(agente.getApellido())
         print(agente.gettipo())
         print(agente.calcsueldo())
    def categoria(self,cate):
        importe = 0
        for agente in self.__lista:
          if isinstance(agente, DocInvestigador):
              if agente.getcate().lower() == cate.lower():
                  print('-'*50)
                  print(agente.getApellido())
                  print(agente.getNombre())
                  print(agente.getextra())
                  importe+=agente.getextra()
        print(' total de dinero que la Secretaría de Investigación debe solicitar al Ministerio: '+ str(importe))

    
    def guardarJSON(self):
        listaJSON = [agente.toJSON() for agente in self.__lista]
        return listaJSON
    
        
