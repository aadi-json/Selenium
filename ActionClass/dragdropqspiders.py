from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import random

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://demoapps.qspiders.com/ui/dragDrop/dragToCorrect?sublist=2")
# time.sleep(2)
# elements = driver.find_elements(By.CLASS_NAME, "draggable")
# destination_1 = driver.find_element(By.XPATH, "(//div[contains(@class,'drop-column')])[1]")
# destination_2 = driver.find_element(By.XPATH, "(//div[contains(@class,'drop-column')])[2]")

# action = ActionChains(driver)
# for ele in elements:
#     text = ele.text
#     if text.startswith("Mobile"):
#         action.click_and_hold(ele).release(destination_1).perform()
#     else:
#         action.click_and_hold(ele).release(destination_2).perform()
#     time.sleep(1)   

driver.get("https://demoapps.qspiders.com/ui/dragDrop/dragToMultiple?sublist=3")
time.sleep(5)
elements = driver.find_elements(By.CLASS_NAME, "draggable-elemment")
# print(elements)
# destination_1 = driver.find_element(By.ID, "dropZone1")
# destination_2 = driver.find_element(By.ID, "dropZone2")
destination=driver.find_elements(By.XPATH,"//div[@class='container-drag']/div/section[2]/div")
action = ActionChains(driver)
# for ele in elements:
#     text = ele.text
#     if text.startswith("Mobile"):
#         ele.click()
# action.click_and_hold(ele).release(destination[0]).perform()
# for ele in elements:
#     text = ele.text
#     if text.startswith("Laptop"):
#         ele.click()
# action.click_and_hold(ele).release(destination[1]).perform()

