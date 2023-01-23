from PyQt5.QtCore import QObject, pyqtSlot



class MainController(QObject):
    def __init__(self, model):
        super().__init__()

        self._model = model

    # @pyqtSlot(object)
    def readd_file(self):
        self._model.insert_regedit_install()

    def select_data(self):
        return self._model.select_regedit_install()

    @pyqtSlot(object)
    def controller_read_activities(self, table):
        self._model.read_activities()
        return self._model.viev_database_activities(table)

    def controller_del_db(self):
        self._model.del_database()

    def controller_onActivateTab(self):
        self._model.onActivateTab()
    # @pyqtSlot(str)
    # def add_user(self, value):
    #     self._model.add_user(value)
    #
    # @pyqtSlot(int)
    # def delete_user(self, value):
    #     self._model.delete_user(value)
