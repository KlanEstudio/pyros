#coding: utf-8

def load_tests(loader, tests, pattern):
    import test_test

    tests.addTests(loader.loadTestsFromModule(test_test))
    return tests
