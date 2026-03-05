from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
radio=driver.find_element(By.ID,"pollanswers-1")
radio.click()
if radio.is_selected():
    print("It is selected")
else:
    print("It is not selected")