# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class regularsale(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") #В скобках указываем путь к chromedriver.exe
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)


    def test_regularsale(self):
        self.driver.get("http://localhost/litecart/")
    
        yellow = self.driver.find_element_by_xpath("//div[@id='box-campaigns']")
        duck = yellow.find_element_by_xpath("//a[@title='Yellow Duck']").click()
        regular_text = self.driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('text-decoration')
        print(regular_text)
        regular_font = self.driver.find_element_by_xpath("//s[@class='regular-price']").value_of_css_property('font-size')
        print(regular_font)
        campaign_weight = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-weight')
        print(campaign_weight)
        campaign_size = self.driver.find_element_by_xpath("//strong[@class='campaign-price']").value_of_css_property('font-size')
        print(campaign_size)
        if regular_text == ('line-through'):
            print('true regular text decoration')
        else:
            print('false')
        if regular_font == ('16px'):
            print('true regular font-size')
        else:
            print('false')
        if campaign_weight == ('bold'):
            print('true campaign weight')
        else:
            print('false')
        if campaign_size == ('22px'):
            print('true campaign font-size')
        else:
            print('false')
                
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
