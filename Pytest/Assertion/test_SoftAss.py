import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from pytest_check import check

def test_soft():
    expected_url="https://demowebshop.triceom/"
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    options.add_argument("--incognito")
    driver=webdriver.ChromeOptions
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://demowebshop.tricentis.com/")
    actual_url=driver.current_url
    assert actual_url==expected_url
    print("I am in my targated page")
    driver.close()
