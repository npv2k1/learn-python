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
        self.driver.get(FB_URL)
        username_ele = self.driver.find_element_by_css_selector('#email')
        username_ele.send_keys(self.username)
        random_sleep(1, 5)
        password_ele = self.driver.find_element_by_css_selector('#pass')
        password_ele.send_keys(self.password)
        random_sleep(1, 5)
        login_ele = self.driver.find_element_by_css_selector(
            '#loginbutton > input[type="submit"]')
        random_sleep(1, 5)
        login_ele.click()

    def verify_login(self):
        try:
            self.driver.find_element_by_css_selector('#email')
            return False
        except:
            return True


if __name__ == '__main__':
    # parser = argparse.ArgumentParser(description='Auto FB login')
    # parser.add_argument('--username', default=None,
    #                     required=True, help='FB username')
    # parser.add_argument('--password', default=None,
    #                     required=True, help='FB password')

    # try:
    #     options = parser.parse_args()
    # except:
    #     parser.print_help()
    #     sys.exit(0)

    fb = FacebookLogin('01287295909', "Pvn10092001")
    fb.login()
    if fb.verify_login():
        print('Đăng nhập thành công!')
    else:
        print('Đăng nhập thất bại')

    fb.driver.close()
