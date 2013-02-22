#coding: utf-8

'''
Created on 12/06/2012

@author: Andrés Javier López <ajavier.lopez@gmail.com>
@version: 
'''
import pyros.database
import pyros.urlmapper

urlmap = pyros.urlmapper.URL()
urlmap.add('/', 'test.simple.Start')
urlmap.add('/basic', 'test.simple.Basic')
urlmap.add('/test/database', 'test.database.Test')
urlmap.add('/test/auth', 'test.auth.AuthTest')
urls = urlmap.get_map()

database = {'dbn': 'mysql', 'user': 'root', 'password': '', 'database': 'pyros_test'}

debug = True

def init_connection():
    pyros.database.Database.initialize(database)
    
def check_database():
    if(pyros.database.check_connection() == False):
        init_connection()
    
init_connection()