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

    def select_activities_db(self):
        return self._model.select_activities_cache()

    def select_prefetch_control(self):
        return self._model.select_prefetch()

    def select_event_security_control(self):
        return self._model.select_event_security()

    def select_event_security_time_control(self):
        return self._model.select_event_time()

    def select_recent_control(self):
        return self._model.select_recent()

    # @pyqtSlot(object)
    # def controller_read_activities(self, table):
    #     self._model.read_activities()
    #     return self._model.viev_database_activities(table)

    def select_event_aplication_install_and_delete(self):
        return self._model.select_event_aplication_install_and_delete()

    def controller_del_db(self):
        self._model.del_database()


    # def controller_onActivateTab(self):
    #     self._model.onActivateTab()
    # @pyqtSlot(str)
    # def add_user(self, value):
    #     self._model.add_user(value)
    #
    # @pyqtSlot(int)
    # def delete_user(self, value):
    #     self._model.delete_user(value)
