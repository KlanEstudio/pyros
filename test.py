#!/usr/bin/env python
#coding: utf-8

import unittest

if __name__ == '__main__':
    suite = unittest.TestSuite(unittest.defaultTestLoader.discover('.', pattern = 'test'))
    unittest.TextTestRunner().run(suite)
