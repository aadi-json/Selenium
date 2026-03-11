from selenium import webdriver

def test_m1():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://demowebshop.tricentis.com/")
    print("i am m1")

def test_m2():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://claude.ai/")
    print("i am m2")

def test_m3():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://workdrive.zoho.in/")
    print("i am m3")



