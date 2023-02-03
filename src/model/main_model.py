import sqlalchemy
from PyQt5.QtCore import QObject, pyqtSignal
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, table, select
from sqlalchemy.orm import Session
from .service.read_regedit_install import read_file
from .service.read_activities import read_activities
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSlot
from .service.prefetch_dir.prefetch_main import prefetch_main
from .service.event_security import event_read
from .service.recent import path_users
from .service.event_aplication_install_and_delete import read_event_instal_and_delete

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
            # Column('starttime', String),
            Column('lastmodifia', String),
            # Column('ExpirationTime', String),
            # Column('LastModifiedOnClient', String),
            # Column('EndTime', String),
            Column('UserName', String)
        )
        self.prefetch_table = Table(
            'prefetch_table', self._meta,
            Column('id', Integer, primary_key=True),
            Column('name_file', String),
            Column('last_executed', String),
            Column('directory_strings', String),
            Column('resources_loaded', String),
        )
        self.event_security_table = Table(
            'event_security', self._meta,
            Column('id', Integer, primary_key=True),
            Column('task', String),
            Column('security', String),
            Column('event', String),
            Column('date', String),
            Column('KeyName', String),
            Column('DomainName', String),
            Column('PreviousTime', String),
			Column('NewTime', String)
        )
        self.recent_table = Table(
            'recent_table', self._meta,
            Column('id', Integer, primary_key=True),
            Column('user', String),
            Column('date_create', String),
            Column('info', String),
            Column('local_path', String),
            Column('size', String)
        )
        self.event_aplication_table = Table(
            'event_aplication_table', self._meta,
            Column('id', Integer, primary_key=True),
            Column('task', String),
            Column('programs_name', String),
            Column('programs_version', String),
            Column('programs_product', String),
            Column('programs_time', String),
            Column('computer', String),
            Column('info', String)
        )
        self._meta.create_all(self._engine)

    def insert_regedit_install(self):
        self._conn.execute(self.regedit_install.insert(), read_file())
        self._conn.execute(self.activities_cache.insert(), read_activities())
        self._conn.execute(self.prefetch_table.insert(), prefetch_main())
        self._conn.execute(self.event_security_table.insert(), event_read())
        self._conn.execute(self.recent_table.insert(), path_users())
        self._conn.execute(self.event_aplication_table.insert(), read_event_instal_and_delete())


    def select_regedit_install(self):
        regedit_install_keys = self.regedit_install.columns.keys()
        return (regedit_install_keys, self._session.execute(select(self.regedit_install)).all())

    def select_activities_cache(self):
        activities_cache = self.activities_cache.columns.keys()
        return (activities_cache, self._session.execute(select(self.activities_cache)).all())

    def select_prefetch(self):
        prefetch_keys = self.prefetch_table.columns.keys()
        return (prefetch_keys, self._session.execute(select(self.prefetch_table)).all())

    def select_event_security(self):
        event_security_keys = self.event_security_table.columns.keys()
        return (event_security_keys, self._session.execute(select(self.event_security_table)).all())

    def select_event_time(self):
        event_time_keys = self.event_security_table.columns.keys()
        # return (event_time_keys, self._session.execute(self.event_security_table.select().where(self.event_security_table.columns.event == 4616)).all())
        return (event_time_keys, self._session.execute(select(self.event_security_table.columns.event, self.event_security_table.columns.date, self.event_security_table.columns.KeyName, self.event_security_table.columns.PreviousTime, self.event_security_table.columns.NewTime).where(self.event_security_table.columns.event == 4616)).all())

    def select_recent(self):
        recent_keys = self.recent_table.columns.keys()
        return (recent_keys, self._session.execute(select(self.recent_table)).all())
    # select(user.c.description).where(user.c.name == 'wendy')
    # @pyqtSlot(int)

    def select_event_aplication_install_and_delete(self):
        event_aplication_install_and_delete = self.event_aplication_table.columns.keys()
        return (event_aplication_install_and_delete, self._session.execute(select(self.event_aplication_table)).all())

    def view_del_db(self):
        self._main_controller.controller_del_db()

    def del_database(self):
        self._session.query(self.regedit_install).delete()
        self._session.query(self.activities_cache).delete()
        self._session.query(self.prefetch_table).delete()
        self._session.query(self.event_security_table).delete()
        self._session.query(self.recent_table).delete()
        self._session.query(self.event_aplication_table).delete()
        self._session.commit()