import numpy as np
import matplotlib.pyplot as plt
from _ast import Pass
#var_fis = variable fisiologica
#clase contenedora de los objetos tipo estudio y var_fis

class biblioteca(object):
    
    #Inicializador clase buscador
    def __init__(self,estudios=(None)):
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
        if key in self.estudios:return True
        else: return False
     
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
                    variable_fis = Var_Fis.__init__(self)
                    estudio.add_var_fis(self, variable_fis)                 
            
            elif opcion == 3:
                #Ejecuta la funcion buscar estudios de la clase Estudio e imprime todos los objetos tipo estudio
                estudio.busc_estudios(self)
                
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
                busqueda = Var_Fis.busc_var_fis_estadisticos_unitario(self,key)
                if busqueda == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                
            elif opcion == 6:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese el nombre del factor pronostico o variable fisiologica  ')
                #Ejecuta la funcion buscar todos los estadistico de un estudio de la clase Var_Fis
                busqueda = Var_Fis.busc_var_fis_estadisticos_todos(self,key)
                if busqueda == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
            
            elif opcion == 7:
                #Recibe el valor que el usuario desea buscar
                key = input('Ingrese la palabra clave  ')               
                #ejecuta el buscador por palabra d ela clase biblioteca
                busqueda = Biblioteca.buscador(self)
                if busqueda == None:
                    print('Debe crear por lo menos un estudio antes de poder buscar')
                
            elif opcion == 8:
                #Ejecuta la funcion buscar estudios de la clase estudios. Asigna el valor a estudio
                input('Ingrese el nombre del estudio donde se encuentra la variable que desea graficar. Luego elija el estudio y la variable fisiologica  ')
                estudio = Estudio.busc_estudios(self)
                if estudio == None:
                    print('Ingrese un estudio existente. (Debe crear un estudio y asignarle una variable fisiologica para graficar)' )
                else:
                    #Ejecuta la funcion buscar variable fisiologica asociada a un estudio. Asigna el valor a Variable_Fis
                    Variable_Fis = Var_Fis.busc_var_fis(self,estudio)
                    #Utiliza la funcion graficar de la clase Var_Fis. Toma como argumento la variable Variable_Fis 
                    Var_Fis.graficar(self,Variable_Fis)     
            
            
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
    def __init__(self,name,datos=None):
        self.name = name
        self.datos = datos
        #Estadisticos(lista)=contiene los datos estadisticos de la siguiente forma:  Posicion 0: Media. Posicion 1: mediana.Posicion 2: Val max. posicion 3: Val min
        self.estadisticValues = 0
        print('...Variable creada')
        #ejecuta la funcion add_var_fis de la clase Estudio
        Estudio.add_var_fis(self, varFis)   
        
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
