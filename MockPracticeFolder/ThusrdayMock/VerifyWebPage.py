from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")

#verify by url

# acutal_url=driver.current_url
# if driver.current_url==acutal_url:
#     print("I am on the right page")
# else:
#     raise Exception("Invalid Webpage")

#verify by title

# title=driver.title
# if title==driver.title:
#     print("I am in the right page")
# else:
#     raise Exception("Invalid page")

#verify by webElement

# ele=driver.find_elements(By.CLASS_NAME,"poll-options")
# if len(ele)>0:
#     print("Targated Web page")
# else:
#     raise Exception("Invalid page")