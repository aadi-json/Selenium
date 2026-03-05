from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
action=ActionChains(driver)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.CLASS_NAME,"btn.btn-danger").click()
# action.key_down(Keys.ENTER).perform()
# alert=Alert(driver)
# alert.accept()
alt=driver.switch_to.alert
alt.accept()