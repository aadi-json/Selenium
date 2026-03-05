"""
open the browser
maximiaze it
enter in omayo
click on the dropdown button in fotter section
then after clicking 
open flipkart in a different tab
after opening any one of your favourite product
go to omayo page 
refresh the page 
click on the timer enabled button
retrive the text of popup
after retriving hadle the popup by pressing ok button
close all the pages.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=opt)
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://omayo.blogspot.com/")
wait=WebDriverWait(driver,30)
driver.find_element(By.CLASS_NAME,"dropbtn").click()
flipkart_link=driver.find_element(By.LINK_TEXT,"Flipkart")
ActionChains(driver).key_down(Keys.CONTROL).click(flipkart_link).key_up(Keys.CONTROL).perform()
Child=driver.window_handles
driver.switch_to.window(Child[1])
driver.find_element(By.CLASS_NAME,"b3wTlE").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"nw1UBF.v1zwn25").send_keys("Mac book")
sleep(3)
ActionChains(driver).key_down(Keys.ENTER).perform()
driver.switch_to.window(Child[0])
sleep(2)
driver.refresh()
sleep(3)
wait.until(Ec.element_to_be_clickable((By.XPATH,"//input[@value='Button3']")))
driver.find_element(By.XPATH,"//input[@value='Button3']").click()
sleep(2)
alt=driver.switch_to.alert
print(alt.text)
sleep(5)
driver.quit()