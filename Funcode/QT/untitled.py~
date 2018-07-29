# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Sat Jul 28 23:07:38 2018
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(400, 300)
        Form.setAutoFillBackground(True)
        self.plainTextEdit = QtGui.QPlainTextEdit(Form)
        self.plainTextEdit.setGeometry(QtCore.QRect(-20, 51, 421, 361))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushClear = QtGui.QPushButton(Form)
        self.pushClear.setGeometry(QtCore.QRect(280, 0, 111, 51))
        self.pushClear.setObjectName(_fromUtf8("pushClear"))
        self.pushGenerate = QtGui.QPushButton(Form)
        self.pushGenerate.setGeometry(QtCore.QRect(120, 0, 111, 51))
        self.pushGenerate.setObjectName(_fromUtf8("pushGenerate"))

        self.retranslateUi(Form)
        QtCore.QObject.connect(self.pushClear, QtCore.SIGNAL(_fromUtf8("clicked()")), self.plainTextEdit.clear)
        QtCore.QObject.connect(self.pushGenerate, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pushButtonClicked)
        self.plainTextEdit.insertPlainText("dfgdffdgdfdfgg")
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushClear.setText(_translate("Form", "Clear", None))
        self.pushGenerate.setText(_translate("Form", "Generate", None))

    def pushButtonClicked(self):
        self.plainTextEdit.clear       
        code = "" 
        length = 100
        chars = string.ascii_letters + string.digits + '!@#$%^&*()_-'
        for i in range(length):
            code =  code + random.choice(chars)   
        self.plainTextEdit.insertPlainText(code)

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

