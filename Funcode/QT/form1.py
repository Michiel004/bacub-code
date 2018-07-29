# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CodeGenerate.ui'
#
# Created: Sun Jul 29 21:03:17 2018
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

## my imports
import os, random, string

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_GenerateCode(object):
    def setupUi(self, GenerateCode):
        global length
        length = 16
        GenerateCode.setObjectName(_fromUtf8("GenerateCode"))
        GenerateCode.resize(403, 300)
        self.verticalLayout_5 = QtGui.QVBoxLayout(GenerateCode)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pushButton_Generate = QtGui.QPushButton(GenerateCode)
        self.pushButton_Generate.setObjectName(_fromUtf8("pushButton_Generate"))
        self.horizontalLayout_3.addWidget(self.pushButton_Generate)
        self.pushButton_Clear = QtGui.QPushButton(GenerateCode)
        self.pushButton_Clear.setObjectName(_fromUtf8("pushButton_Clear"))
        self.horizontalLayout_3.addWidget(self.pushButton_Clear)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.textOutput = QtGui.QTextEdit(GenerateCode)
        self.textOutput.setObjectName(_fromUtf8("textOutput"))
        self.verticalLayout_4.addWidget(self.textOutput)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        

        self.retranslateUi(GenerateCode)
        QtCore.QObject.connect(self.pushButton_Clear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.textOutput.clear)
        QtCore.QObject.connect(self.pushButton_Generate, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonClicked)
        QtCore.QMetaObject.connectSlotsByName(GenerateCode)

    def retranslateUi(self, GenerateCode):
        GenerateCode.setWindowTitle(_translate("GenerateCode", "GenerateCode", None))
        self.pushButton_Generate.setText(_translate("GenerateCode", "Generate", None))
        self.pushButton_Clear.setText(_translate("GenerateCode", "Clear", None))

    def pushButtonClicked(self):
        global length
        self.textOutput.clear()       
        code = "" 
        chars = string.ascii_letters + string.digits + '!@#$%^&*()_-'
        for i in range(length):
            code =  code + random.choice(chars)   

        self.textOutput.insertPlainText(code)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_GenerateCode()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
