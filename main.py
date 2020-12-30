import os
import sys
import logging

from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QFile, QIODevice, QObject
from PySide2.QtGui import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *
from os.path import expanduser

from ui.mainWindow import Ui_mainWindow
from common.DatabaseHelper import *
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

        self.ui.tray_icon = QSystemTrayIcon(self)
        self.ui.tray_icon.setIcon(QIcon("database-logo.png"))
        self.ui.scheduleTimeEdit.setDateTime(QtCore.QDateTime.currentDateTimeUtc())

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
        self.ui.okButton.clicked.connect(self.onOk_clicked)
        self.ui.backupButton.clicked.connect(self.onBackupClicked)
        self.ui.setButton.clicked.connect(self.getScheduledTime)
        self.ui.connectionLabel.setVisible(False)

        #Initialize Database class
        self.dh = DatabaseHelper()

        self.populate_instance()

    # Check the type of SQL server authentication
    #def checkAuthType(self):
    #    if self.ui.authTypeBox.currentIndex() is 0:
    #        return "yes"
    #    else:
    def get_parameters(self):
        params = self.dh.initialize_params(self.server_name, "yes")
        return params

    def testConnection(self):
        trusted_conn = "yes"

        msg = self.dh.test_connection(self.get_parameters())
        self.ui.connectionLabel.setText(msg)
        self.ui.connectionLabel.setVisible(True)

    def populate_instance(self):
        sqlnames = self.registry.sub_keys()
        sqlnames.append("ML001")
        self.ui.instanceBox.addItem("MSSQLSERVER")
        self.ui.instanceBox.addItems(sqlnames)

    # handlers
    def handleComboActivated(self):
        indexItem = f".\\{self.ui.instanceBox.currentText()}"
        self.server_name = indexItem

    '''
    def onDestChanged(self):
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
        elif self.ui.destinationBox.currentText() == "Device":
            self.ui.chooseButton.setText("Choose")
'''

    def chooseDirectory(self):
        '''
        if self.ui.destinationBox.currentText() == "Google Drive":
            self.ui.chooseButton.setText("Authorize")
            self.ui.chooseButton.clicked.connect(self.show_window)
            pass
        elif self.ui.destinationBox.currentText() == "Device":
        '''
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.AnyFile)
        dest_dir = QFileDialog.getExistingDirectory(self,
                                                        "Backup Destination Folder",
                                                        expanduser("~"),
                                                        QFileDialog.ShowDirsOnly)

        self.ui.destEdit.setText(os.path.normpath(dest_dir))

    def onOk_clicked(self):
        self.ui.databaseListWidget.clear()
        databases = self.dh.displayAllDatabases(self.get_parameters())
        for data in databases:
            item = QtWidgets.QListWidgetItem(data)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.ui.databaseListWidget.addItem(item)

    def getScheduledTime(self):
        sched_time = self.ui.scheduleTimeEdit.dateTime()
        converted_time = sched_time.toPython()
        self.ui.scheduleBackupLabel.setVisible(True)
        self.ui.scheduleBackupLabel.setText(
            f"Schedule Time: {converted_time.hour}:{converted_time.minute} daily."
        )
        return converted_time

    def onBackupClicked(self):
        params = self.get_parameters()
        msgbox = QMessageBox
        trusted_conn = "yes"
        try:
            #trusted_conn = self.checkAuthType()
            path = self.ui.destEdit.text()
            backup_items = self.getCheckedItems()
            if path is not "" or None:
                if not self.ui.enableCheckBox.checkState():
                    for items in backup_items:
                        self.dh.backup_database(params,items,path)
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
        if not self.ui.enableCheckBox.isChecked():
            self.ui.setButton.setEnabled(False)
            self.ui.resetButton.setEnabled(False)
        else:
            self.ui.setButton.setEnabled(True)
            self.ui.resetButton.setEnabled(True)

    def onSetClicked(self):
        # Get attributes
        path = self.ui.destEdit.text()
        time_to_backup = self.getScheduledTime()

        # Initialize message box
        msgbox = QMessageBox

        # Populate schedule indicator
        self.ui.scheduleBackupLabel.setVisible(True)
        self.ui.scheduleBackupLabel.setText(
            f"Schedule Time: {time_to_backup.hour()}:{time_to_backup.minute()} daily."
        )

        params = self.get_parameters()
        backup_items = self.getCheckedItems()
        if path is not "" or None:
            self.ui.scheduleBackupLabel.setText()
            if not self.ui.enableCheckBox.checkState():
                for items in backup_items:
                    _schedule = APS()
                    while True:
                        _schedule.add_schedule(time_to_backup)
                        self.dh.backup_database(params,items,path)
        else:
            msgbox.warning(self, "Warning", "Backup folder destination not chosen")


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Main()
    ui.setupUi(mainWindow)
    ui.show()

    sys.exit(app.exec_())



if __name__ == '__main__':
    main()
