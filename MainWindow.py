# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Wed Nov 11 09:48:08 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!
from database import DatabaseHelper
from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 621)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 551, 621))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 150, 391, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.authTypeBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.authTypeBox.setObjectName("authTypeBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.authTypeBox)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.usernameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.usernameEdit.setObjectName("usernameEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.usernameEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pwdEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.pwdEdit.setObjectName("pwdEdit")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pwdEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 391, 51))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(10, 10, 10, 10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.instanceBox = QtWidgets.QComboBox(self.formLayoutWidget_2)
        self.instanceBox.setObjectName("instanceBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.instanceBox)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 20, 201, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.okButton = QtWidgets.QPushButton(self.frame)
        self.okButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.okButton.setObjectName("okButton")
        self.backupButton = QtWidgets.QPushButton(self.frame)
        self.backupButton.setGeometry(QtCore.QRect(320, 560, 81, 31))
        self.backupButton.setObjectName("backupButton")
        self.connectionButton = QtWidgets.QPushButton(self.frame)
        self.connectionButton.setGeometry(QtCore.QRect(10, 270, 101, 21))
        self.connectionButton.setObjectName("connectionButton")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 310, 391, 231))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 0, 0)
        self.formLayout_3.setObjectName("formLayout_3")
        self.databaseTreeView = QtWidgets.QTreeView(self.formLayoutWidget_3)
        self.databaseTreeView.setObjectName("databaseTreeView")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.databaseTreeView)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "SQLBackupTool", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "Username", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Password", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "Authentication", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("MainWindow", "Server Name", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("MainWindow", "SQL SERVER BACKUP TOOL", None, -1))
        self.okButton.setText(QtWidgets.QApplication.translate("MainWindow", "Ok", None, -1))
        self.backupButton.setText(QtWidgets.QApplication.translate("MainWindow", "Backup", None, -1))
        self.connectionButton.setText(QtWidgets.QApplication.translate("MainWindow", "Test Connection", None, -1))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

