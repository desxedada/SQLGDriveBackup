import sys

from PySide2.QtCore import QFile, QIODevice, Slot , Signal
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog
from ui.mainWindow import Ui_mainWindow
from ui.authorizeWindow import Ui_authorizeWindow
from database.DatabaseHelper import DatabaseHelper
from system.Admin import Admin

class Main(QMainWindow,Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        #Qt app
        app = QApplication(sys.argv)

        #Get Local Host

        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.connectionButton.clicked.connect(self.testConnection)
        self.ui.connectionButton.show()
        self.ui.instanceBox.addItems(self.populate_instance())
        self.ui.usernameEdit.setEnabled(False)
        self.ui.pwdEdit.setEnabled(False)
        self.admin = Admin()
        self.admin.start_admin()
        self.ui.chooseButton.clicked.connect(self.choose_destination)
        self.ui.destinationBox.activated[str].connect(self.onDestChanged)
        self.ui.authTypeBox.activated[str].connect(self.onAuthChanged)
        self.ui.connectionLabel.setVisible(False)

        #Show Window
        self.show()

    def testConnection(self):
        pass
        dh = DatabaseHelper(".\ML001","","","")
        msg = dh.test_connection()
        self.ui.connectionLabel.setText(msg)
        self.ui.connectionLabel.setVisible(True)

    def populate_instance(self):
        dh = DatabaseHelper(".\ML001","","","")
        instances = dh.displayAllInstances()
        print(instances)
        return instances

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

    def show_window(self):

        window = Ui_authorizeWindow()
        window.show()

if __name__ == "__main__":


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