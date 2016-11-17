#Ventana Principal
import sys
from PyQt5.QtWidgets import (QDial, QSpinBox, QGridLayout, QLineEdit,QLabel,QDateEdit,
                             QPushButton, QDialog, QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout,QLabel,QFontDialog,
                             QAction, QFileDialog, QWidget, QDialog, QInputDialog,
                             QToolTip, QMessageBox)


class SignalSlot_window(QDialog):
    def __init__(self,parent=None):
        super(SignalSlot_window,self).__init__(parent)
        
        Grid=QGridLayout()
        
        btn0= QPushButton('Agregar Estudio')
        btn1= QPushButton('Agregar Factor Pronostico')
        btn2= QPushButton('Buscar')
        btn3= QPushButton('Mostrar todos los estudios')
        
        title1 = QLabel('Palabra clave')
        title2 = QLabel('Fecha de Nacimiento')
        title3 = QLabel('Nombre')
        title4 = QLabel('Cedula')
        title5 = QLabel('Patologia')
        title6 = QLabel('FechaFP')
        title7 = QLabel('Ingreso de datos')
        title8 = QLabel('Busqueda')
        
        
        plbra_clave = QLineEdit()
        fecha_nac = QLineEdit()
        name = QLineEdit()
        cc = QLineEdit()
        patologia = QLineEdit()
        fechaFP = QLineEdit()
        

        Grid.addWidget(btn0,1,0)
        Grid.addWidget(btn1,2,0)
        Grid.addWidget(btn2,10,0)
        Grid.addWidget(btn3,10,1)
        Grid.addWidget(plbra_clave,4,1)
        Grid.addWidget(fecha_nac,5,1)
        Grid.addWidget(name,6,1)
        Grid.addWidget(cc,7,1)
        Grid.addWidget(patologia,8,1)
        Grid.addWidget(fechaFP,9,1)

        Grid.addWidget(title1,4,0)
        Grid.addWidget(title2,5,0)
        Grid.addWidget(title3,6,0)
        Grid.addWidget(title4,7,0)
        Grid.addWidget(title5,8,0)
        Grid.addWidget(title6,9,0)
        Grid.addWidget(title7,0,0)
        Grid.addWidget(title8,3,0)

        
        self.setLayout(Grid)
        self.setWindowTitle('Pronostico de Enfermedades')        
        
        '''
        btn0.clicked.connect()        
        btn1.clicked.connect()
        btn2.clicked.connect()
        btn3.clicked.connect()
        '''
    '''    
    def ClicBoton(self):
        sender= self.sender()
        print('Se presionó el '+ sender.text())
    '''

        
if __name__== '__main__':
    app = QApplication(sys.argv)
    vent = SignalSlot_window()
    vent.show()
    sys.exit(app.exec_())
    
# Ventana para agregar estudio
class vent_est(QDialog):
    def __init__(self,parent=None):
        super(vent_est,self).__init__(parent)
        
        Grid=QGridLayout()
        
        btn0= QPushButton('Aceptar')
        btn1= QPushButton('Cancelar')
        

        title1 = QLabel('Nombre')
        title2 = QLabel('Fecha de Nacimiento')
        title3 = QLabel('Cedula')
        title4 = QLabel('Patologia')
        title5 = QLabel('Ingrese los siguientes datos')
        title6 = QLabel('')
        
        name = QLineEdit()
        fecha_nac = QDateEdit()
        cc = QLineEdit()
        patologia = QLineEdit()
        

        Grid.addWidget(btn0,5,0)
        Grid.addWidget(btn1,5,1)
        Grid.addWidget(name,1,1)
        Grid.addWidget(fecha_nac,2,1)
        Grid.addWidget(cc,3,1)
        Grid.addWidget(patologia,4,1)

        Grid.addWidget(title1,1,0)
        Grid.addWidget(title2,2,0)
        Grid.addWidget(title3,3,0)
        Grid.addWidget(title4,4,0)
        Grid.addWidget(title5,0,0)
        Grid.addWidget(title6,6,0)

        
        self.setLayout(Grid)
        self.setWindowTitle('Creacion de Estudio')        
        
        '''
        btn0.clicked.connect()        
        btn1.clicked.connect()
        btn2.clicked.connect()
        btn3.clicked.connect()
        '''
    '''    
    def ClicBoton(self):
        sender= self.sender()
        print('Se presionó el '+ sender.text())
    '''

        
if __name__== '__main__':
    app = QApplication(sys.argv)
    vent = vent_est()
    vent.show()
    sys.exit(app.exec_())
    
#Ventana para agregar factor pronostico a estudio
class ing_factpron(QDialog):
    def __init__(self,parent=None):
        super(ing_factpron,self).__init__(parent)
        
        Grid=QGridLayout()
        
        btn0= QPushButton('Aceptar')
        btn1= QPushButton('Cancelar')
        btn2= QPushButton('Cargar archivo de texto')
       
       
        title1 = QLabel('Cedula del estudio a agregar factor pronostico ')
        title2 = QLabel('Nombre del factor pronostico')
        title3 = QLabel('Fecha de creacion del estudio')
        title4 = QLabel('Datos factor pronostico')
        title5 = QLabel('Ingrese los siguientes datos')
        
        cc_est = QLineEdit()
        namepat = QLineEdit()
        fechaFP = QDateEdit()

        Grid.addWidget(btn0,5,0)
        Grid.addWidget(btn1,5,1)
        Grid.addWidget(btn2,4,1)
        Grid.addWidget(cc_est,1,1)
        Grid.addWidget(namepat,2,1)
        Grid.addWidget(fechaFP,3,1)

        Grid.addWidget(title1,1,0)
        Grid.addWidget(title2,2,0)
        Grid.addWidget(title3,3,0)
        Grid.addWidget(title4,4,0)
        Grid.addWidget(title5,0,0)
        

        
        self.setLayout(Grid)
        self.setWindowTitle('Creacion de factor pronostico')        
        
        btn2.clicked.connect(self.FileDialog)
        '''
        btn0.clicked.connect()        
        btn1.clicked.connect()
        btn2.clicked.connect()
        btn3.clicked.connect()
        '''
    '''    
    def ClicBoton(self):
        sender= self.sender()
        print('Se presionó el '+ sender.text())
    '''
    def FileDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Seleccione un archivo')
        print(fname)
        if fname[0]:
            f = open(fname[0], 'r')
            '''
            data = f.read()
            self.textEdit.setText(data)
            '''
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    vent = ing_factpron()
    vent.show()
    sys.exit(app.exec_())
