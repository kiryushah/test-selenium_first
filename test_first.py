# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver


class VkComLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()

    def test_LogIn(self):
        self.driver.get("http://www.vk.com")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    
