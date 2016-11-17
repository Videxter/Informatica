#Ventana Principal
import sys
from PyQt5.QtWidgets import (QDial, QSpinBox, QGridLayout, QLineEdit,QLabel,
                             QPushButton, QDialog, QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout,QLabel,QFontDialog,
                             QAction, QFileDialog, QWidget, QDialog, QInputDialog,
                             QToolTip, QMessageBox)


class SignalSlot_window(QDialog):
    def __init__(self,parent=None):
        super(SignalSlot_window,self).__init__(parent)
        
        Grid=QGridLayout()
        
        btn0= QPushButton('Agregar Estudio')
        btn1= QPushButton('Agregar Factor Pronostico')
        btn2= QPushButton('Mostrar todos los estudios')
        
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
        
        btn0.clicked.connect()        
        btn1.clicked.connect()
        btn2.clicked.connect()
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    vent = SignalSlot_window()
    vent.show()
    sys.exit(app.exec_())
        
