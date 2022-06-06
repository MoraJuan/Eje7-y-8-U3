from ClaseManejador import Manejador
from ClaseObject import ObjectEncoder
class Menu:
    def __init__(self):
        self.__opcion=0
        self.__Deslpegar = None
    def Desplegar(self):
            print('[1] ')
            print('[2] ')
            print('[3] ')
            print('[4]')
            print('[5]')
            print('[6]')
            print('[7]')
    
    def Opcion(self, Maneja,encoder):
        bande = True
        while bande == True:
            self.Desplegar()
            op = input('ingresar opcion ')
            if op == '1':
                au = Maneja.crearagente()
                print('ingrese indice a colocar')
                ind = int(input())
                Maneja.insertar(au, ind)
            elif op == '2':
                au = Maneja.CrearAgente()
                Maneja.agregar(au)
            elif op == '3':
                Maneja.mostrar()
            elif op == '4':
                print('carreras: LCC,LCI')
                print('ingresar carrera para listar datos')
                care = input()
                Maneja.listadoporcarrera(care)
            elif op == '5':
                Maneja.mostraerareas()
                area = input('ingresar area ')
                Maneja.contararea(area)
            elif op == '6':
                Maneja.listado()
            elif op == '7':
                print('ingrese una categoria (I, II, III, IV o V)')
                cate = input()
                Maneja.categoria(cate)
            elif op == '8':
                listaJSON = Maneja.guardarJSON()
                encoder.guardarJSONArchivo(listaJSON, 'personal.json')
                print('Archivo guardado')
            elif op == '9':
                cuil = input('Ingresar porcentaje ')
                Maneja.modificarPorcentajeporcategoría(cuil)
            elif op.lower() == 'n':
              print('Cerrar menu... volviendo a menu principal')
              bande = False
            else:
                print('opcion incorrecto, vuelva a ingresar opcion')
        print('Fin')