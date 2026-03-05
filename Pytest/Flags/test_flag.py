from selenium import webdriver


def test_csk():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.chennaisuperkings.com/")
    print("Thala for a reason")

def test_mumbai():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.mumbaiindians.com/")
    print("Shana for a reason")
    raise Exception("Mi")

def test_rcb():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://www.royalchallengers.com/")
    print("King for a reason")