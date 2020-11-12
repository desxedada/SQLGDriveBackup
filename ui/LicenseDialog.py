# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'licenseDialog.ui',
# licensing of 'licenseDialog.ui' applies.
#
# Created: Thu Nov 12 14:55:15 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_licenseDialog(object):
    def setupUi(self, licenseDialog):
        licenseDialog.setObjectName("licenseDialog")
        licenseDialog.resize(434, 133)
        self.buttonBox = QtWidgets.QDialogButtonBox(licenseDialog)
        self.buttonBox.setGeometry(QtCore.QRect(0, 81, 421, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayoutWidget = QtWidgets.QWidget(licenseDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 431, 80))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)

        self.retranslateUi(licenseDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), licenseDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), licenseDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(licenseDialog)

    def retranslateUi(self, licenseDialog):
        licenseDialog.setWindowTitle(QtWidgets.QApplication.translate("licenseDialog", "License", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("licenseDialog", "Enter License", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("licenseDialog", "Version", None, -1))

