from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium import *
import os
import time
import pyautogui
from selenium.webdriver import ActionChains

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
    
    options = webdriver.ChromeOptions()
    # options.add_argument("headless")
    # options.add_argument("window-size=1500,1200")
    # options.add_argument("no-sandbox")
    # options.add_argument("disable-dev-shm-usage")
    # options.add_argument("disable-gpu")
    # options.add_argument("log-level=3")
    # options.add_argument(f"user-agent={userAgent}")
    
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome("chromedriver.exe",options=options)
    action = ActionChains(driver)
    driver.get("https://facebook.com")
    driver.find_element_by_id("email").send_keys("TODO: email")
    driver.find_element_by_id("pass").send_keys("")
    driver.find_element_by_id("u_0_b").click()
    time.sleep(1)
    driver.get(
        "https://www.facebook.com/photo?fbid=1188767564926478&set=g.697332711026460")
    time.sleep(1)
    # elem = driver.find_element_by_xpath(
    #     '//*[@id="mount_0_0"]/div/div[1]/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div[1]/div[3]/div/div')
    
    # driver.execute_script('arguments[0].click();', elem)
    # time.sleep(2)
    driver.execute_script('''
    document.querySelectorAll('[aria-haspopup="menu"]')
    document.querySelectorAll('[aria-haspopup="menu"]')[1].click();
    ''')
    time.sleep(1)
    print('ok')
    # driver.execute_script('''
    # document.querySelectorAll('[data-pagelet="root"')[3].getElementsByTagName('a')[0].click()
    # document.querySelectorAll('[data-pagelet="root"')[3].getElementsByTagName('a')[0].getAttribute('href')''')

    tmp = driver.find_elements_by_css_selector('[data-pagelet="root"')
    tmp[3].click()

    # elem=driver.find_element_by_xpath(
    #     '//div[contains(@aria-label, "Gửi tin nhắn")]') 
    driver.find_element_by_css_selector

    a = driver.find_element_by_tag_name('body')
    # time.sleep(1)
    # driver.execute_script('arguments[0].click();', elem)
    # a = driver.find_elements_by_xpath('//div[contains(@class,"_5rpu")]')
    # # driver.execute_script('arguments[0].click();', a)
    # print(a)

    a.send_keys(Keys.ARROW_RIGHT)
    # pyautogui.keyDown('right')
    # driver.quit()
    with open('log.txt', 'wa') as log:
        log.write(driver.current_url)
