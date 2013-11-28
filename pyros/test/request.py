#coding: utf-8

import web

class StatusError(Exception):
    pass

class Request:
    def __init__(self, urls):
        web.config.debug = True
        self.app = web.application(urls, globals())
    
    def get(self, url, body = None):
        response = self.app.request(url, method = 'GET', data = body)
        if response.status != '200 OK':
            raise StatusError(response.status)
        return response.data
    
    def post(self, url, body):
        response = self.app.request(url, method = 'POST', data = body)
        if response.status != '200 OK':
            raise StatusError(response.status)
        return response.data
    
    def put(self, url, body):
        response = self.app.request(url, method = 'PUT', data = body)
        if response.status != '200 OK':
            raise StatusError(response.status)
        return response.data
    
    def delete(self, url, body = None):
        response = self.app.request(url, method = 'DELETE', data = body)
        if response.status != '200 OK':
            raise StatusError(response.status)
        return response.data
