from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
# driver.find_element(By.XPATH,"//input[@value='Add to cart']").click()
# driver.find_element(By.XPATH,"//input[@value='Add to cart']").click()
# driver.find_element(By.XPATH,"(//input[@value='Add to cart'])[2]").click()
# apple=driver.find_element(By.XPATH,"//strong[text()='Categories']")
# print(apple.text)
# apple=driver.find_element(By.XPATH,"//strong[text()='Newsletter']")
# print(apple.text)