# -*- coding: utf-8 -*-
import pyodbc
import pdb

class OpenEdgeConnector():
    def __init__(self, type_connection, uid, pwd, dsn=None, driver_path=None, host=None, port=None, dbname=None):
        """
            Al inicializar la clase, tomamos todos los parámetros necesarios del settings que se configuran en entorno.ini.
        """
        self.connection = None
        self.cursor = None
        connection_string = ''
        connection_kwargs = {}
        """
            EJEMPLO DE TIPOS DE CONEXIONES:
            DSN: dsn_cnx = pyodbc.connect('DSN=CLIENTODBC;UID=sysprogress;PWD=sysprogress')
            DRIVER: driver_cnxn = pyodbc.connect('DRIVER={/usr/dlc/odbc/lib/pgoe1023.so};HostName=192.168.1.240;DATABASENAME=dbname;PORTNUMBER=40002;LogonID=sysprogress;PASSWORD=sysprogress',ansi=True, autocommit=True)
        """
        if type_connection == 'DSN':
            connection_string = 'DSN={};UID={};PWD={};CHARSET=utf8'.format(dsn, uid, pwd)
        else:
            connection_string = 'DRIVER={};HostName={};DATABASENAME={};PORTNUMBER={};LogonID={};PASSWORD={};CHARSET=utf8'.format(driver_path, host, dbname, port, uid, pwd)
            connection_kwargs['ansi'] = True
            connection_kwargs['autocommit'] = True
        self.connection = pyodbc.connect(connection_string, **connection_kwargs)

        self.cursor = self.connection.cursor()
        self.cursor.execute("SET SCHEMA 'PUB'")

        self.connection.setdecoding(pyodbc.SQL_CHAR, encoding='ISO-8859-1')
        self.connection.setdecoding(pyodbc.SQL_WCHAR, encoding='ISO-8859-1')

    def query(self, query):
        return self.cursor.execute(query)

    def update(self, query, argsv=[]):
        self.cursor.execute(query, *argsv)
        self.cursor.commit()
        return self.cursor.rowcount

    def fetchall(self, query, as_dict=False):
        self.query(query)
        return self.as_dict_all() if as_dict == True else self.cursor.fetchall()

    def fetchone(self, query, as_dict=False):
        self.query(query)
        return self.as_dict_one() if as_dict == True else self.cursor.fetchone()

    def as_dict_one(self):
        columns = [column[0] for column in self.cursor.description]
        result = self.cursor.fetchone()
        result = dict(zip(columns, result)) if result else None
        return result

    def as_dict_all(self):
        columns = [column[0] for column in self.cursor.description]
        results = []
        for row in self.cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results
