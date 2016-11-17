#TAREA 2: PRONOSTICO DE ENFERMEDADES
# Daniel Góez Molina         CC 1.037.621.550
# Andres Julian Viana Uribe  CC 1.214.734.333

import numpy as np
import matplotlib.pyplot as plt
#from _ast import Pass
#var_fis = variable fisiologica
#clase contenedora de los objetos tipo estudio y var_fis

class biblioteca(object):
    def __init__(self,estudios=[]):
        self.estudios = estudios

    #Agrega los objetos tipo estudio al atributo self.estudios 
    def addLib (self,object_estudio):
        self.estudios.append(object_estudio)
        print('...Estudio agregado a base de datos ')
    
    # Funcion para buscar en todos los elementos contenidos en self.estudios     
    def buscador (self,key):
        # Inicializa indice para diccionario
        indice = 0
        resultados = {}
        # Itera sobre la lista self.estudios 
        for objeto in self.estudios:
            # Busca la clave en los objetos estudio y varFis por medio del metodo contains de ambas 
            if key in objeto or key in objeto.varfi:
                # Incremento del indice para nueva posicion de diccionario
                indice += 1
                # asigna objetos estudio el dic 
                resultados[indice] = objeto
                print (indice, ": ",resultados[indice])
        # Si el diccionario no es vacio pide el ingreso de una opcion de los resultados  
        if resultados != {}:
            opind = int(input('Seleccione el numero del estudio  '))
        # Si resultados es vacio imprime alerta 
        elif resultados == {}:
            opind = None
            print ("No existe ningun resultado asociado a la palabra clave")
            resultados[opind] = None   
        # retorna diccionario con los resultados
        return resultados[opind]
    
    # Muestra todos los elementos existentes en la biblioteca
    def showLibrary(self):
        if not self.estudios == []:
            for i in self.estudios:
                #ejecuta el str de estudio
                print (i)
    
    # Funcion de administracion de la biblioteca            
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
            #Validacion de ingreso de opcion 
            try:    
                opcion = int(input('Ingrese el número de la opción que desea...\n  '))
            except ValueError:
                print('Ingrese un numero valido')
                continue
            if opcion == 1:
                #Pide los datos necesarios para crear un objeto estudios
                name = str(input('Ingrese nombre  ')) 
                ide = str(input('Ingrese Identificación  '))
                pat = str(input('Ingrese patologia  '))
                #Ejecuta el metodo inicializador de estudios
                self.addLib (estudio(name, ide, pat))
                
            elif opcion == 2:
                #Recibe la palabra clave para buscar el estudio en la clase biblioteca
                key = str(input('Ingrese la palabra clave para la busqueda del estudio al que desea asociarle la viariable fisiologica'))
                #Ejecuta el metodo buscador de biblioteca
                study = self.buscador(key)
                #Valida la existencia de objetos tipo estudio
                if study == None:
                    print ('Ingrese un estudio existente. (Debe crear un estudio antes de asignarle un diagnostico)')
                    continue
                else: 
                    while True:                        
                        #Validacion e importacion del archivo
                        try:
                            file = open(str(input('Ingrese el nombre del archivo seguido de .txt  ')))
                            break
                        except IOError:
                            print ('No es posible abrir el archivo.\nVerifique el nombre ingresado.\nEl algoritmo distingue entre mayusculas')
                            continue
                    #Recive el nombre para asignar a la variable fisiologica
                    variableFis = str(input('Ingrese el nombre de la variable fisiologica: ')) 
                    #Ejecuta el inicializador de la clase varFis
                    objectVarFis = varFis(variableFis, file)
                    #Agrega el objeto tipo varFis al atributo varfi de estudios
                    study.addVarFis(objectVarFis)                 
            
            elif opcion == 3:
                #Ejecuta la funcion buscar estudios de la clase biblioteca e imprime todos los objetos tipo estudio
                self.showLibrary()                
            
            elif opcion == 4:
                #Recibe la palabra clave que el usuario desea buscar
                key = str(input('Ingrese el nombre del estudio  '))
                #Ejecuta la funcion buscar estudios de la clase biblioteca con key como argumento
                study = self.buscador(key)
                if study == None:
                    print('Debe crear por lo menos un estudio antes de poder buscar')
                    continue
                
            elif opcion == 5:
                #Recibe la palabra clave que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio'))
                #Ejecuta el buscador de la clase biblioteca
                study = self.buscador(key)
    
                #Valida la existencia de objetos tipo estudios
                if study == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                    continue
                else:
                    #Imprime la variable seleccionada
                    study.selectVarfis(study.namesVarfi())

            elif opcion == 6:
                #Recibe la palabra clave que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio  '))
                #Ejecuta la funcion buscar todos los estadistico de un estudio de la clase biblioteca
                study = self.buscador(key) 
                #Valida la existencia de objetos tipo estudios 
                if study == None:
                    print('Debe crear por lo menos un estudio y asignarle una variable fisiologica antes de poder buscar')
                    continue
                
                else:
                    #Muestra todas las variables fisiologicas asociadas al estudio seleccionado
                    study.showVarfis()

            elif opcion == 7:
                #Recibe la palabra clave que el usuario desea buscar
                key = str(input('Ingrese la palabra clave del estudio'))
                #Ejecuta el buscador de la clase biblioteca
                study = self.buscador(key)
                #Valida la existencia de objetos tipo estudios
                if study == None:
                    print('Ingrese un estudio existente. (Debe crear un estudio y asignarle una variable fisiologica para graficar)' )
                    continue
                else:
                    #Obtiene el objeto tipo varFis
                    objectVarFis = study.selectVarfis(study.namesVarfi())
                    #Grafica el objeto tipo varFis
                    objectVarFis.graficar()
                        
                    
class estudio(object):
    def __init__(self,name,iD,patologia,varFi=[]):
        self.name = name
        self.id = iD
        self.patology = patologia
        self.varfi = varFi
        print('...Estudio creado')
    
    # Agrega las variables fisiologicas al atributo self.var_fi
    def addVarFis (self, object_variable_fisiologica):
        self.varfi.append(object_variable_fisiologica)
        print('... Variable agregada a estudio')
        return self.varfi
    
    # Redefine del metodo contains para usar en el buscador
    def __contains__ (self,key):
        if (key in self.name + self.patology + self.id): exist = True
        else: exist = False
        for var in self.varfi:
            if key in var: exist = exist or True
            else: exist = exist or False
        return exist
    
    # Redefine str 
    def __str__(self):
        return '| Nombre: %s | ID: %s | Patologia: %s | Factores pronosticos: %s|'%(self.name.capitalize(), self.id, self.patology.capitalize(), self.namesVarfi())

    # Retorna una lista con nombres de las variables fisiologicas
    def namesVarfi(self):
        listvf = []
        # agrstr(input('Ingrese nombre de la variable'))ega a lista auxiliar los nombres del del atributo .name de objetos varFis
        for i in self.varfi:
            listvf.append(i.name)
        return listvf
    
    # Seleccion objetos tipo varFis del atributo self.varfi  
    def selectVarfis(self,lista):
        # Imprime nombres de la variables fisiologicas 
        for varfis in lista:
            print (varfis)
            
        inlet = str(input('Ingrese nombre de la variable'))
        if inlet in lista:
            # Almacena el indice de la variable seleccionado    
            indice = lista.index(inlet)
            # Imprime la variable seleccionada
            print (self.varfi[indice])
            return self.varfi[indice]

        else:
            print ('No existe esa variable fisiologica. Verifique que el estudio tenga variables fisiologicas asociadas')
    
    
    # imprime todas la variales Fisiologicas con el metodo str de los objetos varFis        
    def showVarfis(self):
        # Si la lista no es vacia imprime todas las Variables fisiologicas
        if not self.varfi == []:
            for objetoVarfis in self.varfi:
                #ejecuta el str de los objetos varFis
                print (objetoVarfis)


class varFis(object):
    def __init__(self,name, datos, dic = {} ):
        self.name = name
        self.datos = np.loadtxt(datos)
        self.estadisticValues = dic
        print('...Variable creada')
    
    # redefinicion del metodo contains
    def __contains__ (self,key):
        # Solo busca en el atributo name
        if key in self.name: return True
        else: return False
        
    # redefinicion del metodo print y str 
    def __str__(self):
        # Usa la funcion getEstadistics para asignarle datos al atributo estadisticValues  
        self.getEstadistics()
        # formato de respresentacion string
        return 'Variable Fisiologica:%s\n| Media: %f |\n| Mediana: %f |\n| Valor Maximo: %f |\n| Valor Minimo: %f|\n'%(self.name,float(self.estadisticValues['Media']),float(self.estadisticValues['Mediana']),float(self.estadisticValues['Valor maximo']),float(self.estadisticValues['Valor minimo']))
    
    # Funcion para calcular valores estadisticos de la variables fisiologicas 
    def getEstadistics(self):
        # Convierte el arreglo de numpy loadtxt a un arreglo numpy float
        matriz_float = self.datos.astype(np.float)
        
        estadisticas = {}
        # calcula los valores correspondientes a los datos estadisticos 
        # y los asiga en un diccionario con la clave del valor estadistico
        estadisticas ['Media']=        np.average(matriz_float)
        estadisticas ['Mediana']=      np.median(matriz_float)
        estadisticas ['Valor maximo']= np.argmax(matriz_float)
        estadisticas ['Valor minimo']= np.argmin(matriz_float)
        # asigna al atributo estadisticValues los datos calculados
        self.estadisticValues = estadisticas
        # retorna diccionario con datos estadisticos
        return estadisticas

    # Funcion para graficar
    def graficar(self):
        # Convierte el arreglo de numpy loadtxt a un arreglo numpy float
        matriz_float = self.datos.astype(np.float)
        # Calcula el tamaño de la matriz
        tamaño = matriz_float.shape
        print(tamaño)
        # Calcula la cantidad de datos del eje segundos (eje y)
        segundos = tamaño[0]/100
        # Calcula el paso de los datos para graficar en el eje x
        frecuencia = float(segundos/tamaño[0])
        # Asigna a segundos_graficar las divisiones numericas correspondientes al eje x 
        segundos_graficar = np.arange(0.0,float(segundos),frecuencia)

        # En este bloque se ejecutan los comandos para graficar
        plt.title('Comportamiento de variable fisiologica en el tiempo')
        plt.xlabel('Tiempo  [=]Segundos')
        plt.ylabel('Variable fisiologica')
        plt.plot(segundos_graficar,matriz_float)
        plt.show()


objeto = biblioteca()

objeto.addLib(estudio("Andres", "1214734333", "Tinnitus"))  
objeto.addLib(estudio("Daniel", "1037621550", "Rodilla de Monja"))

objeto.estudios[0].addVarFis(varFis('EEG', open("eeg3.txt")))
objeto.estudios[1].addVarFis(varFis('EE3', open("eeg1.txt"))) 

objeto.menuInicial()

