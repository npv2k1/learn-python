import argparse
import sys
from random import randint
from time import sleep

from selenium import webdriver

FB_URL = "https://fb.com"


def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


class FacebookLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):

        #open

        self.driver.get("https://www.office.com/?auth=2")
        #username
        username_ele = self.driver.find_element_by_css_selector('#i0116')
        username_ele.send_keys(self.username)
        sleep(1)
        username_Click = self.driver.find_element_by_css_selector(
            '#idSIButton9')
        sleep(1)
        username_Click.click()

        sleep(2)
        password_ele = self.driver.find_element_by_css_selector('#i0118')
        sleep(1)
        password_ele.send_keys(self.password)
        sleep(1)
        login_ele = self.driver.find_element_by_css_selector(
            '#idSIButton9')
        sleep(1)
        login_ele.click()

    def verify_login(self):
        try:
            self.driver.find_element_by_css_selector('#email')
            return False
        except:
            return True


if __name__ == '__main__':
    fb = FacebookLogin('oe023@microco.net', "Pvn10092001")
    fb.login()
    # if fb.verify_login():
    #     print('Đăng nhập thành công!')
    # else:
    #     print('Đăng nhập thất bại')

    # fb.driver.close()
