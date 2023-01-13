from PyQt5 import QtCore, QtGui, QtWidgets
from .style.style_buttons import *




class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle("Main")
        MainWindow.resize(700, 800)
        # self.main_window_fone = MainWindow.palette()
        # self.main_window_fone.setBrush(QtGui.QPalette.Normal, QtGui.QPalette.Window,
        #      QtGui.QBrush(QtGui.QPixmap(r"images/fone.jpg")))
        # MainWindow.setPalette(self.main_window_fone)

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([
            "Перевірка дій користувача в АС",
            "Підключені USB носії до АС",
            "Активність користувача в АС"
        ])
        self.combo.setStyleSheet(combostyle)
        # self.vbox.addWidget(self.combo)
        label = QtWidgets.QLabel("PROGRAMS AUDIT OS MICROSOFT WINDOWS")
        label.resize(700, 650)
        label.setAlignment(QtCore.Qt.AlignHCenter)
        label.setAutoFillBackground(True)
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(label)
        MainWindow.setLayout(self.vbox)
