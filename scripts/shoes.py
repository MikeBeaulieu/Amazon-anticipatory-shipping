from selenium import webdriver
from lxml import etree

import stor

DATA_PATH = '../data/'

def fetch_good():
    driver = webdriver.Chrome()
    driver.get()
