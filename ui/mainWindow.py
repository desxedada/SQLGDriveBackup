# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui',
# licensing of 'mainWindow.ui' applies.
#
# Created: Wed Dec 30 16:18:02 2020
#      by: pyside2-uic  running on PySide2 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(408, 831)
        mainWindow.setMinimumSize(QtCore.QSize(408, 831))
        mainWindow.setMaximumSize(QtCore.QSize(408, 831))
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(408, 790))
        self.centralwidget.setMaximumSize(QtCore.QSize(407, 790))
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 811))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 60, 47, 13))
        self.label.setText("")
        self.label.setObjectName("label")
        self.formGroupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.formGroupBox_2.setGeometry(QtCore.QRect(10, 40, 391, 151))
        self.formGroupBox_2.setAutoFillBackground(True)
        self.formGroupBox_2.setObjectName("formGroupBox_2")
        self.databaseLayout = QtWidgets.QFormLayout(self.formGroupBox_2)
        self.databaseLayout.setContentsMargins(10, 10, 10, 10)
        self.databaseLayout.setObjectName("databaseLayout")
        self.label_5 = QtWidgets.QLabel(self.formGroupBox_2)
        self.label_5.setObjectName("label_5")
        self.databaseLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.instanceBox = QtWidgets.QComboBox(self.formGroupBox_2)
        self.instanceBox.setObjectName("instanceBox")
        self.databaseLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.instanceBox)
        self.label_7 = QtWidgets.QLabel(self.formGroupBox_2)
        self.label_7.setObjectName("label_7")
        self.databaseLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.connectionLabel = QtWidgets.QLabel(self.formGroupBox_2)
        self.connectionLabel.setObjectName("connectionLabel")
        self.horizontalLayout.addWidget(self.connectionLabel)
        self.connectionButton = QtWidgets.QPushButton(self.formGroupBox_2)
        self.connectionButton.setObjectName("connectionButton")
        self.horizontalLayout.addWidget(self.connectionButton)
        self.okButton = QtWidgets.QPushButton(self.formGroupBox_2)
        self.okButton.setObjectName("okButton")
        self.horizontalLayout.addWidget(self.okButton)
        self.databaseLayout.setLayout(3, QtWidgets.QFormLayout.SpanningRole, self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.destEdit = QtWidgets.QLineEdit(self.formGroupBox_2)
        self.destEdit.setEnabled(False)
        self.destEdit.setObjectName("destEdit")
        self.horizontalLayout_4.addWidget(self.destEdit)
        self.chooseButton = QtWidgets.QPushButton(self.formGroupBox_2)
        self.chooseButton.setObjectName("chooseButton")
        self.horizontalLayout_4.addWidget(self.chooseButton)
        self.databaseLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(100, 10, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setObjectName("label_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(170, 730, 231, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.backupButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.backupButton.setObjectName("backupButton")
        self.horizontalLayout_2.addWidget(self.backupButton)
        self.logBox = QtWidgets.QGroupBox(self.frame)
        self.logBox.setGeometry(QtCore.QRect(10, 200, 391, 303))
        self.logBox.setAutoFillBackground(True)
        self.logBox.setObjectName("logBox")
        self.gridLayout = QtWidgets.QGridLayout(self.logBox)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(self.logBox)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.databaseListWidget = QtWidgets.QListWidget(self.logBox)
        self.databaseListWidget.setObjectName("databaseListWidget")
        self.gridLayout.addWidget(self.databaseListWidget, 2, 0, 1, 1)
        self.logtextEdit = QtWidgets.QTextEdit(self.logBox)
        self.logtextEdit.setObjectName("logtextEdit")
        self.gridLayout.addWidget(self.logtextEdit, 4, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.logBox)
        self.label_10.setAutoFillBackground(True)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 0, 1, 1)
        self.scheduleGroupBox = QtWidgets.QGroupBox(self.frame)
        self.scheduleGroupBox.setGeometry(QtCore.QRect(10, 500, 391, 191))
        self.scheduleGroupBox.setAutoFillBackground(True)
        self.scheduleGroupBox.setObjectName("scheduleGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scheduleGroupBox)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_9 = QtWidgets.QLabel(self.scheduleGroupBox)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_9.addWidget(self.label_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem2)
        self.enableCheckBox = QtWidgets.QCheckBox(self.scheduleGroupBox)
        self.enableCheckBox.setObjectName("enableCheckBox")
        self.horizontalLayout_9.addWidget(self.enableCheckBox)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(5, -1, 5, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scheduleGroupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.scheduleTimeEdit = QtWidgets.QTimeEdit(self.scheduleGroupBox)
        self.scheduleTimeEdit.setObjectName("scheduleTimeEdit")
        self.horizontalLayout_3.addWidget(self.scheduleTimeEdit)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.setButton = QtWidgets.QPushButton(self.scheduleGroupBox)
        self.setButton.setObjectName("setButton")
        self.horizontalLayout_6.addWidget(self.setButton)
        self.resetButton = QtWidgets.QPushButton(self.scheduleGroupBox)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout_6.addWidget(self.resetButton)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.scheduleBackupLabel = QtWidgets.QLabel(self.scheduleGroupBox)
        self.scheduleBackupLabel.setEnabled(True)
        self.scheduleBackupLabel.setObjectName("scheduleBackupLabel")
        self.horizontalLayout_10.addWidget(self.scheduleBackupLabel)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 408, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuLicense = QtWidgets.QMenu(self.menuBar)
        self.menuLicense.setObjectName("menuLicense")
        mainWindow.setMenuBar(self.menuBar)
        self.actionLicense = QtWidgets.QAction(mainWindow)
        self.actionLicense.setObjectName("actionLicense")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionSQL_Authentication = QtWidgets.QAction(mainWindow)
        self.actionSQL_Authentication.setObjectName("actionSQL_Authentication")
        self.menuLicense.addAction(self.actionLicense)
        self.menuLicense.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuLicense.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QtWidgets.QApplication.translate("mainWindow", "SQLServerBackupTool", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("mainWindow", "Server Name", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("mainWindow", "Backup Destination", None, -1))
        self.connectionLabel.setText(QtWidgets.QApplication.translate("mainWindow", "TextLabel", None, -1))
        self.connectionButton.setText(QtWidgets.QApplication.translate("mainWindow", "Test Connection", None, -1))
        self.okButton.setText(QtWidgets.QApplication.translate("mainWindow", "Ok", None, -1))
        self.chooseButton.setText(QtWidgets.QApplication.translate("mainWindow", "Choose", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("mainWindow", "SQL SERVER BACKUP TOOL", None, -1))
        self.backupButton.setText(QtWidgets.QApplication.translate("mainWindow", "Apply", None, -1))
        self.label_11.setText(QtWidgets.QApplication.translate("mainWindow", "Log", None, -1))
        self.label_10.setText(QtWidgets.QApplication.translate("mainWindow", "Databases", None, -1))
        self.label_9.setText(QtWidgets.QApplication.translate("mainWindow", "Schedule Backups", None, -1))
        self.enableCheckBox.setText(QtWidgets.QApplication.translate("mainWindow", "Enabled", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("mainWindow", "Full Backup Daily at", None, -1))
        self.setButton.setText(QtWidgets.QApplication.translate("mainWindow", "Set schedule", None, -1))
        self.resetButton.setText(QtWidgets.QApplication.translate("mainWindow", "Reset", None, -1))
        self.scheduleBackupLabel.setText(QtWidgets.QApplication.translate("mainWindow", "Next Schedule:", None, -1))
        self.menuLicense.setTitle(QtWidgets.QApplication.translate("mainWindow", "Help", None, -1))
        self.actionLicense.setText(QtWidgets.QApplication.translate("mainWindow", "License", None, -1))
        self.actionAbout.setText(QtWidgets.QApplication.translate("mainWindow", "About", None, -1))
        self.actionSQL_Authentication.setText(QtWidgets.QApplication.translate("mainWindow", "SQL Authentication", None, -1))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())

