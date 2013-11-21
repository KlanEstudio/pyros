#coding: utf-8

def load_tests(loader, tests, pattern):
    import simple

    tests.addTests(loader.loadTestsFromModule(simple))
    return tests
