import numpy as np
import matplotlib.pyplot as plt
#var_fis = variable fisiologica
#clase contenedora de los objetos tipo estudio y var_fis

class Biblioteca(object):
    
    #Inicializador clase buscador
    def __init__(self,Estudios=(None)):
        #self.estudios atributo de clase buscasdor (Lista)
        self.estudios = Estudios

    #Agrega los objetos tipo estudio al atributo self.estudios 
    """por que aqui?"""
    def add_busc (self,Estudio):
        self.estudios.extend(Estudio)
        print('...Estudio agregado a base de datos ')
    
    #Funcion para buscar en todos los elementos contenidos en self.estudios    
    def buscador (self,key):
        if key in self.estudios:return True
        else: return False
     
    def menuInicial(self,option):
        print ("1. Agregar estudio")
        print ("2. Consultar estudios")
        print ("3. Salir")
        option = self.input_validate(self)
        if option == 1: """crear objeto tipo estudio"""
        elif option == 2: """Si no hay estudios: "No hay estudios que consultar"
        y vuelve a el menu inicial
        si hay estudios, se procede a #buscar en un objeto tipo biblioteca 
        (modificar metodo contains esta clase),
        que debe ser un diccionaio o array de objetos tipo estudio""" 
        else: """salir"""
        
    # valida entradas numericas de los input para menu
    def input_validate(self,tipo="int"):
        '''
        consult_validate (int) -> int
        
        retorna un entero segun estas instrucciones:  
        Si tipo == binary: x debe ser adquirir el valor de 1 o 2.
        
        >>> consult_validate (binary)
        Por favor ingrese un número:
        1
        1
        '''
        while True:
            try:
                #Valida para enteros
                option = int(input("Por favor ingrese un número: "))
                #Valida para entradas 1 o 2
                if tipo == "binary":
                    if not (option == 1) or not (option == 2): option = int("error")
                break
            except ValueError:
                print("Oops! No era válido. Intente nuevamente...")
        return option
    
            
            
class Estudio(object):
    #Var_Fi (variables fisiologicas)=lista
    def __init__(self,Name,Patologia,ID,Var_Fi=(None)):
        self.name = Name
        self.patologia = Patologia
        self.id = ID
        self.var_fi = Var_Fi
        print('...Estudio creado')
        #Ejecuta la funcion add_busc de la clase Buscador
        Buscador.add_busc(self, Estudio)
        
        
    #Agrega las variables fisiologicas al atributo self.var_fi   
    def add_var_fis (self,Var_Fis):
        self.var_fi.extend(Var_Fis)
        print('... Variable agregada a estudio')    
    
    # sobrecarga del metodo contains para usar en el buscador
    def __contains__ (self,key):
        pass

class Var_Fis(object):
        
    def __init__(self,Name_VF,Registro,Estadisticos=(None),Val_Est):
        self.name_vf = Name_VF
        self.reg = Registro
        
        #Estadisticos(lista)=contiene los datos estadisticos de la siguiente forma:  Posicion 0: Media. Posicion 1: mediana.Posicion 2: Val max. posicion 3: Val min
        self.estadisticos = Estadisticos
        self.val_est = Val_Est
        print('...Variable creada')
        
        #ejecuta la funcion add_var_fis de la clase Estudio
        Estudio.add_var_fis(self, Var_Fis)
        
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
