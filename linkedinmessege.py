#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 21:29:19 2018

@author: atuljain
"""

from selenium import webdriver 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import time 
  
# Replace below path with the absolute path 
# to chromedriver in your computer 
driver = webdriver.Chrome('/Applications/Google Chrome.app/Contents/MacOS') 
  
driver.get("https://www.linkedin.com/uas/login?") 
wait = WebDriverWait(driver, 600) 
  
a = @driver.find_element(:xpath, '//*[@id="login-email"]').send_Keys('atulj968@gmail.com')
a = @driver.find_element(:xpath, '//*[@id="login-password"]').send_Keys('***********')
a = @driver.find_element(:xpath, '//*[@id="login-submit"]').click
sleep 5
a = @driver.find_element(:xpath, '//*[@id="messaging-tab-icon"]').click
a = @driver.find_element(:xpath, '//*[@id="ember2679"]/span/li-icon/svg').click
a = @driver.find_element(:xpath, '//*[@id="ember13950-search-field"]').send_Keys('//*[@id="ember13950"]/ul/li[2]/span','//*[@id="ember13950"]/ul/li[1]/span')
sleep 5
a = @driver.find_element(:xpath, '//*[@id="ember23891"]').send_Keys('Group name')
sleep 2;p 'This is Where I clicked/initiated the Send Message '
a = @driver.find_element(:xpath, '//*[@id="ember13956"]/div[1]/p')
a.send_Keys('Hello Everyone,My name is Atul and this messege send using selenium driver') # This is where I entered the keys and Did Enter
a.send_Keys:enter
a = @driver.find_element(:xpath, '//*[@id="attachment-trigger-ember23563"]/li-icon/svg').click # This is where you choose a photo
a.send_Keys:enter
