from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()

# driver.get("https://demoapps.qspiders.com/ui/singleElements?sublist=0&scenario=1")
# driver.find_element(By.XPATH,"(//input[@type='button'])[1]").click()
# driver.find_element(By.XPATH,"(//input[@type='button'])[2]").click()

# driver.get("https://demoapps.qspiders.com/ui/login1.0?sublist=0&scenario=1")
#
# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Gauri")
# driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("123456789")
# driver.find_element(By.XPATH,'//input[@name="reg"]').click()
# driver.find_element(By.XPATH,'//input[@name="reg"][2]').click()
#
# driver.find_element(By.XPATH,'//input[@id="sibling1"]').send_keys("Gauri")
# driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("123456789")
# driver.find_element(By.XPATH,'//input[@name="reg"]').click()
# driver.find_element(By.XPATH,'//input[@name="reg"][2]').click()

# driver.find_element(By.XPATH,'//input[@type="text"]').send_keys("Gauri")
# driver.find_element(By.XPATH,'//input[@type="password"]').send_keys("123456789")
# driver.find_element(By.XPATH,'//input[@name="reg"]').click()
# driver.find_element(By.XPATH,'//input[@name="reg"][2]').click()

# driver.get("https://demoapps.qspiders.com/ui/login2.0?sublist=0&scenario=1")
# driver.find_element(By.XPATH,"//input[@placeholder='Username:']").send_keys("gauri")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("gauri")
# driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
# driver.find_element(By.XPATH,"//input[@type='radio']").click()

# driver.get("https://demoapps.qspiders.com/ui/login3.0?sublist=0&scenario=1")
# driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("gauri")
# driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("gauri")
# driver.find_element(By.XPATH,"//button[contains(text(),'Login')]").click()


# driver.get("https://demoapps.qspiders.com/ui/singleElements?sublist=0&scenario=1")
# driver.find_element(By.XPATH,"(//input[@type='button'])[1]").click()
# driver.find_element(By.XPATH,"(//input[@type='button'])[2]").click()

# driver.get("https://demoapps.qspiders.com/ui/duplicate?sublist=0&scenario=1")
# driver.find_element(By.XPATH,"//input[@value='Add to Cart']").click()
# driver.find_element(By.XPATH,"//input[@value='Other Options']").click()
# driver.find_element(By.XPATH,"(//input[@value='Add to Cart'])[2]").click()
# driver.find_element(By.XPATH,"(//input[@value='Add to Cart'])[3]").click()
# driver.find_element(By.XPATH,"(//input[@value='Other Options'])[2]").click()
# driver.find_element(By.XPATH,"(//input[@value='Other Options'])[3]").click()
driver.get("https://demoapps.qspiders.com/ui/duplicate?sublist=0&scenario=1")
time.sleep(2)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()

# driver.find_element(By.XPATH,"//input[@type='checkbox']/../input").click()