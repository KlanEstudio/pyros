#coding: utf-8

import unittest
import json, random, string
from pyros.test.request import Request
from test.config import urls

class TestPrueba(unittest.TestCase):
    def setUp(self):
        self.request = Request(urls)
    
    def test_probar(self):
        rand = ''.join(random.choice(string.lowercase + string.digits) for i in range(4))
        req = ['', rand, rand + '/valores', rand + '/valores/']
        for r in req:
            self.assertIsNotNone(self.request.get('/basic/' + r))
