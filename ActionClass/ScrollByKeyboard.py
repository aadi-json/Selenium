from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(3)
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
action.key_down(Keys.PAGE_UP)