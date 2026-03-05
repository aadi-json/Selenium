from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
a=driver.find_element(By.XPATH,"//span[contains(text(),'1.00')]")
print(a.text)