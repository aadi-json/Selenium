from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.myntra.com/")
Action=ActionChains(driver)
ele=driver.find_element(By.XPATH,"//a[@data-index=4]")
Action.move_to_element(ele).perform()
time.sleep(2)
beauty=driver.find_element(By.XPATH,"//a[@data-reactid=761]")
time.sleep(2)
Action.click(beauty).perform()
