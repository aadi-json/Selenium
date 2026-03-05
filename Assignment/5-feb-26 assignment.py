# Write a script for dws home page
# click excellent/good/poor/.. in the community pole section
# and while clicking fetch the text of those elements.

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
# text1=driver.find_element(By.XPATH,"//label[contains(text(),'Excellent')]")
# print(text1.text)
# text2=driver.find_element(By.XPATH,"//label[contains(text(),'Good')]")
# print(text2.text)
# text3=driver.find_element(By.XPATH,"//label[contains(text(),'Poor')]")
# print(text3.text)
# text4=driver.find_element(By.XPATH,"//label[contains(text(),'Very bad')]")
# print(text4.text)

# Write a script for dws digital download products Open the browser Maximize the browser
# Enter into dws page And click digital download products After clicking add all the
# products inside the shoppingcart after adding remove all the products from shopping cart

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
# driver.find_element(By.XPATH,"(//a[contains(text(),'Digital downloads')])[1]").click()
# driver.find_element(By.XPATH,"//a[contains(text(),'3rd Album')]/../../div[3]/div[2]/input").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//a[contains(text(),'Music 2')]/../../div[3]/div[2]/input").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"(//a[contains(text(),'Music 2')])[3]/../../div[3]/div[2]/input").click()
# time.sleep(2)
# driver.find_element(By.XPATH,"//span[contains(text(),'Shopping cart')]").click()
# driver.find_element(By.XPATH,"(//span[contains(text(),'Remove:')])[1]/../input").click()
# driver.find_element(By.XPATH,"(//span[contains(text(),'Remove:')])[2]/../input").click()
# driver.find_element(By.XPATH,"(//span[contains(text(),'Remove:')])[3]/../input").click()
# driver.find_element(By.XPATH,"//input[@value='Update shopping cart']").click()

driver.get("https://demoapps.qspiders.com/ui/login1.0?sublist=0&scenario=1")
driver.find_element(By.XPATH,"//input[@placeholder='Username:']").send_keys("aditya")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("aditya")
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.XPATH,"//input[@type='radio']").click()