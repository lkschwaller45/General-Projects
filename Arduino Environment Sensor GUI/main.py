# from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette,QColor
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import numpy as np

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow,self).__init__(*args, **kwargs)
        self.graphWidget = pg.PlotWidget()
        self.setCentralWidget(self.graphWidget)
        hour = np.linspace(1,10,num =10)
        temperature = np.random.rand(10)
        print(hour)
        print(temperature)
        pen = pg.mkPen(color = (255,255,255), width = 5)
        self.graphWidget.plot(hour,temperature, pen=pen, symbol= 'o',symbolBrush=('w'),symbolSize= 15 )

        #
        # #Style and Theme - Current Dark mode
        # app.setStyle('Fusion')
        # dark_palette = QPalette()
        # dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
        # dark_palette.setColor(QPalette.WindowText, Qt.white)
        # dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
        # dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
        # dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
        # dark_palette.setColor(QPalette.ToolTipText, Qt.white)
        # dark_palette.setColor(QPalette.Text, Qt.white)
        # dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
        # dark_palette.setColor(QPalette.ButtonText, Qt.white)
        # dark_palette.setColor(QPalette.BrightText, Qt.red)
        # dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
        # dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
        # dark_palette.setColor(QPalette.HighlightedText, Qt.black)
        # qApp.setPalette(dark_palette)
        # qApp.setStyleSheet("QToolTip { color: #ffffff; background-color: #2a82da; border: 1px solid white; }")

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()












