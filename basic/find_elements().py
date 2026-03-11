from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
radio_buttons=driver.find_elements(By.NAME,"pollanswers-1")
for button in radio_buttons:
    button.click()

anchor_tags=driver.find_elements(By.XPATH,"//div[@class='header-links']/ul/li")
for link in anchor_tags:
    link.click()
    time.sleep(2)
    driver.back()
    time.sleep(2)



    