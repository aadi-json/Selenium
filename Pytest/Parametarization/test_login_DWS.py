import pytest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

@pytest.mark.parametrize("username,password", [
    ("admin01@gmail.com", "admin01"),
    ("admin02@gmail.com", "Admin02")
])
def test_dwslogin(username,password):
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    driver.find_element(By.CLASS_NAME,"ico-login").click()
    driver.find_element(By.ID,"Email").send_keys(username)
    sleep(2)
    driver.find_element(By.ID,"Password").send_keys(password)
    sleep(2)
    driver.find_element(By.XPATH,"//input[@class='button-1 login-button']").click()
