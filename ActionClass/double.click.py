from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.guru99.com/test/simple_context_menu")
action=ActionChains(driver)
time.sleep(1)
double_click=driver.find_element(By.XPATH,"//button[contains(text(),'Double-Click Me To See Alert')]")
action.double_click(double_click).perform()