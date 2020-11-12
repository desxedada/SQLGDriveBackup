# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Thu Nov 12 14:54:44 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets, Q

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(416, 715)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 701))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 180, 391, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.authLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.authLayout.setContentsMargins(10, 10, 10, 10)
        self.authLayout.setObjectName("authLayout")
        self.authTypeBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.authTypeBox.setObjectName("authTypeBox")
        self.authLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.authTypeBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.authLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.usernameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.authLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.authLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pwdEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pwdEdit.setObjectName("pwdEdit")
        self.authLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pwdEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.authLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 80, 391, 71))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.databaseLayout = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.databaseLayout.setContentsMargins(10, 10, 10, 10)
        self.databaseLayout.setObjectName("databaseLayout")
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.databaseLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.instanceBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.instanceBox.setObjectName("instanceBox")
        self.databaseLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.instanceBox)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_7.setObjectName("label_7")
        self.databaseLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.destinationBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.destinationBox.setObjectName("destinationBox")
        self.databaseLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.destinationBox)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.okButton = QtWidgets.QPushButton(self.frame)
        self.okButton.setGeometry(QtCore.QRect(320, 300, 75, 23))
        self.okButton.setObjectName("okButton")
        self.backupButton = QtWidgets.QPushButton(self.frame)
        self.backupButton.setGeometry(QtCore.QRect(320, 630, 81, 31))
        self.backupButton.setObjectName("backupButton")
        self.connectionButton = QtWidgets.QPushButton(self.frame)
        self.connectionButton.setGeometry(QtCore.QRect(10, 300, 101, 21))
        self.connectionButton.setObjectName("connectionButton")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 430, 391, 181))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.listLayout = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.listLayout.setContentsMargins(0, 0, 0, 0)
        self.listLayout.setObjectName("listLayout")
        self.databaseTreeView = QtWidgets.QTreeView(self.formLayoutWidget_3)
        self.databaseTreeView.setObjectName("databaseTreeView")
        self.listLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.databaseTreeView)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 416, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuLicense = QtWidgets.QMenu(self.menuBar)
        self.menuLicense.setObjectName("menuLicense")
        mainWindow.setMenuBar(self.menuBar)
        self.actionLicense = QtWidgets.QAction(mainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuLicense.addAction(self.actionLicense)
        self.menuLicense.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuLicense.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "MainWindow", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("mainWindow", "Username", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("mainWindow", "Password", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("mainWindow", "Authentication", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("mainWindow", "Server Name", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("mainWindow", "Backup Destination", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("mainWindow", "SQL SERVER BACKUP TOOL", None, -1))
        self.okButton.setText(QtWidgets.QApplication.translate("mainWindow", "Ok", None, -1))
        self.backupButton.setText(QtWidgets.QApplication.translate("mainWindow", "Backup", None, -1))
        self.connectionButton.setText(QtWidgets.QApplication.translate("mainWindow", "Test Connection", None, -1))
        self.menuLicense.setTitle(QtWidgets.QApplication.translate("mainWindow", "License", None, -1))
        self.actionLicense.setText(QtWidgets.QApplication.translate("mainWindow", "License", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("mainWindow", "About", None, -1))


