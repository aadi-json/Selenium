from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=opt)
actions = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.shoppersstack.com/")
wait=WebDriverWait(driver,30)
wait.until(Ec.presence_of_element_located((By.ID,"loginBtn")))
driver.find_element(By.ID,"loginBtn").click()
wait.until(Ec.element_to_be_clickable((By.XPATH,"//span[text()='Create Account']")))
driver.find_element(By.XPATH,"//span[text()='Create Account']").click()
