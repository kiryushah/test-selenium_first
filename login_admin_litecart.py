# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class AdminLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()

    def test_LogIn(self):
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
