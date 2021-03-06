# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'skinToneDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_skinToneDialog(object):
    def setupUi(self, skinToneDialog):
        skinToneDialog.setObjectName("skinToneDialog")
        skinToneDialog.resize(343, 281)
        self.buttonBox = QtWidgets.QDialogButtonBox(skinToneDialog)
        self.buttonBox.setGeometry(QtCore.QRect(130, 240, 70, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(skinToneDialog)
        self.widget.setGeometry(QtCore.QRect(20, 10, 301, 212))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.skinColorCheck1 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck1.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck1.setStyleSheet("background-color: #874126")
        self.skinColorCheck1.setText("")
        self.skinColorCheck1.setChecked(True)
        self.skinColorCheck1.setObjectName("skinColorCheck1")
        self.skinColorButtonGroup = QtWidgets.QButtonGroup(skinToneDialog)
        self.skinColorButtonGroup.setObjectName("skinColorButtonGroup")
        self.skinColorButtonGroup.addButton(self.skinColorCheck1)
        self.verticalLayout_3.addWidget(self.skinColorCheck1)
        self.skinColorCheck2 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck2.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck2.setStyleSheet("\n"
"background-color: #B86A37")
        self.skinColorCheck2.setText("")
        self.skinColorCheck2.setObjectName("skinColorCheck2")
        self.skinColorButtonGroup.addButton(self.skinColorCheck2)
        self.verticalLayout_3.addWidget(self.skinColorCheck2)
        self.skinColorCheck3 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck3.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck3.setStyleSheet("\n"
"background-color: #DE884D")
        self.skinColorCheck3.setText("")
        self.skinColorCheck3.setObjectName("skinColorCheck3")
        self.skinColorButtonGroup.addButton(self.skinColorCheck3)
        self.verticalLayout_3.addWidget(self.skinColorCheck3)
        self.skinColorCheck4 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck4.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck4.setStyleSheet("\n"
"background-color: #EA9F5A")
        self.skinColorCheck4.setText("")
        self.skinColorCheck4.setObjectName("skinColorCheck4")
        self.skinColorButtonGroup.addButton(self.skinColorCheck4)
        self.verticalLayout_3.addWidget(self.skinColorCheck4)
        self.skinColorCheck5 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck5.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck5.setStyleSheet("\n"
"background-color: #F9B972")
        self.skinColorCheck5.setText("")
        self.skinColorCheck5.setObjectName("skinColorCheck5")
        self.skinColorButtonGroup.addButton(self.skinColorCheck5)
        self.verticalLayout_3.addWidget(self.skinColorCheck5)
        self.skinColorCheck6 = QtWidgets.QRadioButton(self.widget)
        self.skinColorCheck6.setMinimumSize(QtCore.QSize(0, 30))
        self.skinColorCheck6.setStyleSheet("background-color: #FFCB8B")
        self.skinColorCheck6.setText("")
        self.skinColorCheck6.setObjectName("skinColorCheck6")
        self.skinColorButtonGroup.addButton(self.skinColorCheck6)
        self.verticalLayout_3.addWidget(self.skinColorCheck6)

        self.retranslateUi(skinToneDialog)
        self.buttonBox.rejected.connect(skinToneDialog.reject)
        self.buttonBox.accepted.connect(skinToneDialog.accept)
        QtCore.QMetaObject.connectSlotsByName(skinToneDialog)

    def retranslateUi(self, skinToneDialog):
        _translate = QtCore.QCoreApplication.translate
        skinToneDialog.setWindowTitle(_translate("skinToneDialog", "Choose Skin Tone"))
