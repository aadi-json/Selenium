# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from time import sleep

# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach', True)

# driver = webdriver.Chrome(options=options)
# driver.maximize_window()

# driver.get("https://demoapps.qspiders.com/ui")
# sleep(2)

# driver.find_element(By.XPATH,"//li[text()='Disabled']").click()
# sleep(2)

# name=driver.find_element(By.ID, "name")
# driver.execute_script("arguments[0].value='Aadi';",name)
# sleep(2)

# email=driver.find_element(By.ID, "email")
# driver.execute_script("arguments[0].value='Aadi@gmial.com';",email)
# sleep(2)

# password=driver.find_element(By.ID, "password")
# driver.execute_script("arguments[0].value='Aadi@123';",password)
# sleep(2)

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://demoapps.qspiders.com/ui/dropdown/disabled?sublist=3")
sleep(2)

country=driver.find_element(By.ID,"SelectCountry")
driver.execute_script("arguments[0].value='India';",country)
sleep(2)

state=driver.find_element(By.ID,"slectState")
driver.execute_script("arguments[0].value='Maharashtra';",state)
sleep(2)

city=driver.find_element(By.ID,"citySelect")
driver.execute_script("arguments[0].value='Mumbai';",city)
sleep(2)

select_quantity=driver.find_element(By.ID,"select_quantity")
driver.execute_script("arguments[0].value='2';",select_quantity)
sleep(2)