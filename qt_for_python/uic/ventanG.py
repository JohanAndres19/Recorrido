# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\ciencias 2.2\Recorrido\ventanG.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ventanG(object):
    def setupUi(self, ventanG):
        ventanG.setObjectName("ventanG")
        ventanG.resize(713, 486)
        self.centralwidget = QtWidgets.QWidget(ventanG)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 79, 321, 341))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(360, 80, 321, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 201, 22))
        self.comboBox.setObjectName("comboBox")
        self.boton_dibujar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dibujar.setGeometry(QtCore.QRect(500, 40, 111, 23))
        self.boton_dibujar.setObjectName("boton_dibujar")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(320, 40, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        ventanG.setCentralWidget(self.centralwidget)

        self.retranslateUi(ventanG)
        QtCore.QMetaObject.connectSlotsByName(ventanG)

    def retranslateUi(self, ventanG):
        _translate = QtCore.QCoreApplication.translate
        ventanG.setWindowTitle(_translate("ventanG", "MainWindow"))
        self.boton_dibujar.setText(_translate("ventanG", "Dibujar"))
