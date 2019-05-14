# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Demo(object):
    def setupUi(self, Demo):
        Demo.setObjectName("Demo")
        Demo.resize(579, 224)
        self.centralwidget = QtWidgets.QWidget(Demo)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(101, 85, 110, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(257, 83, 110, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(408, 82, 110, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        Demo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Demo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 22))
        self.menubar.setObjectName("menubar")
        Demo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Demo)
        self.statusbar.setObjectName("statusbar")
        Demo.setStatusBar(self.statusbar)

        self.retranslateUi(Demo)
        QtCore.QMetaObject.connectSlotsByName(Demo)

    def retranslateUi(self, Demo):
        _translate = QtCore.QCoreApplication.translate
        Demo.setWindowTitle(_translate("Demo", "MainWindow"))
        self.pushButton.setText(_translate("Demo", "A"))
        self.pushButton_2.setText(_translate("Demo", "B"))
        self.pushButton_3.setText(_translate("Demo", "C"))


