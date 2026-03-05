from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
actions = ActionChains(driver)
driver.maximize_window()

driver.get("https://demowebshop.tricentis.com/")

for i in range(2):
            actions.key_down(Keys.TAB).perform()
            sleep(1)
actions.key_down(Keys.ENTER).perform()

for i in range(25):
    actions.key_down(Keys.TAB).perform()
    sleep(0.3)
actions.key_down(Keys.SPACE).perform()
actions.key_down(Keys.TAB).send_keys("aadi").perform()
actions.key_down(Keys.TAB).send_keys("gawande").perform()
actions.key_down(Keys.TAB).send_keys("aadi@gmail.com").perform()
actions.key_down(Keys.TAB).send_keys("xyz@111").perform()
actions.key_down(Keys.TAB).send_keys("hhh@123").perform()
actions.key_down(Keys.ENTER).perform()
sleep(3)
driver.quit()