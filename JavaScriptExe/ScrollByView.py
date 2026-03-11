from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

#it is not having fixed position
# driver.execute_script("window.scrollBy(0,1000);")
# sleep(3)
# driver.execute_script("window.scrollBy(0,-10000);")

# have fixed position
# driver.execute_script("window.scrollTo(0,1000);")
# sleep(2)
# driver.execute_script("window.scrollTo(0,-1000)")