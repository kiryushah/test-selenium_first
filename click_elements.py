# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver

class AdminLogIn(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()

    def test_LogIn(self):
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()
        
        self.driver.find_element_by_xpath("//li[@id='app-'][1]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-logotype']").click()
        self.driver.find_element_by_css_selector('h1')
        
        self.driver.find_element_by_xpath("//li[@id='app-'][2]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-product_groups']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-option_groups']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-manufacturers']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-suppliers']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-delivery_statuses']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-sold_out_statuses']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-quantity_units']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-csv']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][3]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][4]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][5]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-csv']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-newsletter']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][6]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][7]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-storage_encoding']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][8]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-customer']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-shipping']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-payment']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-order_total']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-order_success']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-order_action']").click()
        self.driver.find_element_by_css_selector('h1')
        
        self.driver.find_element_by_xpath("//li[@id='app-'][9]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-order_statuses']").click()
        self.driver.find_element_by_css_selector('h1')
        
        self.driver.find_element_by_xpath("//li[@id='app-'][10]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][11]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-most_sold_products']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-most_shopping_customers']").click()
        self.driver.find_element_by_css_selector('h1')
       
        self.driver.find_element_by_xpath("//li[@id='app-'][12]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-defaults']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-general']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-listings']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-images']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-checkout']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-advanced']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-security']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][13]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][14]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-tax_rates']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][15]").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-scan']").click()
        self.driver.find_element_by_css_selector('h1')
        self.driver.find_element_by_xpath("//li[@id='doc-csv']").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][16]").click()
        self.driver.find_element_by_css_selector('h1')

        self.driver.find_element_by_xpath("//li[@id='app-'][17]").click()
        self.driver.find_element_by_css_selector('h1')
                
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
