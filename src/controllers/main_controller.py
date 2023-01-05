from PyQt5.QtCore import QObject, pyqtSlot


class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    @pyqtSlot(str)
    def add_user(self, value):
        self._model.add_user(value)

    @pyqtSlot(int)
    def delete_user(self, value):
        self._model.delete_user(value)
