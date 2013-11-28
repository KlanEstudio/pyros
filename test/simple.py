#coding: utf-8

'''
Created on 12/06/2012

@author: Andrés Javier López <ajavier.lopez@gmail.com>
@version: 1.0
'''
import web
import unittest
import random, string, json, time
import hmac, hashlib
from pyros import restobject, auth, database, urlmapper
from pyros.test.request import Request

urlmap = urlmapper.URL()
urlmap.add('/basic', 'test.simple.Basic')
urlmap.add('/auth', 'test.simple.Authenticated')
urlmap.add('/httpauth', 'test.simple.HTTPAuth')
urls = urlmap.get_map()

db = {'dbn': 'mysql', 'host': 'localhost', 'user': 'root', 'password': '', 'database': 'pyros_test'}
database.Database.initialize(db)

restobject.debug_info = True

class Basic(restobject.RestObject):
    @restobject.get_all
    def listar(self):
        return {'success': True, 'msg': u'Lista de elementos'}
    
    @restobject.get
    def element(self, elemento):
        return {'success': True, 'id': elemento, 'msg': u'Elemento individual'}
    
    @restobject.get_list("valores")
    def valores(self, elemento):
        return {'success': True, 'id': elemento, 'list': 'valores', 'msg': u'Lista del elemento'}
    
    @restobject.post
    def prueba_post(self):
        data = json.loads(web.data())
        return {'success': True, 'data': data['msg'], 'msg': u'Insertando elemento'}
    
    @restobject.post_into
    def prueba_post_general(self, elemento):
        data = json.loads(web.data())
        return {'success': True, 'id': elemento, 'data': data['msg'], 'msg': u'Insertando en elemento'}
    
    @restobject.post_list("valores")
    def prueba_post_valores(self, elemento):
        data = json.loads(web.data())
        return {'success': True, 'id': elemento, 'list': 'valores', 'data': data['msg'], 'msg': u'Insertando en lista'}
    
    @restobject.put_all
    def prueba_put(self):
        data = json.loads(web.data())
        return {'success': True, 'data': data['msg'], 'msg': u'Reemplazando todo'}
    
    @restobject.put
    def prueba_put_element(self, elemento):
        data = json.loads(web.data())
        return {'success': True, 'id': elemento, 'data': data['msg'], 'msg': u'Reemplazando elemento'}
    
    @restobject.put_list("valores")
    def prueba_put_valores(self, elemento):
        data = json.loads(web.data())
        return {'success': True, 'id': elemento, 'list': 'valores', 'data': data['msg'], 'msg': u'Reemplazando en lista'}
    
    @restobject.delete_all
    def prueba_delete(self):
        return {'success': True, 'msg': u'Eliminando todo'}
    
    @restobject.delete
    def prueba_delete_element(self, elemento):
        return {'success': True, 'id': elemento, 'msg': u'Eliminando elemento individual'}
    
    @restobject.delete_list("valores")
    def prueba_delete_valores(self, elemento):
        return {'success': True, 'id': elemento, 'list': 'valores', 'msg': u'Eliminando lista del elemento'}
    
class BasicTest(unittest.TestCase):
    def setUp(self):
        self.request = Request(urls)
        
    def test_get(self):
        u'Pruebas para el método get'
        rand = ''.join(random.sample(string.lowercase + string.digits, 4))
        result = json.loads(self.request.get('/basic/'))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado fue exitoso')
        result = json.loads(self.request.get('/basic/%s' % rand))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(result['id'], rand, 'El resultado no es correcto')
        result = json.loads(self.request.get('/basic/%s/%s' % (rand, 'valores')))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(rand, result['id'], 'El elemento no es correcto')
        self.assertEquals('valores', result['list'], 'La lista no es correcta')
        
    def test_post(self):
        u'Pruebas para el método post'
        rand = ''.join(random.sample(string.lowercase + string.digits, 4))
        hola_mundo = 'hola mundo!';
        data = json.dumps({'msg': hola_mundo})
        result = json.loads(self.request.post('/basic/', data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado fue exitoso')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
        result = json.loads(self.request.post('/basic/%s' % rand, data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(result['id'], rand, 'El resultado no es correcto')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
        result = json.loads(self.request.post('/basic/%s/%s' % (rand, 'valores'), data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(rand, result['id'], 'El elemento no es correcto')
        self.assertEquals('valores', result['list'], 'La lista no es correcta')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
        
    def test_put(self):
        u'Pruebas para el método put'
        rand = ''.join(random.sample(string.lowercase + string.digits, 4))
        hola_mundo = 'hola mundo!';
        data = json.dumps({'msg': hola_mundo})
        result = json.loads(self.request.put('/basic/', data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado fue exitoso')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
        result = json.loads(self.request.put('/basic/%s' % rand, data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(result['id'], rand, 'El resultado no es correcto')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
        result = json.loads(self.request.put('/basic/%s/%s' % (rand, 'valores'), data))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(rand, result['id'], 'El elemento no es correcto')
        self.assertEquals('valores', result['list'], 'La lista no es correcta')
        self.assertEquals(hola_mundo, result['data'], 'Los datos no son correctos')
    
    def test_delete(self):
        u'Pruebas para el método delete'
        rand = ''.join(random.sample(string.lowercase + string.digits, 4))
        result = json.loads(self.request.delete('/basic/'))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado fue exitoso')
        result = json.loads(self.request.delete('/basic/%s' % rand))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(result['id'], rand, 'El resultado no es correcto')
        result = json.loads(self.request.delete('/basic/%s/%s' % (rand, 'valores')))
        self.assertIsNotNone(result, 'No se recuperó ningún resultado')
        self.assertTrue(result['success'], 'El resultado no fue exitoso')
        self.assertEquals(rand, result['id'], 'El elemento no es correcto')
        self.assertEquals('valores', result['list'], 'La lista no es correcta')

class SimpleAuth1(auth.Auth):
    def __init__(self):
        self.key = "1234"
        
class SimpleAuth2(auth.Auth):
    def __init__(self):
        super(SimpleAuth2, self).__init__("1234")

class SimpleAuth3(auth.Auth):
    def __init__(self):
        self.key = "1234"
        self.algorithm = self.DEFAULT_ALGORITHM
        
class SimpleAuth4(auth.Auth):
    def __init__(self):
        self.key = "1234"
        self.algorithm = auth.Auth.DEFAULT_ALGORITHM

class Authenticated(restobject.RestObject):
    @auth.auth(SimpleAuth1)
    @restobject.get_all
    def prueba_autenticacion(self):
        return {"success": True, "mensaje": "autorizado GET"}
    
    @auth.auth(SimpleAuth2)
    @restobject.post
    def prueba_auth_post(self):
        return {"success": True, "mensaje": "autorizado POST"}
    
    @auth.auth(SimpleAuth3)
    @restobject.put_all
    def prueba_auth_put(self):
        return {"success": True, "mensaje": "autorizado PUT"}
    
    @auth.auth(SimpleAuth4)
    @restobject.delete_all
    def prueba_auth_del(self):
        return {"success": True, "mensaje": "autorizado DELETE"}
    
class TestAuthenticated(unittest.TestCase):
    def setUp(self):
        self.request = Request(urls)
        self.key = "1234"
    
    def test_authentication(self):
        timestamp = str(int(time.time()))
        datastring = unicode(u"GET /auth/?data=áéíóúñ&timestamp=" + timestamp + ' ')
        signature = hmac.new(self.key, datastring.encode('utf-8'), hashlib.sha256).hexdigest()
        response = json.loads(self.request.get('/auth/?data=áéíóúñ&timestamp=' + timestamp + '&signature=' + signature, ''))
        self.assertIsNotNone(response, 'No se recuperaron resultados')
        self.assertTrue(response['success'], 'Falló la petición')
        self.assertEquals('autorizado GET', response['mensaje'], 'Mensaje no corresponde')
        data = json.dumps({"prueba": u"áéíóúñ"})
        datastring = unicode(u"POST /auth/?data=áéíóúñ&timestamp=" + timestamp + ' ' + data)
        signature = hmac.new(self.key, datastring.encode('utf-8'), hashlib.sha256).hexdigest()
        response = json.loads(self.request.post('/auth/?data=áéíóúñ&timestamp=' + timestamp + '&signature=' + signature, data))
        self.assertIsNotNone(response, 'No se recuperaron resultados')
        self.assertTrue(response['success'], 'Falló la petición')
        self.assertEquals('autorizado POST', response['mensaje'], 'Mensaje no corresponde')
        data = json.dumps({"prueba": u"áéíóúñ"})
        datastring = unicode(u"PUT /auth/?data=áéíóúñ&timestamp=" + timestamp + ' ' + data)
        signature = hmac.new(self.key, datastring.encode('utf-8'), hashlib.sha256).hexdigest()
        response = json.loads(self.request.put('/auth/?data=áéíóúñ&timestamp=' + timestamp + '&signature=' + signature, data))
        self.assertIsNotNone(response, 'No se recuperaron resultados')
        self.assertTrue(response['success'], 'Falló la petición')
        self.assertEquals('autorizado PUT', response['mensaje'], 'Mensaje no corresponde')
        data = json.dumps({"prueba": u"áéíóúñ"})
        datastring = unicode(u"DELETE /auth/?data=áéíóúñ&timestamp=" + timestamp + ' ' + data)
        signature = hmac.new(self.key, datastring.encode('utf-8'), hashlib.sha256).hexdigest()
        response = json.loads(self.request.delete('/auth/?data=áéíóúñ&timestamp=' + timestamp + '&signature=' + signature, data))
        self.assertIsNotNone(response, 'No se recuperaron resultados')
        self.assertTrue(response['success'], 'Falló la petición')
        self.assertEquals('autorizado DELETE', response['mensaje'], 'Mensaje no corresponde')
    
    def test_failed_authentication(self):
        pass
    
    def tearDown(self):
        pass
    
credentials = {'username': 'hola', 'password': 'mundo'}
class HTTPAuth(restobject.RestObject):
    @auth.http_auth(credentials)
    @restobject.get_all
    def prueba_autenticacion_get(self):
        return self._resp("mensaje", "autorizado GET por HTTP")
    
    @auth.http_auth(credentials)
    @restobject.post
    def prueba_autenticacion_post(self):
        return self._resp("mensaje", "autorizado POST por HTTP")
    
    @auth.http_auth(credentials)
    @restobject.put_all
    def prueba_autenticacion_put(self):
        return self._resp("mensaje", "autorizado PUT por HTTP")
    
    @auth.http_auth(credentials)
    @restobject.delete_all
    def prueba_autenticacion_delete(self):
        return self._resp("mensaje", "autorizado DELETE por HTTP")
