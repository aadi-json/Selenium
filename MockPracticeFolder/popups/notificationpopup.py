from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui/browserNot?sublist=0")
driver.find_element(By.ID,"browNotButton").click()