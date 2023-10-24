#! /usr/bin/env python3
# This will simulate a platform mismatch
# Inspired by Opera ua monkey patching
import os
import sys
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from random import randint
from time import sleep

loops = 10

# Mask remote browser
options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
#options.add_argument("--headless=new") # Doesn't work in headless
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 OPR/102.0.0.0 (Edition std-1)")

#config
for x in range(loops):
    url = "https://www.threadgremlin.clothing/"
    driver = webdriver.Chrome(options)

    driver.get(url)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.5845.188 Safari/537.36", "platform":"Windows"})

driver.quit()