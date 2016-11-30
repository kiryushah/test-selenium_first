# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class clickelements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()
        self.driver.implicitly_wait(20)


    def test_clickelements(self):
        self.driver.get("http://localhost/litecart/")
    
        register = self.driver.find_element_by_xpath("//a[text()='New customers click here']").click()
        
        firstname = self.driver.find_element_by_xpath("//input[@name='firstname']").send_keys("Kirill")
        lastname = self.driver.find_element_by_xpath("//input[@name='lastname']").send_keys("Berdyugin")
        address = self.driver.find_element_by_xpath("//input[@name='address1']").send_keys("Stachek 88")
        postcode = self.driver.find_element_by_xpath("//input[@name='postcode']").send_keys("183221")
        city = self.driver.find_element_by_xpath("//input[@name='city']").send_keys("Saint-Petersburg")
        select = self.driver.find_element_by_xpath("//select[@name='country_code']")
        self.driver.execute_script("arguments[0].selectedIndex = 176; arguments[0].dispatchEvent(new Event('change'))", select)
        email_one = self.driver.find_element_by_xpath("//input[@name='email']").send_keys("blah9@blah.ru") #вставьте email, который свободен
        phone = self.driver.find_element_by_xpath("//input[@name='phone']").send_keys("+79991234567")
        newsletter = self.driver.find_element_by_xpath("//input[@name='newsletter']").click()
        password = self.driver.find_element_by_xpath("//input[@name='password']").send_keys("123qwe")
        confirm_password = self.driver.find_element_by_xpath("//input[@name='confirmed_password']").send_keys("123qwe")
        create = self.driver.find_element_by_xpath("//button[@name='create_account']").click()
        logout = self.driver.find_element_by_xpath("//a[text()='Logout']").click()

        email_two = self.driver.find_element_by_xpath("//input[@name='email']").send_keys("blah9@blah.ru" + Keys.TAB) #вставьте email, совпадающий с email_one
        password = self.driver.find_element_by_xpath("//input[@name='password']").send_keys("123qwe"  + Keys.TAB)
        remember_me = self.driver.find_element_by_xpath("//input[@name='remember_me']").click()
        login = self.driver.find_element_by_xpath("//button[@name='login']").send_keys(Keys.ENTER)

        
        
                
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
