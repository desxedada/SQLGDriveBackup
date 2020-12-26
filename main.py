import os
import sys

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QFile, QIODevice, QObject
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from os.path import expanduser

from ui.mainWindow import Ui_mainWindow
from common.DatabaseHelper import DatabaseHelper
from common.windows import Registry


class Main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super(Main,self).__init__()

        #Variables
        self.scheduleTimeNotify = ""

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.connectionButton.clicked.connect(self.testConnection)
        self.ui.connectionButton.show()
        self.registry = Registry()
        self.server_name = self.ui.instanceBox.currentText()
        self.ui.scheduleBackupLabel.setText(self.scheduleTimeNotify)
        self.ui.setButton.setEnabled(False)
        self.ui.resetButton.setEnabled(False)
        self.ui.centralwidget.setMaximumHeight(790)
        self.ui.centralwidget.setMaximumWidth(407)
        self.ui.scheduleBackupLabel.setVisible(False)

        self.ui.tray_icon = QSystemTrayIcon(self)
        self.ui.tray_icon.setIcon(QIcon("database-logo.png"))

        self.show_action = QAction("Show", self)
        self.quit_action = QAction("Exit", self)
        self.hide_action = QAction("Hide", self)

        self.tray_menu = QMenu()
        self.tray_menu.addAction(self.show_action)
        self.tray_menu.addAction(self.hide_action)
        self.tray_menu.addAction(self.quit_action)

        self.show_action.triggered.connect(lambda: self.setVisible(True))
        self.hide_action.triggered.connect(lambda:  self.setVisible(False))
        self.quit_action.triggered.connect(lambda: sys.exit())

        self.ui.tray_icon.setContextMenu(self.tray_menu)
        self.ui.tray_icon.show()



        self.ui.instanceBox.activated.connect(self.handleComboActivated)

        self.ui.chooseButton.clicked.connect(self.chooseDirectory)
        self.ui.enableCheckBox.stateChanged.connect(self.onCheckBoxState)
        self.ui.destinationBox.activated[str].connect(self.onDestChanged)
        self.ui.okButton.clicked.connect(self.onOk_clicked)
        self.ui.backupButton.clicked.connect(self.onBackupClicked)
        self.ui.connectionLabel.setVisible(False)

        self.populate_instance()

    # Check the type of SQL server authentication
    #def checkAuthType(self):
    #    if self.ui.authTypeBox.currentIndex() is 0:
    #        return "yes"
    #    else:



    def testConnection(self):
        trusted_conn = "yes"
        datahelper = DatabaseHelper(self.server_name, trusted_conn)
        msg = datahelper.test_connection()
        self.ui.connectionLabel.setText(msg)
        self.ui.connectionLabel.setVisible(True)

    def populate_instance(self):
        sqlnames = self.registry.sub_keys()
        sqlnames.append("ML001")
        self.ui.instanceBox.addItems(sqlnames)

    # handlers
    def handleComboActivated(self):
        indexItem = f".\\{self.ui.instanceBox.currentText()}"
        self.server_name = indexItem


    #Deprecated
    #
    #def handleComboSQLActivated(self):
    #    if self.ui.authTypeBox.currentIndex() is 0:
    #        self.ui.usernameEdit.setEnabled(False)
    #        self.ui.pwdEdit.setEnabled(False)
    #    else:
    #        self.ui.usernameEdit.setEnabled(True)
    #        self.ui.pwdEdit.setEnabled(True)
    #
    #    self.sql_conn_type = self.ui.authTypeBox.currentIndex()

    def onDestChanged(self):
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
        elif self.ui.destinationBox.currentText() == "Device":
            self.ui.chooseButton.setText("Choose")

    def chooseDirectory(self):
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
            self.ui.chooseButton.clicked.connect(self.show_window)
            pass
        elif self.ui.destinationBox.currentText() == "Device":
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)
            dest_dir = QFileDialog.getExistingDirectory(self,
                                                        "Backup Destination Folder",
                                                        expanduser("~"),
                                                        QFileDialog.ShowDirsOnly)

            self.ui.destEdit.setText(os.path.normpath(dest_dir))

    def onOk_clicked(self):
        self.ui.databaseListWidget.clear()
        trusted_conn = "yes"
        datahelper = DatabaseHelper(self.server_name, trusted_conn)
        databases = datahelper.displayAllDatabases()
        for data in databases:
            item = QtWidgets.QListWidgetItem(data)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.databaseListWidget.addItem(item)

    def onBackupClicked(self):
        msgbox = QMessageBox
        try:
            #trusted_conn = self.checkAuthType()
            path = self.ui.destEdit.text()
            backup_items = self.getCheckedItems()
            datahelper = DatabaseHelper(self.server_name, "yes")
            if path is not "" or None:
                if not self.ui.enableCheckBox.checkState():
                    for items in backup_items:
                        datahelper.backup_database(items, path)
                    msgbox.information(self,"",f"Databases has been backup!")
            else:
                msgbox.warning(self, "Warning", "Backup folder destination not chosen")
        except Exception as e:
            msgbox.warning(self, "Warning", repr(e))

    def setBackupParams(self,item,path):
        param = {

        }
        return param

    def getCheckedItems(self):
        checkedItems = []
        checkedDB = self.ui.databaseListWidget
        for index in range(checkedDB.count()):
            if checkedDB.item(index).checkState() is QtCore.Qt.Checked:
                checkedItems.append(checkedDB.item(index).text())
        print(checkedItems)
        return checkedItems

    @QtCore.Slot(QtCore.Qt.CheckState)
    def onCheckBoxState(self,state):
        self.ui.enableCheckBox.setEnabled(state == QtCore.Qt.Checked)
        if state != QtCore.Qt.Checked:
            self.ui.enableCheckBox.setEnabled(True)
            self.ui.resetButton.setEnabled(True)
            self.ui.setButton.setEnabled(True)
        else:
            self.ui.enableCheckBox.setEnabled(False)
            self.ui.resetButton.setEnabled(False)
            self.ui.setButton.setEnabled(False)


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Main()
    ui.setupUi(mainWindow)
    ui.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
