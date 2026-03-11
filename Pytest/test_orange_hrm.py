from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By

def test_AssignLeave():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(2)
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    sleep(6)
    btn=driver.find_element(By.XPATH,"//button[@title='Assign Leave']")
    if btn.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-img").click()
    driver.find_element(By.LINK_TEXT,"Logoutcd").click()

    


