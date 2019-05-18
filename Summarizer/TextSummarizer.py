# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TextSummarizer.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(923, 616)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 510, 221, 41))
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 80, 401, 391))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(530, 80, 351, 391))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(580, 20, 271, 17))
        self.label_2.setObjectName("label_2")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(680, 40, 48, 26))
        self.spinBox.setMinimum(1)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 411, 31))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 923, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_text_file = QtWidgets.QAction(MainWindow)
        self.actionOpen_text_file.setObjectName("actionOpen_text_file")
        self.actionSummarization_method = QtWidgets.QAction(MainWindow)
        self.actionSummarization_method.setObjectName("actionSummarization_method")
        self.actionOpen_text_from_url = QtWidgets.QAction(MainWindow)
        self.actionOpen_text_from_url.setObjectName("actionOpen_text_from_url")
        self.actionView_help_on_File_menu = QtWidgets.QAction(MainWindow)
        self.actionView_help_on_File_menu.setObjectName("actionView_help_on_File_menu")
        self.actionView_help_on_summary = QtWidgets.QAction(MainWindow)
        self.actionView_help_on_summary.setObjectName("actionView_help_on_summary")
        self.actionGeneral_help = QtWidgets.QAction(MainWindow)
        self.actionGeneral_help.setObjectName("actionGeneral_help")
        self.actionFile_menu_help = QtWidgets.QAction(MainWindow)
        self.actionFile_menu_help.setObjectName("actionFile_menu_help")
        self.actionSummarization_help = QtWidgets.QAction(MainWindow)
        self.actionSummarization_help.setObjectName("actionSummarization_help")
        self.actionGeneral_help_2 = QtWidgets.QAction(MainWindow)
        self.actionGeneral_help_2.setObjectName("actionGeneral_help_2")
        self.menuFile.addAction(self.actionOpen_text_file)
        self.menuFile.addAction(self.actionOpen_text_from_url)
        self.menuHelp.addAction(self.actionGeneral_help_2)
        self.menuHelp.addAction(self.actionFile_menu_help)
        self.menuHelp.addAction(self.actionSummarization_help)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TextSummarization"))
        self.pushButton.setText(_translate("MainWindow", "Summarize"))
        self.label_2.setText(_translate("MainWindow", "Enter number of sentences in summary: "))
        self.label.setText(_translate("MainWindow", "0 sentences in source text"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionOpen_text_file.setText(_translate("MainWindow", "Open text file..."))
        self.actionSummarization_method.setText(_translate("MainWindow", "Summarization method"))
        self.actionOpen_text_from_url.setText(_translate("MainWindow", "Open text from url"))
        self.actionView_help_on_File_menu.setText(_translate("MainWindow", "Help on File menu "))
        self.actionView_help_on_summary.setText(_translate("MainWindow", "Help on summary"))
        self.actionGeneral_help.setText(_translate("MainWindow", "General help"))
        self.actionFile_menu_help.setText(_translate("MainWindow", "File menu help"))
        self.actionSummarization_help.setText(_translate("MainWindow", "Summarization help"))
        self.actionGeneral_help_2.setText(_translate("MainWindow", "General help"))


