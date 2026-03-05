from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
sleep(3)
action=ActionChains(driver)
# field=driver.find_element(By.ID,"small-searchterms")
# sleep(2)
# action.send_keys_to_element(field,"Laptop").perform()
for i in range(0,6):
    sleep(1)
    action.key_down(Keys.TAB)
    sleep(1)
action.send_keys("laptop").perform()
