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
target = driver.find_element(By.CSS_SELECTOR, ".context-menu-one.btn.btn-neutral")
time.sleep(1)
action.context_click(target).perform()
time.sleep(1)
copy=driver.find_element(By.XPATH,"(//span[contains(text(),'Copy')])[2]")
time.sleep(1)
action.click(copy).perform()