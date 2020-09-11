from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://csssr.github.io/qa-engineer/")
    
    time.sleep(10)

    input1 = browser.find_element_by_xpath("//div[@class=\"wrap\"]/footer/div/div/input")
    input1.send_keys("test@test.com")
    input2 = browser.find_element_by_xpath("//div[@class=\"wrap\"]/footer/div/div[2]/textarea")
    input2.send_keys("Здравствуйте! Жду Вашего ответа!")
    button3 = browser.find_element_by_xpath("//div[@class=\"wrap\"]/footer/div/button")
    button3.click()
    

finally:
    time.sleep(10)
    browser.quit()