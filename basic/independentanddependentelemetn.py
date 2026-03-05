from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
# a=driver.find_element(By.XPATH,"//a[contains(text(),'3rd Album')]/../../div[3]/div/span")
# print(a.text)
b=driver.find_element(By.XPATH,"//a[contains(text(),'3rd Album')]/../following-sibling::div[3]/div/span")
print(b.text)
c=driver.find_element(By.XPATH,"//a[contains(text(),'Music 2')]/../../div[3]/div/span")
print(c.text)
d=driver.find_element(By.XPATH,"(//a[contains(text(),'Music 2')])[2]/../../div[3]/div/span")
print(d.text)
