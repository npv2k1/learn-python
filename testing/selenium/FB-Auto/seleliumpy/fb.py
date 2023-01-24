from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium import *
import os
import time
import pyautogui
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    
    
    options = webdriver.ChromeOptions()
  
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    action = ActionChains(driver)
    driver.get("https://facebook.com")
    driver.find_element_by_id("email").send_keys("@gmail.com")
    driver.find_element_by_id("pass").send_keys("")
    driver.find_element_by_id("u_0_b").click()
    time.sleep(1)

    driver.get(
        "https://www.facebook.com/photo?fbid=1188767564926478&set=g.697332711026460")
    time.sleep(2)
    
    # Find
    while(True):
        try:

            driver.execute_script('''
            document.querySelectorAll('[aria-haspopup="menu"]')
            document.querySelectorAll('[aria-haspopup="menu"]')[1].click();
            ''')
            break
        except:
            continue
    time.sleep(1)
    # Download:
    while(True):
        try:
            tmp = driver.find_elements_by_css_selector('[data-pagelet="root"')
            tmp[3].click()
            break
        except:
            continue

    # Write log
    with open('log.txt', 'a') as log:
        log.write(driver.current_url)

    # next img
    a = driver.find_element_by_tag_name('body')
    a.send_keys(Keys.ARROW_RIGHT)   
