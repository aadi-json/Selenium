from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
# elec=driver.find_element(By.XPATH,"//a[contains(text(),'Electronics')]")
# print(elec.get_attribute("href"))
passdata="mobile"
search_field=driver.find_element(By.ID,"Small-searchterms")
present_data=search_field.get_attribute("value")
print(present_data)
search_field.send_keys(passdata)
sleep(2)
present_data=search_field.get_attribute("value")
if present_data==passdata:
    print("data is successfully passed")
else:
    driver.close()
    raise Exception("data is not present with expected one and it is a defect")
