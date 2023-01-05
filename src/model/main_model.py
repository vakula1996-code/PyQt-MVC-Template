from PyQt5.QtCore import QObject, pyqtSignal


class Model(QObject):
    def __init__(self):
        super().__init__()

        self._users = []

    users_changed = pyqtSignal(list)

    def users(self):
        return self._users

    def add_user(self, value):
        self._users.append(value)
        self.users_changed.emit(self._users)

    def delete_user(self, value):
        del self._users[value]
        self.users_changed.emit(self._users)
