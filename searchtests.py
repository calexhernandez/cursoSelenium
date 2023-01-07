import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class HomePageTest(unittest.TestCase):
    def setUp(self):
        s=Service('./chromedriver')
        # establecemos la referencia del driver
        self.driver = webdriver.Chrome(service=s)
        driver = self.driver
        driver.get("http://demo-store.seleniumacademy.com/")
        driver.maximize_window()
        #driver.implicitly_wait(15)

    #def test_search_text_field(self):
        #search_field = self.driver.find_element("id","search")

    #def test_search_text_field_by_name(self):
        #search_field = self.driver.find_element("name","q")

    def test_search_by_class(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME,"search-button")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)

