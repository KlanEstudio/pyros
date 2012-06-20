#coding: utf-8

'''
Created on 13/06/2012

@author: Andrés Javier López <ajavier.lopez@gmail.com>
@version: 1.0 
'''
import pyros.restobject
import pyros.database
import config
import web

class Test(pyros.restobject.RestObject):
    def __init__(self):
        config.check_database()
        test3 = pyros.database.Datamap('test3')
        
        test2 = pyros.database.Datamap('test2')
        test2.add_join(test3, 'id_test2', 'internos')
        
        self.datamap = pyros.database.Datamap('test', ['id_test', 'valor1_test AS valor1', 'valor2_test'])
        self.datamap.add_join(test2, 'id_test', 'subtest')
        
        self.fields_test = ['valor1_test', 'valor2_test']
        
    def read(self):
        return self._resp('elementos', self.datamap.read())
    
    def insert(self):
        data = pyros.database.Dataset(self.fields_test, json_data=web.data())
        result = data.insert_to('test')
        return self._resp_success(result)
    
    def get_element(self, id_element):
        return self._resp('elemento', self.datamap.get_element(id_element))
    
    def insert_into(self, id_element):
        data = pyros.database.Dataset(['prueba'], json_data=web.data())
        data.add_field('id_test', id_element)
        result = data.insert_to('test2')
        return self._resp_success(result)
    
    def update_element(self, id_element):
        data = pyros.database.Dataset(self.fields_test)
        result = data.update_in('test', id_element, web.data())
        return self._resp_success(result)
    
    def delete_element(self, id_element):
        pyros.database.Model('test').delete(id_element)
        return self._resp_success(True)
        