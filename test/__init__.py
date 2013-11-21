#coding: utf-8

import test_test

def load_tests(loader, tests, pattern):
    tests.addTests(loader.loadTestsFromModule(test_test))
    return tests
