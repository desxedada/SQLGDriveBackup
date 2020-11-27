import os
import sys

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile, QIODevice
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox

from os.path import expanduser

from ui.mainWindow import Ui_mainWindow
from common.DatabaseHelper import DatabaseHelper
from common.registry import Registry


# TODO: backup to device, choose file, test connection, choosing databases
class Main(QMainWindow, Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

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

        self.ui.instanceBox.activated.connect(self.handleComboActivated)

        self.ui.chooseButton.clicked.connect(self.chooseDirectory)
        self.ui.enableCheckBox.clicked.connect(self.onCheckBoxState)
        self.ui.destinationBox.activated[str].connect(self.onDestChanged)
        self.ui.okButton.clicked.connect(self.onOk_clicked)
        self.ui.backupButton.clicked.connect(self.onBackupClicked)
        self.ui.connectionLabel.setVisible(False)

        self.populate_instance()

        # Show Window
        self.show()

    # Check the type of SQL server authentication
    #def checkAuthType(self):
    #    if self.ui.authTypeBox.currentIndex() is 0:
    #        return "yes"
    #    else:
    #        return "no"

    def testConnection(self):
        trusted_conn = "yes"
        datahelper = DatabaseHelper(self.server_name, trusted_conn)
        msg = datahelper.main()
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
                for items in backup_items:
                    datahelper.backup_database(items, path)
                msgbox.information(self,"",f"Databases has been backup!")
            else:
                msgbox.warning(self, "Warning", "Backup folder destination not chosen")
        except Exception as e:
            msgbox.warning(self, "Warning", repr(e))

    def getCheckedItems(self):
        checkedItems = []
        checkedDB = self.ui.databaseListWidget
        for index in range(checkedDB.count()):
            if checkedDB.item(index).checkState() is QtCore.Qt.Checked:
                checkedItems.append(checkedDB.item(index).text())
        print(checkedItems)
        return checkedItems


    def onCheckBoxState(self):
        self.ui.enableCheckBox.checkState()
        self.ui.enableCheckBox.setEnabled(True)
        self.ui.timeSpinBox.setEnabled(True)
        self.ui.resetButton.setEnabled(True)
        self.ui.setButton.setEnabled(True)

if __name__ == "__main__":
    # Qt app
    app = QApplication(sys.argv)
    ui_file_name = "ui/mainWindow.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
    window.show()

    window = Main()
    sys.exit(app.exec_())
