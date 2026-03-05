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
ParentHandle=driver.current_window_handle
print(ParentHandle)
driver.get("https://demoapps.qspiders.com/ui/browser?sublist=0")
sleep(3)
driver.find_element(By.XPATH,"(//div[@class='p-4']/button)[1]").click()
sleep(2)
ChildHandle=driver.window_handles
print(ChildHandle)
driver.switch_to.window(ChildHandle[1])
sleep(2)
driver.find_element(By.TAG_NAME,"button").click()
sleep(2)
count=driver.find_element(By.TAG_NAME,"article").text
print(count,type(count))
if count=="1":
    print("Product added successfully")
else:
    raise Exception("Product is not added")