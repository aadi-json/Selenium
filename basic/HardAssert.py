from selenium import webdriver
from selenium.webdriver.common.by import By
import time

expected_url="https://demowebshop.tricentis.com/"
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
actual_url=driver.current_url
assert expected_url==actual_url
driver.find_element(By.ID,"pollanswers-1").click()