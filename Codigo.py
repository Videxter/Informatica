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

    def addLib (self,object_estudio):
        self.estudios.append(object_estudio)
        print('...Estudio agregado a base de datos ')
    
    def showVarfis(self):
        pass    
    
    #Funcion para buscar en todos los elementos contenidos en self.estudios     
    def buscador (self,key):
        indice = 0
        resultados = {}
        for objeto in self.estudios:
            if key in objeto or key in objeto.varfi:
                indice += 1
                resultados[indice] = objeto
                print (indice, ": ",resultados[indice])
        opind = str(input('Seleccione el numero del estudio  '))
        print (resultados[opind])
        if resultados == {}:
            print ("No existe ningun resultado asociado a la palabra clave")
            resultados = None   
        
        return resultados[opind]
    
    def showLibrary(self):
        if not self.estudios == []:
            for i in self.estudios:
                #ejecuta el str de estudio
                print (i)
                
    def menuInicial(self):
        opcion = True
        while opcion!=0:
            print ("1. Agregar estudio")
            print ("2. Agregar factor pronostico")
            print ('3. Mostrar todos los Estudios')
            print ("4. Consultar Estudios")
            print ("5. Consultar Estadisticos de un factor pronostico")
            print ('6. Consultar Estadisticos de todos los factores pronostico')
            print ('7. Graficar una variable fisiologica asociada a un estudio')          
            print ("0. Salir")
            try:    
                opcion = int(input('Ingrese el número de la opción que desea...  '))
            except ValueError:
                print('Ingrese un numero valido')
            if opcion == 1:
                #Ejecuta el inicializador de la clase Estudio
                name = str(input('Ingrse nombre  ')) 
                ide = str(input('Ingrse Identificación  '))
                pat = str(input('Ingrse patlogia  '))
                self.addLib (estudio(name, ide, pat))
                
            elif opcion == 2:
                key = str(input('Ingrese el nombre del estudio al que desea asociarle la viariable fisiologica'))
                study = self.buscador(key)
                if study == None:
                    print ('Ingrese un estudio existente. (Debe crear un estudio antes de asignarle un diagnostico)')
                    continue
                else: 
                    while True:                        
                        try:
                            file = open(str(input('Ingrese el nombre del archivo seguido de .txt  ')))
                            break
                        except IOError:
                            print ('No es posible abrir el archivo.\nVerifique el nombre ingresado.\nEl algoritmo distingue entre mayusculas')
                            continue
                    variableFis = str(input('Ingrese el nombre de la variable fisiologica: ')) 
                    objectVarFis = varFis(variableFis, file)
                    study.addVarFis(objectVarFis)                 
            
            elif opcion == 3:
                #Ejecuta la funcion buscar estudios de la clase Estudio e imprime todos los objetos tipo estudio
                self.showLibrary()                
            
            elif opcion == 4:
                #Recibe el valor que el usuario desea buscar
                key = str(input('Ingrese el nombre del estudio  '))
                #Ejecuta la funcion buscar estudios de la clase Estudio con key como argumento
                study = self.buscador(key)
                if study == None:
                    print('Debe crear por lo menos un estudio antes de poder buscar')
                    continue
                
            elif opcion == 5:
                #Recibe el valor que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio'))
                study = self.buscador(key)

                if study == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                    continue
                else:
                    print ( study.buscadorvarfis())

            elif opcion == 6:
                #Recibe el valor que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio  '))
                #Ejecuta la funcion buscar todos los estadistico de un estudio de la clase Var_Fis

                if study == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                    continue
                
                else:
                    study = self.buscador(key) 
                    study.showallvarfis()

                    
            elif opcion == 7:
                #Recibe el valor que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio'))
                study = self.buscador(key)
                if study == None:
                    print('Ingrese un estudio existente. (Debe crear un estudio y asignarle una variable fisiologica para graficar)' )
                    continue
                else:
                    key2 = study.buscadorvarfis()                
                    key2.graficar()
                        
                    
class estudio(object):
    #Var_Fi (variables fisiologicas)=lista
    def __init__(self,name,iD,patologia,varFi=[]):
        self.name = name
        self.id = iD
        self.patology = patologia
        self.varfi = varFi
        print('...Estudio creado')
    
    #Agrega las variables fisiologicas al atributo self.var_fi
    ##### PROBAR (DEBERIA VAR SER UN DICCIONARIO?)
    def addVarFis (self, object_variable_fisiologica):
        self.varfi.append(object_variable_fisiologica)
        print('... Variable agregada a estudio')
        return self.varfi
    
    # sobrecarga del metodo contains para usar en el buscador
    def __contains__ (self,key):
        if (key in self.name + self.patology + self.id) or (key in self.varfi): return True
        else: return False
    
    # sobrecarga de str #### 
    def __str__(self):
        return '| Nombre: %s | ID: %s | Patologia: %s | Factores pronosticos: %s|'%(self.name.capitalize(), self.id, self.patology.capitalize(), self.namesVarfi())

    def namesVarfi(self):
        listvf = []
        for i in self.varfi:
            listvf.append(i.name)
        return listvf
    
    def buscadorvarfis (self,key):
        indice = 0
        resultados = {}
        for objeto in self.varfi:
            if key in objeto:
                indice += 1
                resultados[indice] = objeto
                print (indice, ": ",resultados[indice])
        opcionvarfi = str(input('Seleccione el numero de la variable fisiologica  '))
       
        if resultados == {}:
            print ("No existe ningun resultado asociado a la palabra clave")
            resultados = None   
        return resultados[opcionvarfi]
        
    def showallvarfis(self):
        if not self.varfi == []:
            for i in self.varfi:
                #ejecuta el str de estudio
                print (i)


class varFis(object):
    def __init__(self,name, datos, dic = {} ):
        self.name = name
        self.datos = np.loadtxt(datos)
        #Estadisticos(lista)=contiene los datos estadisticos de la siguiente forma:  Posicion 0: Media. Posicion 1: mediana.Posicion 2: Val max. posicion 3: Val min
        self.estadisticValues = dic
        print('...Variable creada')
    
    def __contains__ (self,key):
        if key in self.name: return True
        else: return False
        
    def __str__(self):
        self.getEstadistics()
        return 'Variable Fisiologica:%s\n| Media: %f |\n| Mediana: %f |\n| Valor Maximo: %f |\n| Valor Minimo: %f|\n'%(self.name,float(self.estadisticValues['Media']),float(self.estadisticValues['Mediana']),float(self.estadisticValues['Valor maximo']),float(self.estadisticValues['Valor minimo']))
    
    #Funcion para calcular la media de las variables fisiologicas    
    def getEstadistics(self):
        
        matriz_float = self.datos.astype(np.float)

        estadisticas = {}
        estadisticas ['Media']=        np.average(matriz_float)
        estadisticas ['Mediana']=      np.median(matriz_float)
        estadisticas ['Valor maximo']= np.argmax(matriz_float)
        estadisticas ['Valor minimo']= np.argmin(matriz_float)
        self.estadisticValues = estadisticas
        return estadisticas

    # Funcion para graficar. Falta decidir el lugar donde debe ir
    def graficar(self):

        
        matriz_float = self.datos.astype(np.float)
        tamaño = matriz_float.shape
        segundos = tamaño[0]/100
        segundos_graficar = np.array(range(tamaño[0]))
        frecuencia = float(segundos/tamaño[0])
        contador = 0

        for i in np.array(range(tamaño[0])):
            segundos_graficar[i] = contador           
            contador = contador + frecuencia
        

        #En este bloque se ejecutan los comandos para graficar
        plt.title('Comportamiento de variable fisiologica en el tiempo')
        plt.xlabel('Tiempo  [=]Segundos')
        plt.ylabel('Variable fisiologica')
        plt.plot(segundos_graficar,matriz_float)
        plt.show()

objeto = biblioteca()
objeto.menuInicial()
        
'''
PENDIENTES:
-Relacionar las ultimas funciones con las clases.( creo que ya)
-probar menu para la ejecucion de todo el algoritmo (en curso)
-probar buscador (en curso)
-realizar diagrama de clases (en curso)
-probar clase varFis 

Hechos:
- constructor, contain, str de estudios funciona
- crear funcion para importar las variables fisiologicas.
- menu creado
- buscador creado
- metodos de funciones creadas
'''
