# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC



class add_items(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") 
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 30)

    def test_adding(self):
        self.driver.get("http://localhost/litecart/")
        product_one = self.driver.find_element_by_xpath("//a[@title = 'Yellow Duck']").click()
        select = self.driver.find_element_by_name('options[Size]')
        self.driver.execute_script("arguments[0].selectedIndex = 2; arguments[0].dispatchEvent(new Event('change'))", select)
        cart = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item = cart.find_element_by_xpath("//span[text()='0']")       
        add_cart_product = self.driver.find_element_by_name('add_cart_product').click()
        
        wait_i = self.driver.implicitly_wait(30)
        cart_new = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item_new = cart.find_element_by_xpath("//span[text()='1']")
        home = self.driver.find_element_by_css_selector("#site-menu > ul > li.general-0 > a").click()

        product_two = self.driver.find_element_by_xpath("//a[@title = 'Green Duck']").click()
        cart = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item = cart.find_element_by_xpath("//span[text()='1']")
        add_cart_product = self.driver.find_element_by_name('add_cart_product').click()

        wait_i = self.driver.implicitly_wait(30)
        cart_new = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item_new = cart.find_element_by_xpath("//span[text()='2']")
        home = self.driver.find_element_by_css_selector("#site-menu > ul > li.general-0 > a").click()

        product_three = self.driver.find_element_by_xpath("//a[@title = 'Purple Duck']").click()
        cart = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item = cart.find_element_by_xpath("//span[text()='2']")
        add_cart_product = self.driver.find_element_by_name('add_cart_product').click()

        wait_i = self.driver.implicitly_wait(30)
        cart_new = self.driver.find_element_by_xpath("//div[@id = 'cart']")
        cart_item_new = cart.find_element_by_xpath("//span[text()='3']")
        home = self.driver.find_element_by_css_selector("#site-menu > ul > li.general-0 > a").click()

        checkout = self.driver.find_element_by_xpath("//a[text()='Checkout »']").click()
        table = self.driver.find_element_by_xpath("//table[@class ='dataTable rounded-corners']")
        shortcut = self.driver.find_element_by_xpath("//*[@id='box-checkout-cart']/ul/li[2]/a").click()
        delete = self.driver.find_element_by_name('remove_cart_item').click()





    def tearDown(self)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
