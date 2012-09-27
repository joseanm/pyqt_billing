#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 21/05/2011

@author: Luis Carlos Mejia
'''
from PyQt4.QtSql import QSqlTableModel, QSqlDatabase,QSqlQueryModel,QSqlQuery
class mydb(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        QSqlDatabase.removeDatabase( 'QMYSQL' )
        self.database = QSqlDatabase.addDatabase( 'QMYSQL' )
        self.database.setDatabaseName( "misimportaciones" )
        self.database.setHostName( "localhost")
        self.database.setUserName( "root" )
        self.database.setPassword( "root" )