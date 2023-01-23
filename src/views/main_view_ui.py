from PyQt5 import QtCore, QtGui, QtWidgets
from .style.style_buttons import *
from PyQt5.QtWidgets import QApplication, QTableView
from .costom_widget.table import TableModel


from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QSize, Qt


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setWindowTitle("Main")

        ############На весь екран, незалежно від розміру
        # self.desktop = QApplication.desktop()
        # self.screenRect = self.desktop.screenGeometry()
        # self.height = self.screenRect.height()
        # self.width = self.screenRect.width()
        # MainWindow.resize(self.width,self.height)

        MainWindow.resize(700, 700)
        self.window = QtWidgets.QWidget()
        self.window.setObjectName('window')
        self.window.setStyleSheet(stylesheet)

        self.combo = QtWidgets.QComboBox()
        self.combo.addItems([
            "Перевірка дій користувача в АС",
            "Підключені USB носії до АС",
            "Активність користувача в АС"
        ])
        self.combo.setStyleSheet(combostyle)

        self.tab = QtWidgets.QTabWidget()
        self.personal_page = QtWidgets.QWidget()
        self.contact_page = QtWidgets.QWidget()
        self.tab.addTab(self.personal_page, 'Personal Info')
        self.tab.addTab(self.contact_page, 'Personal Info')
        # self.tab.tabBar().hide()

        # self.tabel = QtWidgets.QTableView(parent = self.personal_page)
        #
        # self.table_model = TableModel()
        # self.tabel.setModel(self.table_model)
        # self.tabel.clearSpans()
        # self.tabel.horizontalHeader().setSectionResizeMode(1)
        # self.tabel.setAutoFillBackground(True)
        # self.tabel.setShowGrid(True)
        # self.tabel.resizeRowsToContents()
        self.table = QtWidgets.QTableWidget(parent = self.personal_page)  # Create a table
        self.table.setWordWrap(True)

        self.tabel1 = QtWidgets.QTableView(parent=self.contact_page)

        self.vbox2 = QtWidgets.QVBoxLayout()
        self.vbox2.addWidget(self.tabel1)
        self.contact_page.setLayout(self.vbox2)

        self.vbox1 = QtWidgets.QVBoxLayout()
        self.vbox1.addWidget(self.table)
        self.personal_page.setLayout(self.vbox1)

        self.button_serch = QtWidgets.QPushButton("SEARCH")
        self.button_serch.setStyleSheet(button_serch_style)

        self.button_exit = QtWidgets.QPushButton("EXIT")
        self.button_exit.setStyleSheet(button_exit_style)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.combo)
        self.vbox.addWidget(self.tab)
        self.vbox.addWidget(self.button_serch)
        self.vbox.addWidget(self.button_exit)
        self.window.setLayout(self.vbox)
        MainWindow.setCentralWidget(self.window)


