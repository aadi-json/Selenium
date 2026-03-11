from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
action=ActionChains(driver)
driver.get("https://demo.automationtesting.in/Alerts.html")
driver.find_element(By.XPATH,"(//a[@class='analystic'])[3]").click()
driver.find_element(By.XPATH,'//button[@onclick="promptbox()"]').click()
alt=driver.switch_to.alert
sleep(2)
alt.send_keys("Aditya")
sleep(6)
alt.accept()