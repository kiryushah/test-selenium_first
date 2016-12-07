# -*- coding: utf-8 -*-
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

class visible_elements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("C://chromedriver/chromedriver.exe") 
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 40)

    def test_geozone(self):
        self.driver.get("http://localhost/litecart/admin/")
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()

        countries = self.driver.find_element_by_xpath("//span[text()='Countries']").click()
        table = self.driver.find_element_by_xpath("//table[@class='dataTable']")
        rows = table.find_elements_by_xpath("//tr[@class='row']")
        country_row = [] 
        for row in rows:
            country = row.find_element_by_xpath("./td[5]").text
            country_row.append(country)
        if country_row == sorted(country_row):
            print('ok')
        else:
            print('fail')

        table = self.driver.find_element_by_xpath("//table[@class='dataTable']")
        zone = table.find_elements_by_xpath("//tr[@class='row']")
        non_zero = []
        for i in range(len(zone)):
            if zone[i].find_element_by_xpath("./td[6]").text != '0':
                non_zero.append(i)
                print(non_zero)
   
        
        for ind in non_zero:
                table = self.driver.find_element_by_xpath("//table[@class='dataTable']")
                rows = table.find_elements_by_xpath("//tr[@class='row']")[ind]
                click_rows = rows.find_element_by_tag_name('a').click()
                table_zones = self.driver.find_elements_by_xpath("//*[@id='table-zones']/tbody/tr/td[3]")
                del table_zones[len(table_zones)-1]
                zones_list = []
                for a in table_zones:
                    zzz=a.get_attribute('textContent')
                    zones_list.append(zzz)
                if zones_list == sorted(zones_list):
                    print('ok')
                else:
                    print('fail')
      
                countries = self.driver.find_element_by_xpath("//span[text()='Countries']").click()
                print(zones_list)
                print(sorted(zones_list))

    def test_geozonesort(self):
        self.driver.get('http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones')
        self.driver.find_element_by_name('username').send_keys('admin')
        self.driver.find_element_by_name('password').send_keys('admin')
        self.driver.find_element_by_name('remember_me').click()
        self.driver.find_element_by_name('login').click()

        geo = len(self.driver.find_elements_by_xpath("//tr[@class = 'row']"))
        for i in range(geo):
            self.driver.find_elements_by_xpath("//tr[@class = 'row']")[i].find_element_by_tag_name('a').click()
            select_zones = self.driver.find_elements_by_xpath("//*[@id='table-zones']/tbody/tr/td[3]/select")
            name_zones = []
            for b in select_zones:
                bbb = b.text
                name_zones.append(bbb)                
                if name_zones == sorted(name_zones):
                    print('ok')
                else:
                    print('false')
                    
            geo_zones=self.driver.find_element_by_xpath("//span[text()='Geo Zones']").click()
            print(name_zones)
            print(sorted(name_zones))            
                            
    def tearDown(self)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

