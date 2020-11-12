# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow.ui',
# licensing of 'aboutWindow.ui' applies.
#
# Created: Thu Nov 12 14:55:45 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_aboutWindow(object):
    def setupUi(self, aboutWindow):
        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(436, 211)
        font = QtGui.QFont()
        font.setPointSize(12)
        aboutWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(aboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 151))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.versionLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.versionLabel.setObjectName("versionLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.versionLabel)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.licenseLabel = QtWidgets.QLabel(self.formLayoutWidget)
        self.licenseLabel.setObjectName("licenseLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.licenseLabel)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(340, 160, 75, 23))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        aboutWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(aboutWindow)
        self.statusbar.setObjectName("statusbar")
        aboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        aboutWindow.setWindowTitle(QtWidgets.QApplication.translate("aboutWindow", "About", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("aboutWindow", "Version:", None, -1))
        self.versionLabel.setText(QtWidgets.QApplication.translate("aboutWindow", "TextLabel", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("aboutWindow", "License:", None, -1))
        self.licenseLabel.setText(QtWidgets.QApplication.translate("aboutWindow", "TextLabel", None, -1))
        self.pushButton.setText(QtWidgets.QApplication.translate("aboutWindow", "OK", None, -1))

