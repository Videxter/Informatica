import numpy as np
import matplotlib.pyplot as plt
from _ast import Pass
#var_fis = variable fisiologica
#clase contenedora de los objetos tipo estudio y var_fis

class Biblioteca(object):
    
    #Inicializador clase buscador
    def __init__(self,Estudios=(None)):
        #self.estudios atributo de clase buscasdor (Lista)
        self.estudios = Estudios

    #Agrega los objetos tipo estudio al atributo self.estudios 
    """por que aqui?"""
    '''Este es el metodo que agrega los objetos tipo estudio al atributo self.estudio(este es una lista).   
    Si quiere cambiele el nombre para que quede mas intuitivo '''

    def add_library (self,Estudio):
        self.estudios.extend(Estudio)
        print('...Estudio agregado a base de datos ')
    
    #Funcion para buscar en todos los elementos contenidos en self.estudios    
    def buscador (self,key):
        if key in self.estudios or key in sel.estudios.varFis:return True
        else: return False
     
    def menuInicial(self,option):
        opcion = True
        while opcion!=0:
            print ("1. Agregar estudio")
            print ("2. Agregar factor pronostico")
            print ("3. Consultar Estudios")
            print ("4. Consultar Estadisticos de un factor pronostico (Asociados a un estudio)")
            print ('5. Consultar Estadisticos de todos los factores pronostico (Asociados a un estudio)')
            print ('6. Graficar una variable fisiologica asociada a un estudio')
            print ("0. Salir")
            try:    
                opcion = int(input('Ingrese el número de la opción que desea...  '))
            except ValueError:
                print('Ingrese un numero valido')
            if opcion == 1:
                #Ejecuta el inicializador de la clase Estudio
                Estudio.__init__(self)
                
            elif opcion == 2:
                #Ejecuta el inicializador de la clase Var_Fis
                Var_Fis.__init__(self)
                
            elif opcion == 3:
                #Ejecuta la funcion buscar estudios de la clase Estudio
                Estudio.busc_estudios(self)
                
            elif opcion == 4:
                #Ejecuta la funcion buscar un estadistico de un estudio de la clase Var_Fis
                Var_Fis.busc_var_fis_estadisticos_unitario(self)
                
            elif opcion == 5:
                #Ejecuta la funcion buscar todos los estadistico de un estudio de la clase Var_Fis
                Var_Fis.busc_var_fis_estadisticos_todos(self)
                
            elif opcion == 6:
                #Ejecuta la funcion buscar estudios de la clase estudios. Asigna el valor a estudio
                estudio = Estudio.busc_estudios(self)
                #Ejecuta la funcion buscar variable fisiologica asociada a un estudio. Asigna el valor a Variable_Fis
                Variable_Fis = Var_Fis.busc_var_fis(estudio)
                #Utiliza la funcion graficar de la clase Var_Fis. Toma como argumento la variable Variable_Fis 
                Var_Fis.graficar(Variable_Fis)

            
class Estudio(object):
    #Var_Fi (variables fisiologicas)=lista
    def __init__(self,name, patologia, iD,varFis=(None)):
        self.name = name
        self.patologia = patologia
        self.id = iD
        self.var_fi = varFis
        print('...Estudio creado')

        ##ESTO NO VA AQUI, el contructor solo debe crear el objeto estudio, la clase estudio es la que guarda estudios en listas
        '''Ejecuta la funcion add de biblioteca. y guarda ekl objeto tipo estudio en el atributo self.estudio de biblioteca'''
        Buscador.add_busc(self,Estudio)
        
        
    #Agrega las variables fisiologicas al atributo self.var_fi   
    def add_var_fis (self,addVar):
        self.var_fi.extend(addVar)
        print('... Variable agregada a estudio')    
    
    # sobrecarga del metodo contains para usar en el buscador
    def __contains__ (self,key):
        if key in self.name + self.patologia + self.id: return True
        else: return False

class varFisiologica(object):
    
    def __init__(self,name,datos=(None)):
        self.name = name
        self.datos = datos
        #Estadisticos(lista)=contiene los datos estadisticos de la siguiente forma:  Posicion 0: Media. Posicion 1: mediana.Posicion 2: Val max. posicion 3: Val min
        ## arreglar esta linea, se supone que es un diccionario
        self.estadisticValues = {}
        print('...Variable creada')
        #ejecuta la funcion add_var_fis de la clase Estudio
        Estudio.add_var_fis(self, varFisiologica)
    
    def __contains__ (self,key):
        if key in self.name: return True
        else: return False
        
    #Funcion para calcular la media de las variables fisiologicas    
    def calc_media(var_fisica):
        vector_var_fisica = np.array(var_fisica, dtype=np.float)
        media = np.average(vector_var_fisica)
        return media

    #Funcion para calcular la mediana de las variables fisiologicas    
    def calc_mediana(var_fisica):
        vector_var_fisica = np.array(var_fisica, dtype=np.float)
        mediana = np.median(vector_var_fisica)
        return mediana

    #Funcion para calcular el valor maximo de las variables fisiologicas
    def calc_val_max(var_fisica):
        vector_var_fisica = np.array(var_fisica, dtype=np.float)
        val_max = np.argmax(vector_var_fisica)
        return val_max

    #Funcion para calcular el valor minimo de las variables fisiologicas
    def calc_val_min(var_fisica):
        vector_var_fisica = np.array(var_fisica, dtype=np.float)
        val_min = np.argmin(vector_var_fisica)
        return val_min

    # Funcion para graficar. Falta decidir el lugar donde debe ir
    def graficar(var_fisica,):

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
-Relacionar las ultimas funciones con las clases.
-crear funcion para importar las variables fisiologicas.
-crear menu para la ejecucion de todo el algoritmo (en curso)
-Definir buscadores (modificar funciones contain)
-realizar diagrama de clases
'''
