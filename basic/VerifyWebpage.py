"verifying by url"

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(1)
actual_url=driver.current_url
print(actual_url)

if driver.current_url==actual_url:
    print("i am in my targated page")
    driver.find_element(By.CLASS_NAME,"ico-register").click()
else:
    print("i am not in my targated page")

driver.close()


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

"Verifying by title"
# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)
# driver=webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://demowebshop.tricentis.com/")
# sleep(1)
# actual_title=driver.title
# print(actual_title)

# if driver.title==actual_title:
#     print("I am in my targated page")
#     driver.find_element(By.CLASS_NAME,"ico-register").click()
# else:
#     driver.close()
#     raise Exception(" I am not in my targated element")

# driver.close()

"Verifying by webelement"


options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
# try:
#     poll=driver.find_element(By.XPATH,"//strong[text()='Community poll']")
#     driver.find_element(By.ID,"pollanswers-1").click()
#     print("I am  in my targated page")
# except Exception:
#     raise Exception("I am not in my targated page")




# poll=driver.find_elements(By.XPATH,"//strong[text()='Community poll']")
# if len(poll)>0:
#     print("i am in the targated ele")
# else:
#     raise Exception("I am not in my targated element")

# expected_url = "https://demowebshop.tricentis.com/news/rss/1"
# links = driver.find_elements(By.XPATH, "//div[@class='footer']/div/div[4]/ul/li/a")
# for lin in links:
#     curr_url = driver.current_url
#     if expected_url == curr_url:
#         driver.back()
#         sleep(1)
#     lin.click()
#     sleep(1)
    

    



