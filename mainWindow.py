# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1026, 1124)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lCMM_8 = QtWidgets.QLabel(self.centralwidget)
        self.lCMM_8.setObjectName("lCMM_8")
        self.gridLayout_4.addWidget(self.lCMM_8, 0, 0, 1, 1)
        self.input = QtWidgets.QLineEdit(self.centralwidget)
        self.input.setObjectName("input")
        self.gridLayout_4.addWidget(self.input, 0, 1, 1, 1)
        self.inputFind = QtWidgets.QPushButton(self.centralwidget)
        self.inputFind.setObjectName("inputFind")
        self.gridLayout_4.addWidget(self.inputFind, 0, 2, 1, 1)
        self.outputFind = QtWidgets.QPushButton(self.centralwidget)
        self.outputFind.setObjectName("outputFind")
        self.gridLayout_4.addWidget(self.outputFind, 1, 2, 1, 1)
        self.output = QtWidgets.QLineEdit(self.centralwidget)
        self.output.setObjectName("output")
        self.gridLayout_4.addWidget(self.output, 1, 1, 1, 1)
        self.lCMM_3 = QtWidgets.QLabel(self.centralwidget)
        self.lCMM_3.setObjectName("lCMM_3")
        self.gridLayout_4.addWidget(self.lCMM_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.steamid64 = BigIntSpinbox(self.centralwidget)
        self.steamid64.setMinimumSize(QtCore.QSize(180, 0))
        self.steamid64.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.steamid64.setButtonSymbols(QtWidgets.QAbstractSpinBox.NoButtons)
        self.steamid64.setMaximum(999999999)
        self.steamid64.setObjectName("steamid64")
        self.horizontalLayout_2.addWidget(self.steamid64)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_9.addLayout(self.gridLayout_4)
        self.nsw = QtWidgets.QCheckBox(self.centralwidget)
        self.nsw.setObjectName("nsw")
        self.verticalLayout_9.addWidget(self.nsw)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.convert = QtWidgets.QPushButton(self.centralwidget)
        self.convert.setObjectName("convert")
        self.horizontalLayout_3.addWidget(self.convert)
        self.encrypt = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt.setObjectName("encrypt")
        self.horizontalLayout_3.addWidget(self.encrypt)
        self.decrypt = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt.setObjectName("decrypt")
        self.horizontalLayout_3.addWidget(self.decrypt)
        self.verticalLayout_9.addLayout(self.horizontalLayout_3)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_9.addWidget(self.line_2)
        self.verticalLayout.addLayout(self.verticalLayout_9)
        self.console = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        self.console.setFont(font)
        self.console.setReadOnly(True)
        self.console.setObjectName("console")
        self.verticalLayout.addWidget(self.console)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1026, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lCMM_8.setText(_translate("MainWindow", "Input Save"))
        self.inputFind.setText(_translate("MainWindow", "..."))
        self.outputFind.setText(_translate("MainWindow", "..."))
        self.lCMM_3.setText(_translate("MainWindow", "Output Save"))
        self.label.setText(_translate("MainWindow", "Steam ID64"))
        self.nsw.setText(_translate("MainWindow", "Convert to Switch"))
        self.convert.setText(_translate("MainWindow", "Convert"))
        self.encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.decrypt.setText(_translate("MainWindow", "Decrypt"))

from BigIntSpinbox import BigIntSpinbox

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
