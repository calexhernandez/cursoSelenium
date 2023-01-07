import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path='./chromedriver')
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(cls):
        drive = cls.driver
        drive.get('https://www.platzi.com')

    def test_visit_wikipedia(cls):
        driver = cls.driver.get('https://www.wikipedia.org')
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner= HTMLTestRunner(output='reportes', report_name='hello_world_report, '))