# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 06:53:16 2021

@author: AsteriskAmpersand
"""

import sys
import os
from PyQt5 import uic, QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog
from mainWindow import Ui_MainWindow
from skinToneDialog import Ui_skinToneDialog
import SaveTools as ST
from pathlib import Path

def checkPath(path):
    return os.path.isfile(path)

STORIESTITLE = r""" _  _   __   __ _  ____  ____  ____  ____    _  _  _  _  __ _  ____  ____  ____    ____  ____  __  ____  __  ____  ____    ____ 
( \/ ) /  \ (  ( \/ ___)(_  _)(  __)(  _ \  / )( \/ )( \(  ( \(_  _)(  __)(  _ \  / ___)(_  _)/  \(  _ \(  )(  __)/ ___)  (___ \
/ \/ \(  O )/    /\___ \  )(   ) _)  )   /  ) __ () \/ (/    /  )(   ) _)  )   /  \___ \  )( (  O ))   / )(  ) _) \___ \   / __/
\_)(_/ \__/ \_)__)(____/ (__) (____)(__\_)  \_)(_/\____/\_)__) (__) (____)(__\_)  (____/ (__) \__/(__\_)(__)(____)(____/  (____)"""

TOOLTITLE =  r""" ____   __   _  _  ____    ____  ____   __   __ _  ____  ____  ____  ____     __   __ _  ____ 
/ ___) / _\ / )( \(  __)  (_  _)(  _ \ / _\ (  ( \/ ___)(  __)(  __)(  _ \   / _\ (  ( \(    \
\___ \/    \\ \/ / ) _)     )(   )   //    \/    /\___ \ ) _)  ) _)  )   /  /    \/    / ) D (
(____/\_/\_/ \__/ (____)   (__) (__\_)\_/\_/\_)__)(____/(__)  (____)(__\_)  \_/\_/\_)__)(____/
  ___  __   __ _  _  _  ____  ____  ____  __  __   __ _    ____  __    __   __                
 / __)/  \ (  ( \/ )( \(  __)(  _ \/ ___)(  )/  \ (  ( \  (_  _)/  \  /  \ (  )               
( (__(  O )/    /\ \/ / ) _)  )   /\___ \ )((  O )/    /    )( (  O )(  O )/ (_/\             
 \___)\__/ \_)__) \__/ (____)(__\_)(____/(__)\__/ \_)__)   (__) \__/  \__/ \____/"""
SPACE = "=========================================================================================================================="
                                                                           
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, arguments):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Ando-Asterisk Stories 2 Save Tool")
        if getattr(sys, 'frozen', False):
            application_path = sys._MEIPASS
        elif __file__:
            application_path = os.path.dirname(__file__)
        self.setWindowIcon(QtGui.QIcon(application_path+r"\resources\DodoSama.png"))
        self.connect()
        self.show()
        self.ui.console.append(STORIESTITLE)
        self.ui.console.append("")
        self.ui.console.append(TOOLTITLE)
        self.ui.console.append("")
        self.ui.console.append("==========================================================================================================================")
        self.ui.console.append("Written by Asterisk Ampersand with the help of Andoryuuta")
        self.ui.console.append("Ando: https://github.com/Andoryuuta")
        self.ui.console.append("Asterisk: https://github.com/AsteriskAmpersand")
        self.ui.console.append("")
        self.ui.console.append("This is a free tool, if you paid for it, you've been scammed")
        self.ui.console.append("You can find your Steam Id 64 here: https://www.steamidfinder.com/")
        self.ui.console.append("")
        self.ui.console.append("Thanks to Ando for his significant help reversing the encryption and key generation")
        self.ui.console.append("Thanks to Akantorex, Phemeto, ShinSeiKen and TheChief for their Saves and Testing")
        self.ui.console.append("==========================================================================================================================")
    def pathCheck(self,output):
        if not checkPath(self.ui.input.text()):
            output("Input file %s does not exist."%self.ui.input.text())
            return False
        if not self.ui.output.text():
            output("No output specified.")
            return False
        return True
    def execute(self):
        self.ui.console.append("Starting Conversion:")
        output = lambda x: self.ui.console.append(" "*4+str(x))
        if not self.pathCheck(output):
            return
        if self.ui.nsw.checkState():
            ST.filePCtoSwitch(self.ui.input.text(),self.ui.output.text(),output)
        else:            
            ST.fileTransfer(self.ui.input.text(),self.ui.steamid64.value(),self.ui.output.text(),output)
        self.ui.console.append(SPACE)
    def encrypt(self):
        self.ui.console.append("Starting Encryption:")
        output = lambda x: self.ui.console.append(" "*4+str(x))
        ST.encryptPC(self.ui.input.text(),self.ui.steamid64.value(),self.ui.output.text(),output)
        self.ui.console.append(SPACE)
    def decrypt(self):
        self.ui.console.append("Starting Decryption:")
        output = lambda x: self.ui.console.append(" "*4+str(x))
        ST.decryptPC(self.ui.input.text(),self.ui.output.text(),output)
        self.ui.console.append(SPACE)
    def fixSave(self):
        self.ui.console.append("Starting Fix Save (skin):")
        output = lambda x: self.ui.console.append(" "*4+str(x))
        chooser = SkinToneDialog()
        chooser.exec()
        ST.fixSave(self.ui.input.text(), self.ui.output.text(), self.ui.steamid64.value(), chooser.choice-1, output)
        self.ui.console.append(SPACE)
    def connect(self):
        self.ui.convert.clicked.connect(self.execute)
        self.ui.encrypt.clicked.connect(self.encrypt)
        self.ui.decrypt.clicked.connect(self.decrypt)
        self.ui.fixSave.clicked.connect(self.fixSave)
        self.ui.inputFind.clicked.connect(self.getInput)
        self.ui.outputFind.clicked.connect(self.getOutput)        
        
    def getInput(self):
       file = QFileDialog.getOpenFileName(self, "Open Input Folder", "*.sav")[0]
       if file:
           self.ui.input.setText(file)    
    def getOutput(self):
        file = QFileDialog.getSaveFileName(self, "Open Output File", "*.sav")[0]
        if file:
            self.ui.output.setText(file)


class SkinToneDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(SkinToneDialog, self).__init__(parent)
        self.ui = Ui_skinToneDialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.OkClicked)
        self.show()

    def OkClicked(self):
        self.choice = int(self.ui.skinColorButtonGroup.checkedButton().objectName().removeprefix('skinColorCheck'))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    args = app.arguments()[1:]
    window = MainWindow(args)
    sys.exit(app.exec_())