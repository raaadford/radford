#!/usr/bin/env python
# -*- coding:utf-8 -*-

from selenium import webdriver
import datetime
import time


myoptions = webdriver.firefox.options.Options()
myoptions.add_argument('-headless')

mydriver = webdriver.Firefox()
def login(username, password):
    time.sleep(1)
    mydriver.get("https://user.qzone.qq.com/1247355707/main")
    time.sleep(1)
    
    mydriver.switch_to.frame('login_frame')
    mydriver.find_element_by_id('switcher_plogin').click()
    
    mydriver.find_element_by_name('u').clear()
    mydriver.find_element_by_name("u").send_keys(username)
    mydriver.find_element_by_name('p').clear()
    mydriver.find_element_by_name("p").send_keys(password)
    time.sleep(1)
    mydriver.find_element_by_id("login_button").click()
    
    time.sleep(3)
    # mydriver.get("https://user.qzone.qq.com/1247355707/main")
    # mydriver.find_element_by_id("QM_Profile_Photo_Cnt").click()
    mydriver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/div[4]/div/div/ul/li[3]/a").click()
    # mydriver.close()
    
login('1247355707', '123456789....')
