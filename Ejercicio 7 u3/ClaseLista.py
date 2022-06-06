from ClaseNodo import Nodo
from zope.interface import implementer


class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0

    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato
    
    def InsertarElemento(self, Objeto, Indice):
        try:
            Indice = int(Indice)
            if Indice >= 1 and Indice <= self.__tope:
                miNodo = Nodo(Objeto)
                nodo = self.__cabeza
                i = 1
                while i != Indice:
                    anterior = nodo
                    nodo = nodo.getSiguiente()
                    i += 1
                miNodo.setSiguiente(nodo)
                if Indice == 1:
                    self.__cabeza = miNodo
                    self.__actual = miNodo
                else:
                    anterior.setSiguiente(miNodo)
                self.__tope += 1
                print('Elemento Agregado')
            else:
                print('Posicion fuera de limites')
        except ValueError:
            print('Error: La posicion debe ser un entero')
            




    def agregarPersonal(self, personal):
        nodo = Nodo(personal)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def mostrarElemento(self,indice):
        indice = int(indice)
        if indice > self.__tope:
         print('Error indice mayor al numero de componentes')
        elif indice < 0:
         print('Error indice inaccesible')
        else:
         i = 0
         aux = self.__cabeza
         while i != indice:
          aux = aux.getsiguiente()
          i +=1
         return  aux.getdato()

    def listar(self):
        aux = self.__cabeza
        for x in range(0, self.__tope):
            print('-'*40)
            aux.getdato().mostrar()
            aux = aux.getsiguiente()
    
    def Maximo(self):
        return self.__tope
    
    def cambiarElemento(self,elemento,posicion):
        try:
            posicion = posicion
            if posicion >= 0 and posicion < self.__tope:
                i=0
                nodo = self.__cabeza
                while i != posicion:
                    nodo = nodo.getSiguiente()
                    i+=1
                nodo.setSiguiente(elemento)
            else:
                print('Error: Posicion fuera de los limites de la lista')

        except ValueError:
            print('Error: Posicion fuera de los limites de la lista')

