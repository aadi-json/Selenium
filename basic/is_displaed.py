"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
ele=driver.find_element(By.XPATH,"//a[contains(text(),'Electronics')]")
if ele.is_displayed():
    print("Yes its is displaying")
else:
    print("No it is not displaying")
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.shoppersstack.com/signup")
sleep(20)
btn=driver.find_element(By.ID,"Register")
if btn.is_enabled():
    driver.close()
    raise Exception("Defect in signup button")
else:
    print("Yes its is not enabled no defect...")
driver.close()