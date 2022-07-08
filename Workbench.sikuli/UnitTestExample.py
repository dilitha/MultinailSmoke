import unittest
import HTMLTestRunner
reload(HTMLTestRunner)

class TestDemo(unittest.TestCase):
    def testA(self):
        assert True
    def testB(self):
        assert False

class TestDemo2(unittest.TestCase):
    def testC(self):
        assert True
    def testD(self):
        assert True

def suite():
    suite = unittest.TestSuite()
    # TestDemo
    suite.addTest(TestDemo('testA'))
    suite.addTest(TestDemo('testB'))
    # TestDemo2
    suite.addTest(TestDemo2('testC'))
    suite.addTest(TestDemo2('testD'))

    return suite

if __name__ == "__main__":
    suite = suite()
    unittest.TextTestRunner(verbosity=2)
    output = open(getBundlePath()+"\\results.html", 'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=output, title='Test Report', description='This is a test')
    runner.run(suite)  
