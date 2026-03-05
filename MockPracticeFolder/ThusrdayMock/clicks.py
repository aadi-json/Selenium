from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
action = ActionChains(driver)
driver.get("https://demo.guru99.com/test/simple_context_menu")
right_button = driver.find_element(By.XPATH, "//span[text()='right click me']")
action.context_click(right_button).perform()
time.sleep(2)
action.click(right_button).perform()
time.sleep(3)
double_click=driver.find_element(By.XPATH,"//button[text()='Double-Click Me To See Alert']")
action.double_click(double_click).perform()