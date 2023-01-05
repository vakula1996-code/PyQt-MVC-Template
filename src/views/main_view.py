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

        self._ui.pushButton_add.clicked.connect(self.on_add_user)
        self._ui.pushButton_delete.clicked.connect(self.on_delete_user)

        self._model.users_changed.connect(self.on_list_changed)


    @pyqtSlot(bool)
    def on_add_user(self):
        self._main_controller.add_user(self._ui.lineEdit_name.text())
        self._ui.lineEdit_name.clear()

    @pyqtSlot(bool)
    def on_delete_user(self):
        self._main_controller.delete_user(self._ui.listWidget_names.currentRow())

    @pyqtSlot(list)
    def on_list_changed(self, value):
        self._ui.listWidget_names.clear()
        self._ui.listWidget_names.addItems(value)