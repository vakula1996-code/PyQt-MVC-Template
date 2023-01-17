from .main_view_ui import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot


class MainView(QMainWindow):
    def __init__(self, model, main_controller):
        super().__init__()

        self._model = model
        self._main_controller = main_controller
        self._ui = Ui_MainWindow()
        self._ui.setup_ui(self)
        self._ui.combo.activated.connect(self.onActivateTab)
        self._ui.button_serch.clicked.connect(self.read_file)
        self._ui.button_exit.clicked.connect(self.view_del_db)

    @pyqtSlot(int)
    def onActivateTab(self, index):
        self._ui.tab.setCurrentIndex(index)

    def view_del_db(self):
        self._main_controller.controller_del_db()

    def read_file(self):
        self.view_db(self._main_controller.read_file(self._ui.tabel))


    def view_db(self, model):
        self._ui.tabel.setModel(model)
        self._ui.tabel.hideColumn(0)
        self._ui.tabel.setColumnWidth(1, 100)
        self._ui.tabel.setColumnWidth(2, 100)
        self._ui.tabel.setColumnWidth(4, 250)
        self._ui.tabel.setColumnWidth(5, 250)
        self._ui.tabel.setColumnWidth(6, 250)
        # self._ui.tab.setCurrentIndex(index)
        # self._ui.pushButton_add.clicked.connect(self.on_add_user)
        # self._ui.pushButton_delete.clicked.connect(self.on_delete_user)
        #
        # self._model.users_changed.connect(self.on_list_changed)


    # @pyqtSlot(bool)
    # def on_add_user(self):
    #     self._main_controller.add_user(self._ui.lineEdit_name.text())
    #     self._ui.lineEdit_name.clear()
    #
    # @pyqtSlot(bool)
    # def on_delete_user(self):
    #     self._main_controller.delete_user(self._ui.listWidget_names.currentRow())
    #
    # @pyqtSlot(list)
    # def on_list_changed(self, value):
    #     self._ui.listWidget_names.clear()
    #     self._ui.listWidget_names.addItems(value)