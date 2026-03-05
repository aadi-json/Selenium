from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
pass_data="Mobile"
ele=driver.find_element(By.ID,"small-searchterms")
present_data=driver.find_element(By.ID,"small-searchterms").get_attribute("value")
ele.send_keys(pass_data)
present_data=driver.find_element(By.ID,"small-searchterms").get_attribute("value")
if present_data==pass_data:
    print("Yes")