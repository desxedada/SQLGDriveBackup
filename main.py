import sys

from PySide2.QtCore import QFile, QIODevice, Slot , Signal
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication, QMainWindow
from ui.Ui_mainWindow import Ui_mainWindow
from database.DatabaseHelper import DatabaseHelper

class Main(QMainWindow,Ui_mainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_mainWindow()
        self.ui.setupUi(self)
        self.ui.connectionButton.clicked.connect(self.testConnection())
        self.ui.connectionButton.show()
        self.ui.instanceBox.addItems(self.populate_instance())
        #Show Window
        self.show()


    def testConnection(self):
        pass
        dh = DatabaseHelper(".\ML001","","","")
        msg = dh.test_connection()
        self.ui.connectionLabel.setText(msg)

    def populate_instance(self):
        dh = DatabaseHelper(".\ML001","","","")
        instances = dh.displayAllInstances()
        print(instances)
        return instances




if __name__ == "__main__":
    app = QApplication(sys.argv)
    '''
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
    '''
    window = Main()
    sys.exit(app.exec_())