from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def test_AssignLeave():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    btn=driver.find_element(By.CLASS_NAME,"oxd-icon-button.orangehrm-quick-launch-icon")
    if btn.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_LeaveList():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    Leave=driver.find_element(By.XPATH,"//button[@title='Leave List']")
    if Leave.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_TimeSheet():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    sheet=driver.find_element(By.XPATH,"//button[@title='Timesheets']")
    if sheet.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_ApplyLeave():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    apply=driver.find_element(By.XPATH,"//button[@title='Apply Leave']")
    if apply.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_MyLeave():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    MyLeave=driver.find_element(By.XPATH,"//button[@title='My Leave']")
    if MyLeave.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()

def test_MyTimesheet():
    driver = webdriver.Chrome()
    options=webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver=webdriver.Chrome(options=options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
    driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
    driver.find_element(By.TAG_NAME,"button").click()
    MyTimesheet=driver.find_element(By.XPATH,"//button[@title='My Timesheet']")
    if MyTimesheet.is_enabled():
        print("there is a no defect")
    else:
        raise Exception("Defect is Assign Leave")
    driver.find_element(By.CLASS_NAME,"oxd-userdropdown-name").click()
    driver.find_element(By.LINK_TEXT,"Logout").click()