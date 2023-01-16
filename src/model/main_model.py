from PyQt5.QtCore import QObject, pyqtSignal
import sqlite3
import winreg
from winreg import *
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, table


class Model(QObject):
    def __init__(self):
        super().__init__()
        self.creat_bd()
        self.read_file()


    def creat_bd(self):
        engine = create_engine('sqlite:///shows.db', echo=True)
        conn = engine.connect()
        meta = MetaData()

        regedit_install = Table(
            'regedit_install', meta,
            Column('id', Integer, primary_key=True),
            Column('display_name', String),
            Column('DisplayVersion', String),
            Column('InstallDate', String),
            Column('InstallSource', String),
            Column('Publisher', String),
            Column('InstallLocation', String)
        )
        meta.create_all(engine)
        conn.close()
    def read_file(self):
        aReg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        aKey = OpenKey(aReg, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
        mass = []
        i = 0

        try:
            while True:
                keyname = EnumKey(aKey, i)
                asubkey = OpenKey(aKey, keyname)
                try:
                    a = (QueryValueEx(asubkey, "DisplayName")[0])
                except:
                    a = 'Інформація відсутня'
                try:
                    b = (QueryValueEx(asubkey, "DisplayVersion")[0])
                except:
                    b = 'Інформація відсутня'
                try:
                    c = (QueryValueEx(asubkey, "InstallDate")[0])
                except:
                    c = 'Інформація відсутня'
                try:
                    d = (QueryValueEx(asubkey, "InstallSource")[0])
                except:
                    d = 'Інформація відсутня'
                try:
                    e = (QueryValueEx(asubkey, "Publisher")[0])
                except:
                    e = 'Інформація відсутня'
                try:
                    r = (QueryValueEx(asubkey, "InstallLocation")[0])
                    # if r.count('') == 1:
                    #     r = 'Інформація відсутня'
                except:
                    r = 'Інформація відсутня'
                i += 1
                mass.append([
                    a,
                    b,
                    c,
                    d,
                    e,
                    r
                ])

        except:
            pass

        self.insert_mas(mass)
    def insert_mas(self,mas):
        try:
            con = sqlite3.connect("shows.db")
            cur = con.cursor()
            sql = """INSERT INTO regedit_install
                    ( display_name, DisplayVersion, InstallDate, InstallSource, Publisher, InstallLocation)
                   VALUES (?,?,?,?,?,?)"""
            cur.executemany(sql, mas)
            con.commit()
            cur.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if con:
                con.close()
                print("Соединение с SQLite закрыто")
    #     self._users = []
    #
    # users_changed = pyqtSignal(list)
    #
    # def users(self):
    #     return self._users
    #
    # def add_user(self, value):
    #     self._users.append(value)
    #     self.users_changed.emit(self._users)
    #
    # def delete_user(self, value):
    #     del self._users[value]
    #     self.users_changed.emit(self._users)
