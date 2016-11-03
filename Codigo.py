import numpy as np
import matplotlib.pyplot as plt
from _ast import Pass
#var_fis = variable fisiologica
#clase contenedora de los objetos tipo estudio y var_fis

class biblioteca(object):
    
    #Inicializador clase buscador
    def __init__(self,estudios=[]):
        #self.estudios atributo de clase buscasdor (Lista)
        self.estudios = estudios

    #Agrega los objetos tipo estudio al atributo self.estudios 
    """por que aqui?"""
    '''Este es el metodo que agrega los objetos tipo estudio al atributo self.estudio(este es una lista).   
    Si quiere cambiele el nombre para que quede mas intuitivo '''

    def addLib (self,estudio):
        self.estudios.extend(estudio)
        print('...Estudio agregado a base de datos ')
    
    #Funcion para buscar en todos los elementos contenidos en self.estudios     
    def buscador (self,key):
        indice = 0
        resultados = {}
        for objeto in self.estudios:
            if key in self.estudios:
                indice += 1
                resultados[indice] = objeto
                print (indice, ": ",resultados[indice])
        
        if resultados == {}:
            print ("No existe ningun resultado asociado al a palabra clave")
            
            
        return resultados    
                
    def menuInicial(self,option):
        opcion = True
        while opcion!=0:
            print ("1. Agregar estudio")
            print ("2. Agregar factor pronostico")
            print ('3. Mostrar todos los Estudios')
            print ("4. Consultar Estudios")
            print ("5. Consultar Estadisticos de un factor pronostico")
            print ('6. Consultar Estadisticos de todos los factores pronostico')
            print ('7. Consultar por palabra clave')
            print ('8. Graficar una variable fisiologica asociada a un estudio')          
            print ("0. Salir")
            try:    
                opcion = int(input('Ingrese el número de la opción que desea...  '))
            except ValueError:
                print('Ingrese un numero valido')
            if opcion == 1:
                #Ejecuta el inicializador de la clase Estudio
                self.addLib (estudio.__init__(self))
                
            elif opcion == 2:
                #Ejecuta el buscador de estudio y el estudio que elija el usuario es asignado a paciente
                paciente = estudio.busc_estudios(self)
                #Ejecuta el inicializador de la clase Var_Fis
                if paciente == None:
                    print ('Ingrese un estudio existente. (Debe crear un estudio antes de asignarle un diagnostico)')
                else: 
                    while True:                        
                        try:
                            fileName = input('Ingrese el nombre del archivo seguido de .txt  ')
                            datos = varFis.importar(self, fileName)
                            break
                        except IOError:
                            print ('No es posible abrir el archivo.\nVerifique el nombre ingresado.\nEl algoritmo distingue entre mayusculas')
                            continue
                    name_variable_fis = input('Ingrese el nombre de la variable fisiologica: ')
                    estadisticas = varFis.getEstadistics (self, datos) 
                    object_var_fis = varFis.__init__(self, name_variable_fis, datos,estadisticas )
                    estudio.add_var_fis(self, object_var_fis)                 
            
            elif opcion == 3:
                #Ejecuta la funcion buscar estudios de la clase Estudio e imprime todos los objetos tipo estudio
                estudio.busc_estudios(self)
            ''' Esta opcion debe imprimir todos los estudios...'''
                
            elif opcion == 4:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese el nombre del estudio  ')
                #Ejecuta la funcion buscar estudios de la clase Estudio con key como argumento
                busqueda = estudio.busc_estudios(self,key)
                if busqueda == None:
                    print('Debe crear por lo menos un estudio antes de poder buscar')
                
            elif opcion == 5:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese el nombre del factor pronostico o variable fisiologica  ')
                #Ejecuta la funcion buscar un estadistico de un estudio de la clase Var_Fis con key como argumento
                busqueda =
                ''' en esta opcion se debe poder consutar los valores estadisticos de un factor pronostico'''
                if busqueda == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                
            elif opcion == 6:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese el nombre del factor pronostico o variable fisiologica  ')
                #Ejecuta la funcion buscar todos los estadistico de un estudio de la clase Var_Fis
                busqueda = 
                '''En esta opcion se debe poder buscar todos los valores estadisticos de todas las variables fisiologicas asociadas a un estudio '''
                if busqueda == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
            
            elif opcion == 7:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese la palabra clave  ')               
                #ejecuta el buscador por palabra d ela clase biblioteca
                busqueda = biblioteca.buscador(self, key)
                if busqueda == None:
                    print('Debe crear por lo menos un estudio antes de poder buscar')
                
            elif opcion == 8:
                #Ejecuta la funcion buscar estudios de la clase estudios. Asigna el valor a estudio
                input('Ingrese el nombre del estudio donde se encuentra la variable que desea graficar. Luego elija el estudio y la variable fisiologica  ')
                estudio = estudio.busc_estudios(self)
                '''Esta opcion debe poder permitir buscar un factor pronostico para graficarlo'''
                if estudio == None:
                    print('Ingrese un estudio existente. (Debe crear un estudio y asignarle una variable fisiologica para graficar)' )
                else:
  
            
class estudio(object):
    #Var_Fi (variables fisiologicas)=lista
    def __init__(self,name,iD,patologia,varFis=None):
        self.name = name
        self.id = iD
        self.patology = patologia
        self.var_fi = varFis
        print('...Estudio creado')
    
    #Agrega las variables fisiologicas al atributo self.var_fi
    
    def add_var_fis (self,addVar):
        self.var_fi.extend(addVar)
        print('... Variable agregada a estudio')    
    
    # sobrecarga del metodo contains para usar en el buscador
    def __contains__ (self,key):
        if key in self.name + self.patology + self.id: return True
        else: return False

    def __str__(self):
        return '| Nombre: %s | ID: %s | Patologia: %s | Factores pronosticos: %s|'%(self.name.capitalize(), self.id, self.patology.capitalize(), self.var_fi)

class varFis(object):
    def __init__(self,name,datos):
        self.name = name
        self.datos = datos
        #Estadisticos(lista)=contiene los datos estadisticos de la siguiente forma:  Posicion 0: Media. Posicion 1: mediana.Posicion 2: Val max. posicion 3: Val min
        self.estadisticValues = {}
        print('...Variable creada')
    
    def __contains__ (self,key):
        if key in self.name: return True
        else: return False
        
    def importar (self,fileName):
        datos = open(fileName)
        
    def __str__(self):
        estadistics = self.getEstadistics(self.datos)
        return 'Variable Fisiologica:%s\n| Media: %s |\n| Mediana: %s |\n| Valor Maximo: %s |\n| Valor Minimo: %s|\n'
        %(self.name,estadistics['Media'],estadistics['Mediana'],estadistics['Valor maximo'],estadistics['Valor minimo'])
    
    #Funcion para calcular la media de las variables fisiologicas    
    def getEstadistics(self,var_fisica):
        vector_var_fisica = np.array(var_fisica, dtype=np.float) 
        estadisticas = {}
        estadisticas ['Media']=        np.average(vector_var_fisica)
        estadisticas ['Mediana']=      np.median(vector_var_fisica)
        estadisticas ['Valor maximo']= np.argmax(vector_var_fisica)
        estadisticas ['Valor minimo']= np.argmin(vector_var_fisica)
        return estadisticas

    # Funcion para graficar. Falta decidir el lugar donde debe ir
    def graficar(self,var_fisica,):

        #En este bloque obtengo las dos matrices para graficar 
        #(vector_var_fisica   y   segundos_graficar
        vector_var_fisica = np.array(var_fisica, dtype=np.float)
        tamaño = vector_var_fisica.shape
        segundos = tamaño[0]/100
        segundos_graficar = np.zeros((1,tamaño[0]))
        frecuencia = float(segundos/tamaño[0])
        contador = 0
        for i in range(0,tamaño[0]):
            segundos_graficar[i] = contador
            contador = contador + frecuencia

        #En este bloque se ejecutan los comandos para graficar
        plt.title('Comportamiento de variable fisiologica en el tiempo')
        plt.xlabel('Tiempo  [=]Segundos')
        plt.ylabel('Variable fisiologica')
        plt.plot(segundos_graficar,vector_var_fisica)
        plt.show()

'''
PENDIENTES:
-Relacionar las ultimas funciones con las clases.( creo que ya)
-crear menu para la ejecucion de todo el algoritmo (en curso)
-probar buscador (en curso)
-realizar diagrama de clases (en curso)

Hechos:
- constructor, contain, str de estudios funciona
- crear funcion para importar las variables fisiologicas.
'''
