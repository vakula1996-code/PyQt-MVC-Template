from PyQt5 import QtCore, QtGui, QtWidgets
from wheel.cli.pack import pack

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
            "Активність ПЗ у системі",
            "Запуск процесів, які ініціював користувач або процес",
            "Вивід документів на пристрої друку",
            "Облікові записи користувачів",
            "Доступ користувачів до обєктів ОС",
            "Зміна системного часу в ОС",
            "Дати встановлення/видалення ПЗ",
            "Файли та директорії, до яких звертався користувач останнім часом"
        ])
        self.combo.setStyleSheet(combostyle)

        self.tab = QtWidgets.QTabWidget()
        self.personal_page = QtWidgets.QWidget()
        self.contact_page = QtWidgets.QWidget()
        self.vkladka_3 = QtWidgets.QWidget()
        self.vkladka_4 = QtWidgets.QWidget()
        self.vkladka_5 = QtWidgets.QWidget()
        self.vkladka_6 = QtWidgets.QWidget()
        self.vkladka_7 = QtWidgets.QWidget()
        self.vkladka_8 = QtWidgets.QWidget()

        self.tab.addTab(self.personal_page, 'Інстальоване ПЗ (відомості з реєстру)')
        self.tab.addTab(self.contact_page, 'Інформація, яка міститься в файлі PREFETCH')
        self.tab.addTab(self.vkladka_3, 'Запуск программ користувачами')
        self.tab.addTab(self.vkladka_4, 'AAAAAAAAAAAAAAA')
        self.tab.addTab(self.vkladka_5, 'Зміна часу системи')
        self.tab.addTab(self.vkladka_6, 'Файли та директорії, до яких звертався користувач останнім часом')
        self.tab.addTab(self.vkladka_7, 'ZZZZZZZZZZZZZZ')
        self.tab.addTab(self.vkladka_8, 'ЙЙЙЙЙЙЙЙЙЙЙЙЙЙ')
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

        self.tabel1 = QtWidgets.QTableWidget(parent=self.contact_page)
        self.tabel1.setWordWrap(True)

        self.tabel3 = QtWidgets.QTableWidget(parent=self.vkladka_3)
        self.tabel3.setWordWrap(True)

        self.tabel4 = QtWidgets.QTableWidget(parent=self.vkladka_4)
        self.tabel4.setWordWrap(True)

        self.tabel5 = QtWidgets.QTableWidget(parent=self.vkladka_5)
        self.tabel5.setWordWrap(True)

        self.tabel6 = QtWidgets.QTableWidget(parent=self.vkladka_6)
        self.tabel6.setWordWrap(True)

        self.tabel7 = QtWidgets.QTableWidget(parent=self.vkladka_7)
        self.tabel7.setWordWrap(True)

        self.vbox7 = QtWidgets.QVBoxLayout()
        self.vbox7.addWidget(self.tabel7)
        self.vkladka_7.setLayout(self.vbox7)

        self.vbox6 = QtWidgets.QVBoxLayout()
        self.vbox6.addWidget(self.tabel6)
        self.vkladka_6.setLayout(self.vbox6)

        self.vbox5 = QtWidgets.QVBoxLayout()
        self.vbox5.addWidget(self.tabel5)
        self.vkladka_5.setLayout(self.vbox5)

        self.vbox4 = QtWidgets.QVBoxLayout()
        self.vbox4.addWidget(self.tabel4)
        self.vkladka_4.setLayout(self.vbox4)

        self.vbox3 = QtWidgets.QVBoxLayout()
        self.vbox3.addWidget(self.tabel3)
        self.vkladka_3.setLayout(self.vbox3)

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


