# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'link_reader.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LinkReader(object):
    def setupUi(self, LinkReader):
        LinkReader.setObjectName("LinkReader")
        LinkReader.resize(486, 109)
        self.textEdit = QtWidgets.QTextEdit(LinkReader)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 401, 31))
        self.textEdit.setInputMethodHints(QtCore.Qt.ImhMultiLine|QtCore.Qt.ImhUrlCharactersOnly)
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(LinkReader)
        self.label.setGeometry(QtCore.QRect(70, 10, 281, 20))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(LinkReader)
        self.pushButton.setGeometry(QtCore.QRect(430, 40, 41, 25))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(LinkReader)
        QtCore.QMetaObject.connectSlotsByName(LinkReader)

    def retranslateUi(self, LinkReader):
        _translate = QtCore.QCoreApplication.translate
        LinkReader.setWindowTitle(_translate("LinkReader", "Open URL"))
        self.label.setText(_translate("LinkReader", "Enter your link: "))
        self.pushButton.setText(_translate("LinkReader", "Ok"))


