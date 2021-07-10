# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 07:19:01 2021

@author: AsteriskAmpersand
"""
from PyQt5 import uic, QtWidgets, QtGui, QtCore

class BigIntSpinbox(QtWidgets.QAbstractSpinBox):

    def __init__(self, parent=None):
        super(BigIntSpinbox, self).__init__(parent)

        self._singleStep = 1
        self._minimum = -18446744073709551616
        self._maximum = 18446744073709551615

        self.lineEdit = QtWidgets.QLineEdit(self)

        rx = QtCore.QRegExp("[1-9]\\d{0,20}")
        validator = QtGui.QRegExpValidator(rx, self)

        self.lineEdit.setValidator(validator)
        self.setLineEdit(self.lineEdit)

    def value(self):
        try:
            return int(self.lineEdit.text())
        except:
            #raise
            return 0

    def setValue(self, value):
        if self._valueInRange(value):
            self.lineEdit.setText(str(value))

    def stepBy(self, steps):
        self.setValue(self.value() + steps*self.singleStep())

    def stepEnabled(self):
        return self.StepUpEnabled | self.StepDownEnabled

    def setSingleStep(self, singleStep):
        assert isinstance(singleStep, int)
        # don't use negative values
        self._singleStep = abs(singleStep)

    def singleStep(self):
        return self._singleStep

    def minimum(self):
        return self._minimum

    def setMinimum(self, minimum):
        assert isinstance(minimum, int)
        self._minimum = minimum

    def maximum(self):
        return self._maximum

    def setMaximum(self, maximum):
        assert isinstance(maximum, int)
        self._maximum = maximum

    def _valueInRange(self, value):
        if value >= self.minimum() and value <= self.maximum():
            return True
        else:
            return False