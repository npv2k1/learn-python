
from selenium import webdriver
from selenium import *
import os
import time

# class HelloSelenium:
#     def __init__(self, url):
#         self.driver = webdriver.Firefox()
#         self.driver.get(url)
#
#     def get_site_info(self):
#         print('URL:', self.driver.current_url)
#         print('Title:', self.driver.title)
#         sleep(5)
#         self.driver.save_screenshot('screen_shot.png')


if __name__ == '__main__':
    # hello = HelloSelenium('https://google.com')
    # hello.get_site_info()
    # Close driver
    #hello.driver.close()
    driver = webdriver.Chrome()
    driver.get("https://facebook.com")
    driver.find_element_by_id("email").send_keys("@gmail.com")
    driver.find_element_by_id("pass").send_keys("")
    driver.find_element_by_id("u_0_b").click()
    time.sleep(1)
    driver.get(
        "https://www.facebook.com/groups/gnsupport/pending_posts?search=&has_selection=false")
    time.sleep(1)
    a=driver.find_elements_by_class_name('tr9rh885')
    for i in a:
        print(i.get_attribute("textContent"))
    # driver.quit()
