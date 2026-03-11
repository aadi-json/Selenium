from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
actions = ActionChains(driver)
driver.maximize_window()
driver.get("https://www.easemytrip.com/")