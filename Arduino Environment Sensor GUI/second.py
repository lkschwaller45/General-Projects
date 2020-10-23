
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import enviroment_old
from PyQt5.QtGui import QPalette,QColor
from PyQt5.QtCore import Qt
from guicalls import guiBackend

class ChangeGraphVariable(enviroment_old.Ui_MainWindow):
    def __init__(self,MainWindow):
        super(ChangeGraphVariable,self).setupUi(MainWindow)
        self.backend = guiBackend(self)
        self.variablelist = [self.Humidity_box, self.Temp_box, self.Pressure_box, self.UVA_Intensity_box,  self.UVIndex_box, self.LightIntens_box,self.UVB_Intesity_box]


if __name__=="__main__":
    app = QApplication(sys.argv)
    # Style and Theme - Current Dark mode
    app.setStyle('Fusion')
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)
    qApp.setPalette(dark_palette)
    qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")
    MainWindow = QtWidgets.QMainWindow()
    ui = ChangeGraphVariable(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())