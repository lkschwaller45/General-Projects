# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1337, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setDockOptions(QtWidgets.QMainWindow.AllowTabbedDocks|QtWidgets.QMainWindow.AnimatedDocks)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 921, 441))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 901, 319))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.shotSquareAngleMinimumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotSquareAngleMinimumValueLineEdit.setObjectName("shotSquareAngleMinimumValueLineEdit")
        self.gridLayout.addWidget(self.shotSquareAngleMinimumValueLineEdit, 5, 2, 1, 1)
        self.customHorizontalVerticalCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customHorizontalVerticalCheckBox.setObjectName("customHorizontalVerticalCheckBox")
        self.gridLayout.addWidget(self.customHorizontalVerticalCheckBox, 10, 2, 1, 1)
        self.speedStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.speedStepSizeLineEdit.setEnabled(True)
        self.speedStepSizeLineEdit.setObjectName("speedStepSizeLineEdit")
        self.gridLayout.addWidget(self.speedStepSizeLineEdit, 6, 11, 1, 1)
        self.customDistanceXMinimumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceXMinimumLineEdit.setEnabled(False)
        self.customDistanceXMinimumLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.customDistanceXMinimumLineEdit.setObjectName("customDistanceXMinimumLineEdit")
        self.gridLayout.addWidget(self.customDistanceXMinimumLineEdit, 11, 2, 1, 1)
        self.shotElevationAngleStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotElevationAngleStepSizeLineEdit.setEnabled(True)
        self.shotElevationAngleStepSizeLineEdit.setObjectName("shotElevationAngleStepSizeLineEdit")
        self.gridLayout.addWidget(self.shotElevationAngleStepSizeLineEdit, 4, 11, 1, 1)
        self.speedMaximumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.speedMaximumValueLineEdit.setEnabled(True)
        self.speedMaximumValueLineEdit.setObjectName("speedMaximumValueLineEdit")
        self.gridLayout.addWidget(self.speedMaximumValueLineEdit, 6, 4, 1, 1)
        self.speedMinimumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.speedMinimumValueLineEdit.setObjectName("speedMinimumValueLineEdit")
        self.gridLayout.addWidget(self.speedMinimumValueLineEdit, 6, 2, 1, 1)
        self.defaultLocationLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.defaultLocationLabel.setObjectName("defaultLocationLabel")
        self.gridLayout.addWidget(self.defaultLocationLabel, 10, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.gridLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 8, 2, 1, 1)
        self.defaultLocationComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.defaultLocationComboBox.setObjectName("defaultLocationComboBox")
        self.defaultLocationComboBox.addItem("")
        self.defaultLocationComboBox.addItem("")
        self.defaultLocationComboBox.addItem("")
        self.defaultLocationComboBox.addItem("")
        self.gridLayout.addWidget(self.defaultLocationComboBox, 10, 1, 1, 1)
        self.customRadialDistanceMinimumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialDistanceMinimumLineEdit.setEnabled(False)
        self.customRadialDistanceMinimumLineEdit.setObjectName("customRadialDistanceMinimumLineEdit")
        self.gridLayout.addWidget(self.customRadialDistanceMinimumLineEdit, 13, 2, 1, 1)
        self.shotSquareAngleStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotSquareAngleStepSizeLineEdit.setEnabled(True)
        self.shotSquareAngleStepSizeLineEdit.setObjectName("shotSquareAngleStepSizeLineEdit")
        self.gridLayout.addWidget(self.shotSquareAngleStepSizeLineEdit, 5, 11, 1, 1)
        self.shotSquareAngleMaximumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotSquareAngleMaximumValueLineEdit.setEnabled(True)
        self.shotSquareAngleMaximumValueLineEdit.setObjectName("shotSquareAngleMaximumValueLineEdit")
        self.gridLayout.addWidget(self.shotSquareAngleMaximumValueLineEdit, 5, 4, 1, 1)
        self.backSpinUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.backSpinUnitComboBox.setObjectName("backSpinUnitComboBox")
        self.backSpinUnitComboBox.addItem("")
        self.backSpinUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.backSpinUnitComboBox, 7, 8, 1, 1)
        self.customDistanceXLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.customDistanceXLabel.setObjectName("customDistanceXLabel")
        self.gridLayout.addWidget(self.customDistanceXLabel, 11, 0, 1, 1)
        self.shotElevationAngleFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.shotElevationAngleFixedCheckBox.setEnabled(True)
        self.shotElevationAngleFixedCheckBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.shotElevationAngleFixedCheckBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.shotElevationAngleFixedCheckBox.setToolTipDuration(41)
        self.shotElevationAngleFixedCheckBox.setProperty("checkFixed", False)
        self.shotElevationAngleFixedCheckBox.setObjectName("shotElevationAngleFixedCheckBox")
        self.gridLayout.addWidget(self.shotElevationAngleFixedCheckBox, 4, 1, 1, 1)
        self.shotSquareAngleLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.shotSquareAngleLabel.setObjectName("shotSquareAngleLabel")
        self.gridLayout.addWidget(self.shotSquareAngleLabel, 5, 0, 1, 1)
        self.customDistanceYMinimumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceYMinimumLineEdit.setEnabled(False)
        self.customDistanceYMinimumLineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.customDistanceYMinimumLineEdit.setObjectName("customDistanceYMinimumLineEdit")
        self.gridLayout.addWidget(self.customDistanceYMinimumLineEdit, 12, 2, 1, 1)
        self.shotElevationAngleMinimumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotElevationAngleMinimumValueLineEdit.setObjectName("shotElevationAngleMinimumValueLineEdit")
        self.gridLayout.addWidget(self.shotElevationAngleMinimumValueLineEdit, 4, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 4, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 11, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setAcceptDrops(False)
        self.label_5.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 2, 1, 1)
        self.speedUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.speedUnitComboBox.setObjectName("speedUnitComboBox")
        self.speedUnitComboBox.addItem("")
        self.speedUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.speedUnitComboBox, 6, 8, 1, 1)
        self.backSpinMinimumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.backSpinMinimumValueLineEdit.setObjectName("backSpinMinimumValueLineEdit")
        self.gridLayout.addWidget(self.backSpinMinimumValueLineEdit, 7, 2, 1, 1)
        self.speedFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.speedFixedCheckBox.setObjectName("speedFixedCheckBox")
        self.gridLayout.addWidget(self.speedFixedCheckBox, 6, 1, 1, 1)
        self.shotElevationAngleUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.shotElevationAngleUnitComboBox.setObjectName("shotElevationAngleUnitComboBox")
        self.shotElevationAngleUnitComboBox.addItem("")
        self.shotElevationAngleUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.shotElevationAngleUnitComboBox, 4, 8, 1, 1)
        self.shotSquareAngleUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.shotSquareAngleUnitComboBox.setObjectName("shotSquareAngleUnitComboBox")
        self.shotSquareAngleUnitComboBox.addItem("")
        self.shotSquareAngleUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.shotSquareAngleUnitComboBox, 5, 8, 1, 1)
        self.backSpinFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.backSpinFixedCheckBox.setObjectName("backSpinFixedCheckBox")
        self.gridLayout.addWidget(self.backSpinFixedCheckBox, 7, 1, 1, 1)
        self.backSpinStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.backSpinStepSizeLineEdit.setEnabled(True)
        self.backSpinStepSizeLineEdit.setObjectName("backSpinStepSizeLineEdit")
        self.gridLayout.addWidget(self.backSpinStepSizeLineEdit, 7, 11, 1, 1)
        self.shotElevationAngleLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.shotElevationAngleLabel.setObjectName("shotElevationAngleLabel")
        self.gridLayout.addWidget(self.shotElevationAngleLabel, 4, 0, 1, 1)
        self.customDistanceYLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.customDistanceYLabel.setObjectName("customDistanceYLabel")
        self.gridLayout.addWidget(self.customDistanceYLabel, 12, 0, 1, 1)
        self.backSpinLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.backSpinLabel.setObjectName("backSpinLabel")
        self.gridLayout.addWidget(self.backSpinLabel, 7, 0, 1, 1)
        self.shotElevationAngleMaximumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.shotElevationAngleMaximumValueLineEdit.setEnabled(True)
        self.shotElevationAngleMaximumValueLineEdit.setObjectName("shotElevationAngleMaximumValueLineEdit")
        self.gridLayout.addWidget(self.shotElevationAngleMaximumValueLineEdit, 4, 4, 1, 1)
        self.backSpinMaximumValueLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.backSpinMaximumValueLineEdit.setEnabled(True)
        self.backSpinMaximumValueLineEdit.setObjectName("backSpinMaximumValueLineEdit")
        self.gridLayout.addWidget(self.backSpinMaximumValueLineEdit, 7, 4, 1, 1)
        self.shotSquareAngleFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.shotSquareAngleFixedCheckBox.setObjectName("shotSquareAngleFixedCheckBox")
        self.gridLayout.addWidget(self.shotSquareAngleFixedCheckBox, 5, 1, 1, 1)
        self.customDistanceRadialLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.customDistanceRadialLabel.setObjectName("customDistanceRadialLabel")
        self.gridLayout.addWidget(self.customDistanceRadialLabel, 13, 0, 1, 1)
        self.speedLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.speedLabel.setObjectName("speedLabel")
        self.gridLayout.addWidget(self.speedLabel, 6, 0, 1, 1)
        self.customDistanceAngleLabel = QtWidgets.QLabel(self.gridLayoutWidget)
        self.customDistanceAngleLabel.setObjectName("customDistanceAngleLabel")
        self.gridLayout.addWidget(self.customDistanceAngleLabel, 14, 0, 1, 1)
        self.customRadialAngleMinimumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialAngleMinimumLineEdit.setEnabled(False)
        self.customRadialAngleMinimumLineEdit.setObjectName("customRadialAngleMinimumLineEdit")
        self.gridLayout.addWidget(self.customRadialAngleMinimumLineEdit, 14, 2, 1, 1)
        self.customDistanceYMaximumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceYMaximumLineEdit.setEnabled(False)
        self.customDistanceYMaximumLineEdit.setObjectName("customDistanceYMaximumLineEdit")
        self.gridLayout.addWidget(self.customDistanceYMaximumLineEdit, 12, 4, 1, 1)
        self.customDistanceXMaximumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceXMaximumLineEdit.setEnabled(False)
        self.customDistanceXMaximumLineEdit.setObjectName("customDistanceXMaximumLineEdit")
        self.gridLayout.addWidget(self.customDistanceXMaximumLineEdit, 11, 4, 1, 1)
        self.customRadialDistanceMaximumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialDistanceMaximumLineEdit.setEnabled(False)
        self.customRadialDistanceMaximumLineEdit.setObjectName("customRadialDistanceMaximumLineEdit")
        self.gridLayout.addWidget(self.customRadialDistanceMaximumLineEdit, 13, 4, 1, 1)
        self.customRadialAngleMaximumLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialAngleMaximumLineEdit.setEnabled(False)
        self.customRadialAngleMaximumLineEdit.setObjectName("customRadialAngleMaximumLineEdit")
        self.gridLayout.addWidget(self.customRadialAngleMaximumLineEdit, 14, 4, 1, 1)
        self.customRadialAngleUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.customRadialAngleUnitComboBox.setEnabled(False)
        self.customRadialAngleUnitComboBox.setObjectName("customRadialAngleUnitComboBox")
        self.customRadialAngleUnitComboBox.addItem("")
        self.customRadialAngleUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.customRadialAngleUnitComboBox, 14, 8, 1, 1)
        self.customRadialDistanceUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.customRadialDistanceUnitComboBox.setEnabled(False)
        self.customRadialDistanceUnitComboBox.setObjectName("customRadialDistanceUnitComboBox")
        self.customRadialDistanceUnitComboBox.addItem("")
        self.customRadialDistanceUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.customRadialDistanceUnitComboBox, 13, 8, 1, 1)
        self.customRadialDistanceAngleCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customRadialDistanceAngleCheckBox.setObjectName("customRadialDistanceAngleCheckBox")
        self.gridLayout.addWidget(self.customRadialDistanceAngleCheckBox, 10, 4, 1, 1)
        self.customDistanceUnitComboBox = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.customDistanceUnitComboBox.setEnabled(False)
        self.customDistanceUnitComboBox.setObjectName("customDistanceUnitComboBox")
        self.customDistanceUnitComboBox.addItem("")
        self.customDistanceUnitComboBox.addItem("")
        self.gridLayout.addWidget(self.customDistanceUnitComboBox, 11, 8, 1, 1)
        self.customDistanceXStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceXStepSizeLineEdit.setEnabled(False)
        self.customDistanceXStepSizeLineEdit.setObjectName("customDistanceXStepSizeLineEdit")
        self.gridLayout.addWidget(self.customDistanceXStepSizeLineEdit, 11, 11, 1, 1)
        self.customDistanceYStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customDistanceYStepSizeLineEdit.setEnabled(False)
        self.customDistanceYStepSizeLineEdit.setObjectName("customDistanceYStepSizeLineEdit")
        self.gridLayout.addWidget(self.customDistanceYStepSizeLineEdit, 12, 11, 1, 1)
        self.customRadialDistanceStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialDistanceStepSizeLineEdit.setEnabled(False)
        self.customRadialDistanceStepSizeLineEdit.setObjectName("customRadialDistanceStepSizeLineEdit")
        self.gridLayout.addWidget(self.customRadialDistanceStepSizeLineEdit, 13, 11, 1, 1)
        self.customRadialAngleStepSizeLineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.customRadialAngleStepSizeLineEdit.setEnabled(False)
        self.customRadialAngleStepSizeLineEdit.setObjectName("customRadialAngleStepSizeLineEdit")
        self.gridLayout.addWidget(self.customRadialAngleStepSizeLineEdit, 14, 11, 1, 1)
        self.customDistanceXFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customDistanceXFixedCheckBox.setEnabled(False)
        self.customDistanceXFixedCheckBox.setObjectName("customDistanceXFixedCheckBox")
        self.gridLayout.addWidget(self.customDistanceXFixedCheckBox, 11, 1, 1, 1)
        self.customDistanceYFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customDistanceYFixedCheckBox.setEnabled(False)
        self.customDistanceYFixedCheckBox.setObjectName("customDistanceYFixedCheckBox")
        self.gridLayout.addWidget(self.customDistanceYFixedCheckBox, 12, 1, 1, 1)
        self.customRadialDistanceFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customRadialDistanceFixedCheckBox.setEnabled(False)
        self.customRadialDistanceFixedCheckBox.setObjectName("customRadialDistanceFixedCheckBox")
        self.gridLayout.addWidget(self.customRadialDistanceFixedCheckBox, 13, 1, 1, 1)
        self.customRadialAngleFixedCheckBox = QtWidgets.QCheckBox(self.gridLayoutWidget)
        self.customRadialAngleFixedCheckBox.setEnabled(False)
        self.customRadialAngleFixedCheckBox.setObjectName("customRadialAngleFixedCheckBox")
        self.gridLayout.addWidget(self.customRadialAngleFixedCheckBox, 14, 1, 1, 1)
        self.speedLabel.raise_()
        self.speedMaximumValueLineEdit.raise_()
        self.shotSquareAngleMaximumValueLineEdit.raise_()
        self.shotElevationAngleMinimumValueLineEdit.raise_()
        self.shotElevationAngleLabel.raise_()
        self.shotElevationAngleMaximumValueLineEdit.raise_()
        self.label_13.raise_()
        self.backSpinLabel.raise_()
        self.backSpinMinimumValueLineEdit.raise_()
        self.label_6.raise_()
        self.shotSquareAngleLabel.raise_()
        self.speedMinimumValueLineEdit.raise_()
        self.shotSquareAngleMinimumValueLineEdit.raise_()
        self.backSpinMaximumValueLineEdit.raise_()
        self.backSpinStepSizeLineEdit.raise_()
        self.speedStepSizeLineEdit.raise_()
        self.defaultLocationLabel.raise_()
        self.shotSquareAngleStepSizeLineEdit.raise_()
        self.shotElevationAngleStepSizeLineEdit.raise_()
        self.backSpinUnitComboBox.raise_()
        self.speedUnitComboBox.raise_()
        self.shotSquareAngleUnitComboBox.raise_()
        self.shotElevationAngleUnitComboBox.raise_()
        self.line_2.raise_()
        self.shotElevationAngleFixedCheckBox.raise_()
        self.shotSquareAngleFixedCheckBox.raise_()
        self.speedFixedCheckBox.raise_()
        self.backSpinFixedCheckBox.raise_()
        self.label_5.raise_()
        self.defaultLocationComboBox.raise_()
        self.customHorizontalVerticalCheckBox.raise_()
        self.customDistanceXLabel.raise_()
        self.customDistanceXMinimumLineEdit.raise_()
        self.customDistanceRadialLabel.raise_()
        self.customDistanceYLabel.raise_()
        self.customRadialDistanceMinimumLineEdit.raise_()
        self.customDistanceYMinimumLineEdit.raise_()
        self.customDistanceAngleLabel.raise_()
        self.customRadialAngleMinimumLineEdit.raise_()
        self.customDistanceYMaximumLineEdit.raise_()
        self.customDistanceXMaximumLineEdit.raise_()
        self.customRadialDistanceMaximumLineEdit.raise_()
        self.customRadialAngleMaximumLineEdit.raise_()
        self.customRadialAngleUnitComboBox.raise_()
        self.customRadialDistanceUnitComboBox.raise_()
        self.customRadialDistanceAngleCheckBox.raise_()
        self.customDistanceUnitComboBox.raise_()
        self.customDistanceXStepSizeLineEdit.raise_()
        self.customDistanceYStepSizeLineEdit.raise_()
        self.customRadialDistanceStepSizeLineEdit.raise_()
        self.customRadialAngleStepSizeLineEdit.raise_()
        self.customDistanceXFixedCheckBox.raise_()
        self.customDistanceYFixedCheckBox.raise_()
        self.customRadialDistanceFixedCheckBox.raise_()
        self.customRadialAngleFixedCheckBox.raise_()
        self.runSimsPushButton = QtWidgets.QPushButton(self.tab)
        self.runSimsPushButton.setGeometry(QtCore.QRect(750, 370, 116, 28))
        self.runSimsPushButton.setObjectName("runSimsPushButton")
        self.simModeComboBox = QtWidgets.QComboBox(self.tab)
        self.simModeComboBox.setGeometry(QtCore.QRect(630, 370, 73, 22))
        self.simModeComboBox.setObjectName("simModeComboBox")
        self.simModeComboBox.addItem("")
        self.simModeComboBox.addItem("")
        self.simModeLabel = QtWidgets.QLabel(self.tab)
        self.simModeLabel.setGeometry(QtCore.QRect(630, 350, 71, 16))
        self.simModeLabel.setObjectName("simModeLabel")
        self.tabWidget.addTab(self.tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1337, 21))
        self.menubar.setObjectName("menubar")
        self.menutester = QtWidgets.QMenu(self.menubar)
        self.menutester.setObjectName("menutester")
        self.menutest1 = QtWidgets.QMenu(self.menutester)
        self.menutest1.setObjectName("menutest1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionView_History = QtWidgets.QAction(MainWindow)
        self.actionView_History.setObjectName("actionView_History")
        self.menutester.addAction(self.menutest1.menuAction())
        self.menutester.addAction(self.actionSave)
        self.menutester.addAction(self.actionView_History)
        self.menubar.addAction(self.menutester.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.customRadialAngleFixedCheckBox.toggled['bool'].connect(self.customRadialAngleStepSizeLineEdit.setDisabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceXMinimumLineEdit.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceYStepSizeLineEdit.setEnabled)
        self.shotElevationAngleFixedCheckBox.toggled['bool'].connect(self.shotElevationAngleMaximumValueLineEdit.setDisabled)
        self.shotSquareAngleFixedCheckBox.toggled['bool'].connect(self.shotSquareAngleMaximumValueLineEdit.setDisabled)
        self.customDistanceXFixedCheckBox.toggled['bool'].connect(self.customDistanceXMaximumLineEdit.setDisabled)
        self.speedFixedCheckBox.toggled['bool'].connect(self.speedMaximumValueLineEdit.setDisabled)
        self.customRadialAngleFixedCheckBox.toggled['bool'].connect(self.customRadialAngleMaximumLineEdit.setDisabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceYMaximumLineEdit.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceXFixedCheckBox.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceYFixedCheckBox.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialAngleFixedCheckBox.setEnabled)
        self.shotElevationAngleFixedCheckBox.toggled['bool'].connect(self.shotElevationAngleStepSizeLineEdit.setDisabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceUnitComboBox.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialAngleStepSizeLineEdit.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialDistanceMaximumLineEdit.setEnabled)
        self.customDistanceYFixedCheckBox.toggled['bool'].connect(self.customDistanceYStepSizeLineEdit.setDisabled)
        self.customRadialDistanceFixedCheckBox.toggled['bool'].connect(self.customRadialDistanceStepSizeLineEdit.setDisabled)
        self.customDistanceXFixedCheckBox.toggled['bool'].connect(self.customDistanceXStepSizeLineEdit.setDisabled)
        self.speedFixedCheckBox.toggled['bool'].connect(self.speedStepSizeLineEdit.setDisabled)
        self.shotSquareAngleFixedCheckBox.toggled['bool'].connect(self.shotSquareAngleStepSizeLineEdit.setDisabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialDistanceFixedCheckBox.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceXMaximumLineEdit.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialDistanceMinimumLineEdit.setEnabled)
        self.backSpinFixedCheckBox.toggled['bool'].connect(self.backSpinMaximumValueLineEdit.setDisabled)
        self.backSpinFixedCheckBox.toggled['bool'].connect(self.backSpinStepSizeLineEdit.setDisabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialAngleMinimumLineEdit.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialDistanceStepSizeLineEdit.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceXStepSizeLineEdit.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialAngleMaximumLineEdit.setEnabled)
        self.customHorizontalVerticalCheckBox.toggled['bool'].connect(self.customDistanceYMinimumLineEdit.setEnabled)
        self.customDistanceYFixedCheckBox.toggled['bool'].connect(self.customDistanceYMaximumLineEdit.setDisabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialAngleUnitComboBox.setEnabled)
        self.customRadialDistanceAngleCheckBox.toggled['bool'].connect(self.customRadialDistanceUnitComboBox.setEnabled)
        self.customRadialDistanceFixedCheckBox.toggled['bool'].connect(self.customRadialDistanceMaximumLineEdit.setDisabled)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.shotElevationAngleMinimumValueLineEdit, self.shotElevationAngleMaximumValueLineEdit)
        MainWindow.setTabOrder(self.shotElevationAngleMaximumValueLineEdit, self.shotElevationAngleStepSizeLineEdit)
        MainWindow.setTabOrder(self.shotElevationAngleStepSizeLineEdit, self.shotSquareAngleMinimumValueLineEdit)
        MainWindow.setTabOrder(self.shotSquareAngleMinimumValueLineEdit, self.shotSquareAngleMaximumValueLineEdit)
        MainWindow.setTabOrder(self.shotSquareAngleMaximumValueLineEdit, self.shotSquareAngleStepSizeLineEdit)
        MainWindow.setTabOrder(self.shotSquareAngleStepSizeLineEdit, self.speedMinimumValueLineEdit)
        MainWindow.setTabOrder(self.speedMinimumValueLineEdit, self.speedMaximumValueLineEdit)
        MainWindow.setTabOrder(self.speedMaximumValueLineEdit, self.speedStepSizeLineEdit)
        MainWindow.setTabOrder(self.speedStepSizeLineEdit, self.backSpinMinimumValueLineEdit)
        MainWindow.setTabOrder(self.backSpinMinimumValueLineEdit, self.backSpinMaximumValueLineEdit)
        MainWindow.setTabOrder(self.backSpinMaximumValueLineEdit, self.backSpinStepSizeLineEdit)
        MainWindow.setTabOrder(self.backSpinStepSizeLineEdit, self.customDistanceXMinimumLineEdit)
        MainWindow.setTabOrder(self.customDistanceXMinimumLineEdit, self.customDistanceXMaximumLineEdit)
        MainWindow.setTabOrder(self.customDistanceXMaximumLineEdit, self.customDistanceXStepSizeLineEdit)
        MainWindow.setTabOrder(self.customDistanceXStepSizeLineEdit, self.customDistanceYMinimumLineEdit)
        MainWindow.setTabOrder(self.customDistanceYMinimumLineEdit, self.customDistanceYMaximumLineEdit)
        MainWindow.setTabOrder(self.customDistanceYMaximumLineEdit, self.customDistanceYStepSizeLineEdit)
        MainWindow.setTabOrder(self.customDistanceYStepSizeLineEdit, self.customRadialDistanceMinimumLineEdit)
        MainWindow.setTabOrder(self.customRadialDistanceMinimumLineEdit, self.customRadialDistanceMaximumLineEdit)
        MainWindow.setTabOrder(self.customRadialDistanceMaximumLineEdit, self.customRadialDistanceStepSizeLineEdit)
        MainWindow.setTabOrder(self.customRadialDistanceStepSizeLineEdit, self.customRadialAngleMinimumLineEdit)
        MainWindow.setTabOrder(self.customRadialAngleMinimumLineEdit, self.customRadialAngleMaximumLineEdit)
        MainWindow.setTabOrder(self.customRadialAngleMaximumLineEdit, self.customRadialAngleStepSizeLineEdit)
        MainWindow.setTabOrder(self.customRadialAngleStepSizeLineEdit, self.simModeComboBox)
        MainWindow.setTabOrder(self.simModeComboBox, self.runSimsPushButton)
        MainWindow.setTabOrder(self.runSimsPushButton, self.shotElevationAngleFixedCheckBox)
        MainWindow.setTabOrder(self.shotElevationAngleFixedCheckBox, self.tabWidget)
        MainWindow.setTabOrder(self.tabWidget, self.customHorizontalVerticalCheckBox)
        MainWindow.setTabOrder(self.customHorizontalVerticalCheckBox, self.defaultLocationComboBox)
        MainWindow.setTabOrder(self.defaultLocationComboBox, self.shotSquareAngleUnitComboBox)
        MainWindow.setTabOrder(self.shotSquareAngleUnitComboBox, self.customRadialAngleUnitComboBox)
        MainWindow.setTabOrder(self.customRadialAngleUnitComboBox, self.customRadialDistanceUnitComboBox)
        MainWindow.setTabOrder(self.customRadialDistanceUnitComboBox, self.backSpinUnitComboBox)
        MainWindow.setTabOrder(self.backSpinUnitComboBox, self.customDistanceUnitComboBox)
        MainWindow.setTabOrder(self.customDistanceUnitComboBox, self.shotElevationAngleUnitComboBox)
        MainWindow.setTabOrder(self.shotElevationAngleUnitComboBox, self.speedUnitComboBox)
        MainWindow.setTabOrder(self.speedUnitComboBox, self.customRadialDistanceAngleCheckBox)
        MainWindow.setTabOrder(self.customRadialDistanceAngleCheckBox, self.speedFixedCheckBox)
        MainWindow.setTabOrder(self.speedFixedCheckBox, self.customDistanceXFixedCheckBox)
        MainWindow.setTabOrder(self.customDistanceXFixedCheckBox, self.customDistanceYFixedCheckBox)
        MainWindow.setTabOrder(self.customDistanceYFixedCheckBox, self.customRadialDistanceFixedCheckBox)
        MainWindow.setTabOrder(self.customRadialDistanceFixedCheckBox, self.customRadialAngleFixedCheckBox)
        MainWindow.setTabOrder(self.customRadialAngleFixedCheckBox, self.shotSquareAngleFixedCheckBox)
        MainWindow.setTabOrder(self.shotSquareAngleFixedCheckBox, self.backSpinFixedCheckBox)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.customHorizontalVerticalCheckBox.setText(_translate("MainWindow", "Custom Horizontal/Vertical"))
        self.defaultLocationLabel.setText(_translate("MainWindow", "Location"))
        self.defaultLocationComboBox.setItemText(0, _translate("MainWindow", "Free throw"))
        self.defaultLocationComboBox.setItemText(1, _translate("MainWindow", "Top of key"))
        self.defaultLocationComboBox.setItemText(2, _translate("MainWindow", "3-Point"))
        self.defaultLocationComboBox.setItemText(3, _translate("MainWindow", "Half court"))
        self.backSpinUnitComboBox.setItemText(0, _translate("MainWindow", "rad/s"))
        self.backSpinUnitComboBox.setItemText(1, _translate("MainWindow", "rev/min"))
        self.customDistanceXLabel.setText(_translate("MainWindow", "Horizontal"))
        self.shotElevationAngleFixedCheckBox.setToolTip(_translate("MainWindow", "Check to keep values fixed"))
        self.shotElevationAngleFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.shotSquareAngleLabel.setText(_translate("MainWindow", "Shot square angle"))
        self.label_6.setText(_translate("MainWindow", "Maximum value"))
        self.label_13.setText(_translate("MainWindow", "Step size"))
        self.label_5.setText(_translate("MainWindow", "Minumin value"))
        self.speedUnitComboBox.setItemText(0, _translate("MainWindow", "m/s"))
        self.speedUnitComboBox.setItemText(1, _translate("MainWindow", "mph"))
        self.speedFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.shotElevationAngleUnitComboBox.setItemText(0, _translate("MainWindow", "rad"))
        self.shotElevationAngleUnitComboBox.setItemText(1, _translate("MainWindow", "deg"))
        self.shotSquareAngleUnitComboBox.setItemText(0, _translate("MainWindow", "rad"))
        self.shotSquareAngleUnitComboBox.setItemText(1, _translate("MainWindow", "deg"))
        self.backSpinFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.shotElevationAngleLabel.setText(_translate("MainWindow", "Shot elevation angle"))
        self.customDistanceYLabel.setText(_translate("MainWindow", "Vertical"))
        self.backSpinLabel.setText(_translate("MainWindow", "Back spin"))
        self.shotSquareAngleFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.customDistanceRadialLabel.setText(_translate("MainWindow", "radial distance"))
        self.speedLabel.setText(_translate("MainWindow", "Speed"))
        self.customDistanceAngleLabel.setText(_translate("MainWindow", "angle"))
        self.customRadialAngleUnitComboBox.setItemText(0, _translate("MainWindow", "rad"))
        self.customRadialAngleUnitComboBox.setItemText(1, _translate("MainWindow", "deg"))
        self.customRadialDistanceUnitComboBox.setItemText(0, _translate("MainWindow", "m"))
        self.customRadialDistanceUnitComboBox.setItemText(1, _translate("MainWindow", "ft"))
        self.customRadialDistanceAngleCheckBox.setText(_translate("MainWindow", "Custom Radial Distance/Angle"))
        self.customDistanceUnitComboBox.setItemText(0, _translate("MainWindow", "m"))
        self.customDistanceUnitComboBox.setItemText(1, _translate("MainWindow", "ft"))
        self.customDistanceXFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.customDistanceYFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.customRadialDistanceFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.customRadialAngleFixedCheckBox.setText(_translate("MainWindow", "Fixed"))
        self.runSimsPushButton.setText(_translate("MainWindow", "Run Sims"))
        self.simModeComboBox.setItemText(0, _translate("MainWindow", "2D"))
        self.simModeComboBox.setItemText(1, _translate("MainWindow", "3D"))
        self.simModeLabel.setText(_translate("MainWindow", "Sim Mode"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Inputs"))
        self.menutester.setTitle(_translate("MainWindow", "Menu"))
        self.menutest1.setTitle(_translate("MainWindow", "Current session"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionView_History.setText(_translate("MainWindow", "View History"))
        self.actionView_History.setShortcut(_translate("MainWindow", "Ctrl+H"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
