import sys

from PySide2 import QtCore, QtWidgets
from PySide2.QtCore import QFile, QIODevice, Slot, Signal, QRunnable
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog

from ui.mainWindow import Ui_mainWindow
from ui.authorizeWindow import Ui_authorizeWindow
from database.DatabaseHelper import DatabaseHelper
from system.Admin import Admin


class Main(QMainWindow,Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.connectionButton.clicked.connect(self.testConnection)
        self.ui.connectionButton.show()
        self.ui.usernameEdit.setEnabled(False)
        self.ui.pwdEdit.setEnabled(False)
        self.admin = Admin()
        self.admin.start_admin()
        self.ui.chooseButton.clicked.connect(self.choose_destination)
        self.ui.destinationBox.activated[str].connect(self.onDestChanged)
        self.ui.authTypeBox.activated[str].connect(self.onAuthChanged)
        self.ui.okButton.clicked.connect(self.onOk_clicked)
        self.ui.connectionLabel.setVisible(False)
        self.populate_instance()
        name = self.ui.instanceBox.currentText()


        #Show Window
        self.show()

    def establishConnection(self):
        dh = DatabaseHelper()

    def testConnection(self):
        server_name = ".\\" + (self.ui.instanceBox.currentText())
        dh = DatabaseHelper(server_name,"","","")
        msg = dh.test_connection()
        self.ui.connectionLabel.setText(msg)
        self.ui.connectionLabel.setVisible(True)

    def populate_instance(self):
        a = Admin()
        sqlnames = a.sub_keys()
        print(sqlnames)
        self.ui.instanceBox.addItems(sqlnames)


    def choose_destination(self):
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
            self.ui.chooseButton.clicked.connect(self.show_window)
            pass
        elif self.ui.destinationBox.currentText() == "Device":
            dialog = QFileDialog(self)
            dialog.setFileMode(QFileDialog.AnyFile)

    def onDestChanged(self):
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
        elif self.ui.destinationBox.currentText() == "Device":
            self.ui.chooseButton.setText("Choose")

    def onAuthChanged(self):
        if self.ui.destinationBox.currentText() == "Windows Authentication":
            self.ui.usernameEdit.setEnabled(False)
            self.ui.pwdEdit.setEnabled(False)
        else:
            self.ui.usernameEdit.setEnabled(True)
            self.ui.pwdEdit.setEnabled(True)


    def onOk_clicked(self):
        self.ui.databaseListWidget.clear()
        dh = DatabaseHelper(".\ML001","","","")
        databases = dh.displayAllDatabases()
        for data in databases:
            item = QtWidgets.QListWidgetItem(data)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.databaseListWidget.addItem(item)



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