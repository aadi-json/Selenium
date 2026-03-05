from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.oracle.com/in/java/technologies/downloads/")
sleep(2)
lockSym=driver.find_element(By.LINK_TEXT,"jdk-17.0.18_linux-x64_bin.rpm")
driver.execute_script("arguments[0].scrollIntoView(false);",lockSym)
lockSym.click()
wait=WebDriverWait(driver,30)
diasbledEle=wait.until(Ec.presence_of_element_located((By.LINK_TEXT,"Download jdk-17.0.18_linux-x64_bin.rpm")))
driver.execute_script("arguments[0].click();",diasbledEle)