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
driver.get("https://demo.automationtesting.in/Static.html")
action=ActionChains(driver)
time.sleep(1)
source=driver.find_elements(By.XPATH,"//div[@id='dragarea']/div/img")
# index=random.randint(0,2)
# for sou in source:
#     target=driver.find_element(By.ID,"droparea")
#     time.sleep(1)
#     action.drag_and_drop(sou,target).perform()

# container=[0,0,0]
# for sou in range(1,10):
#     index=random.randint(0,2)
#     target=driver.find_element(By.ID,"droparea")
#     time.sleep(0.5)
#     action.drag_and_drop(source[index],target).perform()
#     container[index]+=1
# print(container)