from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 250)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.vboxlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.listWidget_names = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_names.setObjectName("listWidget_names")
        self.verticalLayout.addWidget(self.listWidget_names)

        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.verticalLayout.addWidget(self.lineEdit_name)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setObjectName("pushButton_add")
        self.horizontalLayout_2.addWidget(self.pushButton_add)

        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setEnabled(True)
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.horizontalLayout_2.addWidget(self.pushButton_delete)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.vboxlayout.addLayout(self.verticalLayout)
        self.label_even_odd = QtWidgets.QLabel(self.centralwidget)
        self.label_even_odd.setObjectName("label_even_odd")
        self.vboxlayout.addWidget(self.label_even_odd)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_add.setText(_translate("MainWindow", "Add"))
        self.pushButton_delete.setText(_translate("MainWindow", "Delete"))

