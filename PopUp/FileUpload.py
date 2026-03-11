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
driver.get("https://www.ilovepdf.com/word_to_pdf")
sleep(2)
selectFile=driver.find_element(By.XPATH,"//input[@type='file']")
selectFile.send_keys("/home/aadi/Downloads/Hr Round Questions.docx")