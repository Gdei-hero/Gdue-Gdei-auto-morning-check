# -*- coding: utf-8 -*-
from selenium import webdriver
import time

def main():
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'  #chromedriver的文件位置
    driver = webdriver.Chrome(executable_path = chrome_driver)
    driver.get('https://tb.gdei.edu.cn/login')
    
    username=""#用户名
    password=""#密码
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
    
    time.sleep(1)
    driver.switch_to.frame("iframe0")
    driver.find_element_by_xpath("(//button[@class='btn  '])[2]").click()
    
    driver.switch_to.default_content()
    time.sleep(1)
    driver.switch_to.frame("iframe0")
    
    time.sleep(2)
    exit()

if __name__ == '__main__':
    main()
    
