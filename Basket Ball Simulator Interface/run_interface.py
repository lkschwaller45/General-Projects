

# MH 1/28/2020

from PyQt5 import QtCore, QtGui, QtWidgets


import interface
import gui2py

from gui2py import guiBackend


# this script is only for initializing the user interface and handing 
# control over to the backend
#
# run this script with python to start the GUI and all connected code


class interface_instance(interface.Ui_MainWindow):
    def __init__(self,MainWindow):
        super(interface_instance,self).setupUi(MainWindow)
        self.backend = guiBackend(self)


if __name__ == "__main__":
    import sys 
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = interface_instance(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())





