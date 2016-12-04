# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class AddProductTest(unittest.TestCase):


    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()

    def test_LogIn(self):
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()

        catalog = self.driver.find_element_by_xpath("//span[text() = 'Catalog']").click()
        add_new_product = self.driver.find_element_by_xpath("//a[text() = ' Add New Product']").click()
        enabled = self.driver.find_element_by_xpath("//label[text() = ' Enabled']").click()
        name = self.driver.find_element_by_xpath("//input[@name = 'name[en]']").send_keys('Alive duck')
        code = self.driver.find_element_by_xpath("//input[@name = 'code']").send_keys('A1-1a')
        select_category = self.driver.find_element_by_xpath("//input[@data-name='Rubber Ducks']").click()
        male = self.driver.find_element_by_xpath("//input[@value = '1-1']").click()
        quantity = self.driver.find_element_by_xpath("//input[@name = 'quantity']").clear()
        quantity = self.driver.find_element_by_xpath("//input[@name = 'quantity']").send_keys('100')
        upload = self.driver.find_element_by_xpath("//input[@name='new_images[]']").send_keys("C:\duck.jpg")
        date_from = self.driver.find_element_by_name('date_valid_from').click()
        date_from = self.driver.find_element_by_name('date_valid_from').send_keys('02 12 2016')
        date_to = self.driver.find_element_by_name('date_valid_to').click()
        date_to = self.driver.find_element_by_name('date_valid_to').send_keys('04 12 2016')
        
        information = self.driver.find_element_by_xpath("//a[text()='Information']").click()
        manufacturer = self.driver.find_element_by_xpath("//select[@name='manufacturer_id']")
        self.driver.execute_script("arguments[0].selectedIndex = 1; arguments[0].dispatchEvent(new Event('change'))", manufacturer)
        keywords = self.driver.find_element_by_name('keywords').send_keys('keyword, duck, alive')
        short_description = self.driver.find_element_by_name('short_description[en]').send_keys('short_description')
        description = self.driver.find_element_by_xpath("//div[@class='trumbowyg-editor']").send_keys('description')
        head_title = self.driver.find_element_by_name('head_title[en]').send_keys('alive duck')
        meta_description = self.driver.find_element_by_name('meta_description[en]').send_keys('meta_description')
        
        prices = self.driver.find_element_by_xpath("//a[text()='Prices']").click()
        purchase_price = self.driver.find_element_by_name('purchase_price').clear()
        purchase_price = self.driver.find_element_by_name('purchase_price').send_keys('19')
        purchase_price_currency_code = self.driver.find_element_by_name('purchase_price_currency_code')
        self.driver.execute_script("arguments[0].selectedIndex = 2; arguments[0].dispatchEvent(new Event('change'))", purchase_price_currency_code)
        usd_price = self.driver.find_element_by_name('prices[USD]').send_keys('100')
        save = self.driver.find_element_by_xpath("//button[@name='save']").click()
        assert_element = self.driver.find_element_by_xpath("//a[text()='Alive duck']")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
