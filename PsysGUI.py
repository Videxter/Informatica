import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, 
                             QWidget, QAction, QTabWidget,QVBoxLayout,
                             QHBoxLayout,QGroupBox, QFormLayout,QTextEdit, 
                             QLineEdit, QLabel,QCalendarWidget, QSpacerItem,
                             QComboBox,QListWidget, QFileDialog, QDialog)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
#from PyQt5.Qt import 
from psysClass import biblioteca, estudio, varFis


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PSYS'
        self.left = 0
        self.top = 0
        self.width = 300
        self.height = 200
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()

class MyTableWidget(QWidget):        

    def __init__(self, parent):   
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        #self.tabs.resize(100,200) 
        #self.tabs.setTabPosition(self.tabs.West)
        #self.tabs.setMovable(False)
        #self.tabs.setTabEnabled(1, False)
        #self.tabs.isEnabled()
        #self.tabs.setVisible(False)
        #self.tabs.setTabBarAutoHide(True)
        #self.tabs.setTabsClosable(True)

        self.bbliotca = biblioteca()
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()	
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        
        # organizacion de la parte superior
        self.tabSuper = QGroupBox('Psys')
        self.lay = QHBoxLayout(self)
        
        # botones y objetos de esa zona 
        self.butSearch = QPushButton("Buscar")
        self.searchLine = QLineEdit('Buscar...')
        
        # agrega los objetos
        self.lay.addWidget(self.searchLine)
        self.lay.addWidget(self.butSearch)
        
        # establece la organizacion horizontal del group box
        self.tabSuper.setLayout(self.lay)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Estudios")
        self.tabs.addTab(self.tab2,"Factores Pronosticos")
        self.tabs.addTab(self.tab3,"Estadisticas y Graficos")
        self.tabs.addTab(self.tab4,"Busqueda")
        
        # Create estudios tab
        self.tab1.layout1 = QFormLayout(self)
       
        self.nombre = QLineEdit()
        self.id = QLineEdit()
        self.ptology = QLineEdit()
        self.date = QCalendarWidget(self.tab1)
        self.pushSaveEst = QPushButton("Guardar")
        self.pushCancel = QPushButton("Cancelar")
        self.btnCreate= QPushButton('Crear Nuevo Estudio')
        self.btnShowFP = QPushButton('Ver Factor Pronostico')
        
        
        
        self.tab1.layout1.addRow(self.btnCreate)
        self.tab1.layout1.addRow(QLabel('Nombre'), self.nombre)
        self.tab1.layout1.addRow(QLabel('Identificacion'), self.id)
        self.tab1.layout1.addRow(QLabel('Patologia'), self.ptology)
        self.tab1.layout1.addRow(QLabel('Fecha de nacimiento'), self.date)
        self.tab1.layout1.addItem(QSpacerItem(0,10))
        self.tab1.layout1.addRow(self.pushCancel, self.pushSaveEst)
        self.tab1.layout1.addItem(QSpacerItem(0,10))
        self.tab1.layout1.addWidget(self.btnShowFP)
        
        #self.tab1.layout1.addWidget()
        self.tab1.setLayout(self.tab1.layout1)
        

        # crea factores tab
        self.tab2.layout2 = QFormLayout(self)
       
        self.nombreFP = QLineEdit()
        self.dateFP = QCalendarWidget(self.tab2)
        self.verEstadtcs = QPushButton('Ver Datos Estadisticos')
        self.pushOpen = QPushButton('Open file')
        self.fileName = ''
        self.butAbrir= QPushButton('Abrir\nFactor Pronostico ') #ventana de dialogo + combobox
        self.butCrearFP= QPushButton('Crear Nuevo Factor Pronostico')
        self.comboFP = QComboBox()
        self.saveFP = QPushButton('Guardar')
        self.cancel = QPushButton('cancelar')
        
                
        
        self.tab2.layout2.addRow(self.butAbrir, self.comboFP)
        self.tab2.layout2.addItem(QSpacerItem(0,20))
        self.tab2.layout2.addRow(self.butCrearFP)    
        self.tab2.layout2.addRow(QLabel('Nombre'), self.nombreFP)
        self.tab2.layout2.addRow(QLabel('Fecha'), self.dateFP)
        self.tab2.layout2.addRow(QLabel('Archivo'), self.pushOpen) #conectar a ventanafiledialog
        
        self.tab2.layout2.addItem(QSpacerItem(0,10))
        self.tab2.layout2.addRow(self.cancel,self.saveFP)
        self.tab2.layout2.addItem(QSpacerItem(0,10))
        self.tab2.layout2.addWidget(self.verEstadtcs)
        
        self.tab2.setLayout(self.tab2.layout2)
        
        
        # crea 3er tab
        
        self.tab3.layout3 = QFormLayout(self)
        self.butShowGraf = QPushButton("Ver Grafico")
        self.media = QLabel('00000000000')
        self.mediana = QLabel('00000000000')
        self.maximum = QLabel('00000000000')
        self.minimum = QLabel('00000000000')
        self.tab3.layout3.addRow(QLabel('Media:'),self.media)
        self.tab3.layout3.addRow(QLabel('Mediana:'),self.mediana)
        self.tab3.layout3.addRow(QLabel('Maximo:'),self.maximum)
        self.tab3.layout3.addRow(QLabel('Minimo:'),self.minimum)
        self.tab3.layout3.addItem(QSpacerItem(0,20))
        self.tab3.layout3.addRow(self.butShowGraf)
        
        self.tab3.setLayout(self.tab3.layout3)
        
        # crea 4 ventana
        
        self.tab4.layout4 = QVBoxLayout()
        
        self.comboEstud = QComboBox()
        self.btnComboAcept = QPushButton('Aceptar')
        self.tab4.layout4.addWidget(QLabel('Seleccione un estudio'))
        self.tab4.layout4.addWidget(self.comboEstud)
        self.tab4.layout4.addSpacerItem(QSpacerItem(0,500))   
        self.tab4.layout4.addWidget(self.btnComboAcept)
        
        self.tab4.setLayout(self.tab4.layout4)
        
        # desactiva el tab1
        self.tabs.setTabEnabled(0, True)
        self.tabs.setTabEnabled(1, False)
        self.tabs.setTabEnabled(2, False)

        # Add tabs to widget 
        self.layout.addWidget(self.tabSuper)     
        self.layout.addWidget(self.tabs)
        
        self.setLayout(self.layout)
        self.tabs.setCurrentIndex(3)
        
        
        self.butSearch.clicked.connect(self.buscar) # buscador
        self.btnComboAcept.clicked.connect(self.selectEst) # seleccion del buscador
        self.btnCreate.clicked.connect(self.configCreate) # habilita la creacion de Estudio
        self.pushSaveEst.clicked.connect(self.addEst) # guarda estudio
        self.pushCancel.clicked.connect(self.tabEst) # cancela ingreso de datos de estudio
        
        self.btnShowFP.clicked.connect(self.showTabFP) # abre ventana Var Fisiologica
        self.butAbrir.clicked.connect(self.abrirVarfis) # abre VF despejada
        
        self.butCrearFP.clicked.connect(self.configCreate)
        self.pushOpen.clicked.connect(self.getFile)
        self.saveFP.clicked.connect(self.addFP)
        self.verEstadtcs.clicked.connect(self.showEstadist)
        self.butShowGraf.clicked.connect(self.showGraf)
        self.tabs.currentChanged.connect(self.tabEst)
        self.tabs.currentChanged.connect(self.tabVarfis)
        
        self.cancel.clicked.connect(self.tabVarfis)
        
        
        #self.btnShowFP.clicked.connect(self.tabVarfis)
        
    ####FAltan los QmessagesBox
        
    @pyqtSlot()
    #busca los estudios en la clase biblioteca 
    def buscar(self):
        self.comboEstud.clear()
        key = self.searchLine.text()
        busqueda = self.bbliotca.buscador(key)
        self.tabs.setCurrentIndex(3)
        self.btnShowFP.setEnabled(True)
        # falta un buscar todo
        for clave in busqueda:
            #print (clave)
            self.comboEstud.addItems([busqueda[clave].id+"-"+busqueda[clave].name])
    
    #carga un Estudio existente
    #abre el estudio seleccionado
    def selectEst (self):
        self.comboFP.clear() # limpia el combo para agregar actuales FP
        key = self.searchLine.text()
        busqueda = self.bbliotca.buscador(key)
        index = (self.comboEstud.currentIndex()+1) 
        self.estudio = busqueda[index] 
        
        self.tabs.setCurrentIndex(0) #cambia de ventana
        # configura ventana estudios
        self.nombre.setText(self.estudio.name) 
        self.id.setText(self.estudio.id)
        self.ptology.setText(self.estudio.patology)  
        #falta cargar date 
        
        # configura ventana FP 
        self.comboFP.addItems(self.estudio.namesVarfi())
    
    def abrirVarfis(self):
        index = (self.comboFP.currentIndex())
        self.varfis =  self.estudio.varfi[index]
        
        self.nombreFP.setText(self.varfis.name)
        self.verEstadtcs.setEnabled(True)
        self.varfis.getEstadistics()
        estadistics = self.varfis.estadisticValues
        
        self.media.setText(str(estadistics['Media']))
        self.mediana.setText(str(estadistics['Mediana']))
        self.minimum.setText(str(estadistics['Valor minimo']))
        self.maximum.setText(str(estadistics['Valor maximo']))
        
    def showTabFP(self):
        self.tabs.setCurrentIndex(1)
        self.tabs.setTabEnabled(1, True)
        
    def showEstadist(self):
        self.tabs.setCurrentIndex(2)
        self.tabs.setTabEnabled(2, True)

    def showGraf(self):
        self.varfis.graficar()
                
    def addEst(self):# Agrega estudio nuevo

        #'''self.date.selectedDate().toString()'''
        
        n = self.nombre.text()
        i = self.id.text()
        p = self.ptology.text()
        d = self.date.selectedDate().toString()
        est = estudio(n,i,p,d)
        self.bbliotca.addLib(est)
        
        self.tabEst()   
    
    def getFile(self):#obtiene el archivo de variable fisiologica
        fileName = QFileDialog.getOpenFileName(self, 'Seleccione un archivo')
        self.fileName = open(fileName[0])
        self.pushOpen.setText(str(fileName[0]))
     
    def addFP(self):# crea factor pronostico nuevo

        name = self.nombreFP.text()
        date = self.dateFP.selectedDate().toString()
        var = varFis(name,self.fileName,date)
        self.estudio.addVarFis(var)
        self.abrirVarfis()
        self.comboFP.clear()
        self.tabVarfis()
        
    def configCreate(self):#configuraciones de los layouts para crear estudios y FP o V. Fisiologicas
        if self.tabs.currentIndex() == 0:
            self.btnShowFP.setEnabled(False)
            self.btnCreate.setEnabled(False)            
            self.nombre.setEnabled(True)
            self.id.setEnabled(True)
            self.ptology.setEnabled(True)
            self.date.setEnabled(True)
            self.pushSaveEst.setEnabled(True)
            self.pushCancel.setEnabled(True)
            self.nombre.setText('')
            self.id.setText('')
            self.ptology.setText('')
            
        elif self.tabs.currentIndex() == 1:
            self.nombreFP.setEnabled(True   )
            self.dateFP.setEnabled(True)
            self.verEstadtcs.setEnabled(False)
            self.pushOpen.setEnabled(True)
            self.butAbrir.setEnabled(True)
            self.butCrearFP.setEnabled(True)
            self.comboFP.setEnabled(True)         
            self.cancel.setEnabled(True )
            self.saveFP.setEnabled(True)
            self.pushOpen.setText('Abrir')
            self.comboFP.setEnabled(False)
            self.butAbrir.setEnabled(False)
    
    def tabVarfis(self):#configuracion por defecto de var fisiologica 
        self.nombreFP.setEnabled(False)
        self.nombreFP.setText('')
        self.dateFP.setEnabled(False)
        self.verEstadtcs.setEnabled(False)
        self.pushOpen.setEnabled(False)
        self.butAbrir.setEnabled(True)
        self.butCrearFP.setEnabled(True)
        self.comboFP.setEnabled(True)
        self.cancel.setEnabled(False)
        self.saveFP.setEnabled(False)
        self.verEstadtcs.setEnabled(True)
        self.verEstadtcs.setEnabled(False)
        self.pushOpen.setText('Abrir')
        self.tabs.setTabEnabled(2,True)

        #self.comboFP.clear()

    def tabEst(self):#configuracion por defecto de pestaña estudio        
        self.nombre.setEnabled(False)
        self.id.setEnabled(False)
        self.ptology.setEnabled(False)
        
        self.date.setEnabled(False)
        self.pushSaveEst.setEnabled(False)
        self.pushCancel.setEnabled(False)
        self.btnCreate.setEnabled(True)
        self.btnShowFP.setEnabled(True)  
        
        
        
        
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  

