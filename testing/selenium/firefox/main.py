import argparse
import sys
from random import randint
from time import sleep

from selenium import webdriver

FB_URL = "https://fb.com"


def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get(FB_URL)
