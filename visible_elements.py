# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class visible_elements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") 
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)


    def test_clickelements(self):
        self.driver.get("http://localhost/litecart/en/")
        
        rows = self.driver.find_elements_by_xpath("//li[@class='product column shadow hover-light']")

        def are_elements_present(self, *args):
            return len(self.driver.find_elements(*args)) == 1 

        are_elements_present(self, By.XPATH, "//div[@class='sticker sale']" and "//div[@class='sticker new']" ) in rows 

                            
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

