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

        self._ui.combo.activated[int].connect(self.onActivateTab)
        # self._ui.combo.activated.connect(self._main_controller.controller_onActivateTab)
        self._ui.button_serch.clicked.connect(self.read_db_view_regedit_install)
        self._ui.button_serch.clicked.connect(self.prefetch_main_view)
        self._ui.button_serch.clicked.connect(self.activities_main_view)
        self._ui.button_serch.clicked.connect(self.event_security_main_view)
        self._ui.button_serch.clicked.connect(self.event_security_time_main_view)
        self._ui.button_serch.clicked.connect(self.recent_main_view)
        self._ui.button_serch.clicked.connect(self.event_main_application_install_and_delete)
        # self._ui.button_serch.clicked.connect(self.coconnect_dbdb)
        self._ui.button_exit.clicked.connect(self.closeEvent)

    def closeEvent(self, event):
        self._main_controller.controller_del_db()
        sys.exit()

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

    def onActivateTab(self, index):
        self._ui.tab.setCurrentIndex(index)

    def prefetch_main_view(self):
        self._ui.tabel1.setColumnCount(len(self._main_controller.select_prefetch_control()[0]))
        self._ui.tabel1.setRowCount(len(self._main_controller.select_prefetch_control()[1]))  # and one row
        self._ui.tabel1.setHorizontalHeaderLabels(self._main_controller.select_prefetch_control()[0])
        for row,i in enumerate(self._main_controller.select_prefetch_control()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel1.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        # self._ui.tabel1.resizeColumnsToContents()

    def activities_main_view(self):
        self._ui.tabel3.setColumnCount(len(self._main_controller.select_activities_db()[0]))
        self._ui.tabel3.setRowCount(len(self._main_controller.select_activities_db()[1]))  # and one row
        self._ui.tabel3.setHorizontalHeaderLabels(self._main_controller.select_activities_db()[0])
        for row,i in enumerate(self._main_controller.select_activities_db()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel3.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.tabel3.resizeColumnsToContents()

    def event_security_main_view(self):
        self._ui.tabel4.setColumnCount(len(self._main_controller.select_event_security_control()[0]))
        self._ui.tabel4.setRowCount(len(self._main_controller.select_event_security_control()[1]))  # and one row
        self._ui.tabel4.setHorizontalHeaderLabels(self._main_controller.select_event_security_control()[0])
        for row,i in enumerate(self._main_controller.select_event_security_control()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel4.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.tabel4.resizeColumnsToContents()
        # self._ui.tabel4.rowSpan()

    def event_security_time_main_view(self):
        table_names_column = ['Подія',"Час Події","Користувач", "Попередній Час", "Новий Час"]
        self._ui.tabel5.setColumnCount(len(table_names_column))
        self._ui.tabel5.setRowCount(len(self._main_controller.select_event_security_time_control()[1]))  # and one row
        self._ui.tabel5.setHorizontalHeaderLabels(table_names_column)
        self._ui.tabel5.setSortingEnabled(True)
        for row,i in enumerate(self._main_controller.select_event_security_time_control()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel5.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.tabel5.resizeColumnsToContents()

    def recent_main_view(self):
        self._ui.tabel6.setColumnCount(len(self._main_controller.select_recent_control()[0]))
        self._ui.tabel6.setRowCount(len(self._main_controller.select_recent_control()[1]))
        self._ui.tabel6.setHorizontalHeaderLabels(self._main_controller.select_recent_control()[0])
        self._ui.tabel6.setSortingEnabled(True)
        for row,i in enumerate(self._main_controller.select_recent_control()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel6.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.tabel6.resizeColumnsToContents()

    def event_main_application_install_and_delete(self):
        self._ui.tabel7.setColumnCount(len(self._main_controller.select_event_aplication_install_and_delete()[0]))
        self._ui.tabel7.setRowCount(len(self._main_controller.select_event_aplication_install_and_delete()[1]))
        self._ui.tabel7.setHorizontalHeaderLabels(self._main_controller.select_event_aplication_install_and_delete()[0])
        self._ui.tabel7.setSortingEnabled(True)
        for row, i in enumerate(self._main_controller.select_event_aplication_install_and_delete()[1]):
            for colmn,j in enumerate(i):
                self._ui.tabel7.setItem(row, colmn, QtWidgets.QTableWidgetItem(str(j)))
        self._ui.tabel7.resizeColumnsToContents()