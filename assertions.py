import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException

class AssertionsTest(unittest.TestCase):
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

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, 'q'))

    def test_language_option(self):
        self.asserTrue(self.is_element_present(By.ID, 'select-language'))

    def test_search_tee(self):
        driver = self.driver
        search_field = self.driver.find_element(By.CLASS_NAME, "q")
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver = self.driver
        search_field = self.driver.find_element(By.CLASS_NAME, "q")

        search_field.send_keys('salt shaker')
        search_field.submit()

        products = driver.find_elements_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1, len(products))


    def test_search_by_class(self):
        search_field = self.driver.find_element(By.CLASS_NAME, "input-text")

    def test_search_button_enabled(self):
        button = self.driver.find_element(By.CLASS_NAME,"search-button")

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True


if __name__ == "__main__":
    unittest.main(verbosity=2)

