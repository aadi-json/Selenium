from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=opt)
actions = ActionChains(driver)
driver.maximize_window()
expected_1="https://demoapps.qspiders.com/ui/browser/product/2"
expected_2="https://demoapps.qspiders.com/ui/browser/product/1"
ParentHandle=driver.current_window_handle
print(ParentHandle)
driver.get("https://demoapps.qspiders.com/ui/browser/newTab?sublist=1")
sleep(1)
driver.find_element(By.XPATH,"(//button[text()='view more'])[1]").click()
sleep(1)
driver.find_element(By.XPATH,"(//button[text()='view more'])[2]").click()
ChildHandle=driver.window_handles
print(ChildHandle)
for child in ChildHandle:
    driver.switch_to.window(child)
    actual=driver.current_url
    if actual==expected_1:
        sleep(1)
        driver.find_element(By.TAG_NAME,"button").click()
    elif actual==expected_2:
        driver.find_element(By.TAG_NAME,"button").click()
    sleep(2)
        
