from .main_view_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtWidgets

class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setup_ui(self)


        # self._ui.combo.activated.connect(self.onActivateTab)
        self._ui.button_serch.clicked.connect(self.read_db_view_regedit_install)
        # self._ui.button_serch.clicked.connect(self.coconnect_dbdb)
        # self._ui.button_exit.clicked.connect(self.closeEvent)
    # def closeEvent(self, event):
    #     self.view_del_db()

    def read_db_view_regedit_install(self):
        self._main_controller.readd_file()
        self._ui.table.setColumnCount(len(self._main_controller.select_data()[0]))
        self._ui.table.setRowCount(len(self._main_controller.select_data()[1]))  # and one row
        # Set three columns
        self._ui.table.setHorizontalHeaderLabels(self._main_controller.select_data()[0])
        for row,i in enumerate(self._main_controller.select_data()[1]):
            for colmn,j in enumerate(i):
                self._ui.table.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.table.resizeColumnsToContents()

