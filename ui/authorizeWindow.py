# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authorizeWindow.ui',
# licensing of 'authorizeWindow.ui' applies.
#
# Created: Wed Nov 18 16:02:14 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_authorizeWindow(object):
    def setupUi(self, authorizeWindow):
        authorizeWindow.setObjectName("authorizeWindow")
        authorizeWindow.resize(424, 163)
        self.centralwidget = QtWidgets.QWidget(authorizeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 421, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.buttonBox_2 = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox_2.setGeometry(QtCore.QRect(0, 110, 421, 31))
        self.buttonBox_2.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox_2.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox_2.setObjectName("buttonBox_2")
        authorizeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(authorizeWindow)
        self.statusbar.setObjectName("statusbar")
        authorizeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(authorizeWindow)
        QtCore.QMetaObject.connectSlotsByName(authorizeWindow)

    def retranslateUi(self, authorizeWindow):
        authorizeWindow.setWindowTitle(QtWidgets.QApplication.translate("authorizeWindow", "Authorize Google Drive", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("authorizeWindow", "Authorization Code", None, -1))


    def show(self):
     import sys
     app = QtWidgets.QApplication(sys.argv)
     authorizeWindow = QtWidgets.QMainWindow()
     ui = Ui_authorizeWindow()
     ui.setupUi(authorizeWindow)
     authorizeWindow.show()
     sys.exit(app.exec_())

