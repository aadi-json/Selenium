from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import random

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
source=driver.find_element(By.ID,"node")
driver.get("https://demo.automationtesting.in/Static.html")
action=ActionChains(driver)
action.scroll_to_element(source).perform()