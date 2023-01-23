import sqlalchemy
from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, table, select
from sqlalchemy.orm import Session
from .service.read_regedit_install import read_file
from .service.read_activities import read_activities



class Model(QObject):
    def __init__(self):
        super().__init__()
        self._engine = create_engine('sqlite:///shows.db', echo=True)
        self._conn = self._engine.connect()
        self._meta = MetaData()

        self._regedit_install_data = []

        self._session = Session(self._engine)
        self._regedit_install_model = object
        self.creat_bd()

    # def read_activities(self):
    #     self._session.query(activities_cache).filter(String("display_name = 'user'")).all()
    #     self.model.beginResetModel()
    #     self.model._data = []
    #     for row in cur:
    #         self.model._data.append([col for col in row])
    #     self.model.headers = [i[0] for i in cur.description]
    #     self.model.endResetModel()

    def list_regedit_install(self):
        return self._regedit_install_data

    def creat_bd(self):
        self.regedit_install = Table(
            'regedit_install', self._meta,
            Column('id', Integer, primary_key=True),
            Column('display_name', String),
            Column('DisplayVersion', String),
            Column('InstallDate', String),
            Column('InstallSource', String),
            Column('Publisher', String),
            Column('InstallLocation', String)
        )
        self.activities_cache = Table(
            'activities_cache', self._meta,
            Column('id', Integer, primary_key=True),
            Column('aplication', String),
            Column('starttime', String),
            Column('lastmodifia', String),
            Column('ExpirationTime', String),
            Column('LastModifiedOnClient', String),
            Column('EndTime', String),
            Column('UserName', String)
        )
        self._meta.create_all(self._engine)

    def insert_regedit_install(self):
        self._conn.execute(self.regedit_install.insert(), read_file())
        self._conn.execute(self.activities_cache.insert(), read_activities())

    def select_regedit_install(self):
        regedit_install_keys = self.regedit_install.columns.keys()
        return (regedit_install_keys, self._session.execute(select(self.regedit_install)).all())

    def del_database(self):
        con1 = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con1.setDatabaseName("shows.db")
        con1.open()
        self._regedit_install_model.setQuery("delete from regedit_install")
        con.close()


    def write_mass_activities(self,mas):
        con = sqlite3.connect("shows.db")
        cur = con.cursor()
        sql = """INSERT INTO activities_cache
            (aplication, starttime, lastmodifia, ExpirationTime,
            LastModifiedOnClient, EndTime, UserName)
            VALUES (?,?,?,?,?,?,?)"""
        cur.executemany(sql, mas)
        con.commit()
        cur.close()

    def viev_database_activities(self, table1):
        con = QtSql.QSqlDatabase.addDatabase("QSQLITE")
        con.setDatabaseName("shows.db")
        con.open()
        self._regedit_install_model = QtSql.QSqlQueryModel(parent = table1)
        self._regedit_install_model.setQuery("select * from activities_cache")
        con.close()
        return self._regedit_install_model


    # @pyqtSlot(int)
    def onActivateTab(self, index):
        self._ui.tab.setCurrentIndex(index)

    def view_del_db(self):
        self._main_controller.controller_del_db()

