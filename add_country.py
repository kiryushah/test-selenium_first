# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class add_country(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") 
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)

    def test_adding(self):
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()

        self.driver.find_element_by_xpath("//span[text()='Countries']").click()

        self.driver.find_element_by_xpath("//a[@class='button']").click()

        main_window = self.driver.current_window_handle
        
        targets = self.driver.find_elements_by_xpath("//a[@target = '_blank']")

        for i in targets:
            i.click()
            self.driver.implicitly_wait(30)

        old_windows = self.driver.window_handles


        for a in old_windows:
            wait = WebDriverWait(self.driver, 30)
            if a != main_window:
                self.driver.switch_to_window(a)
                self.driver.close()
                self.driver.switch_to_window(main_window)
            else:
                print('main_window')
                

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
