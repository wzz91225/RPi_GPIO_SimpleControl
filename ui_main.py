# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(585, 394)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 401, 71))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit_DC = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_DC.setObjectName("lineEdit_DC")
        self.horizontalLayout.addWidget(self.lineEdit_DC)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_DC_UP = QtWidgets.QPushButton(self.widget)
        self.button_DC_UP.setObjectName("button_DC_UP")
        self.verticalLayout.addWidget(self.button_DC_UP)
        self.button_DC_DOWN = QtWidgets.QPushButton(self.widget)
        self.button_DC_DOWN.setObjectName("button_DC_DOWN")
        self.verticalLayout.addWidget(self.button_DC_DOWN)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_FRE = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_FRE.setObjectName("lineEdit_FRE")
        self.horizontalLayout_2.addWidget(self.lineEdit_FRE)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_FRE_UP = QtWidgets.QPushButton(self.widget)
        self.button_FRE_UP.setObjectName("button_FRE_UP")
        self.verticalLayout_2.addWidget(self.button_FRE_UP)
        self.button_FRE_DOWN = QtWidgets.QPushButton(self.widget)
        self.button_FRE_DOWN.setObjectName("button_FRE_DOWN")
        self.verticalLayout_2.addWidget(self.button_FRE_DOWN)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_DC_UP.setText(_translate("MainWindow", "DC+"))
        self.button_DC_DOWN.setText(_translate("MainWindow", "DC-"))
        self.button_FRE_UP.setText(_translate("MainWindow", "Fre+"))
        self.button_FRE_DOWN.setText(_translate("MainWindow", "Fre-"))