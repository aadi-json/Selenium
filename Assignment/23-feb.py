"""
write a script for qspider demo app
in that complte js popup
auth popup
file uploadpopup
and notification
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

options.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=options)
driver.maximize_window()


# driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")
# sleep(2)

# driver.get("https://demoapps.qspiders.com/ui/fileUpload?sublist=0")
# sleep(2)
# file=driver.find_element(By.XPATH,"//input[@type='file']")
# sleep(2)
# file.send_keys("/home/aadi/Downloads/Hr Round Questions.docx")

# driver.get("https://demoapps.qspiders.com/ui/browserNot?sublist=0")
# sleep(2)
# driver.find_element(By.ID, "browNotButton").click()
# print("Notification handled successfully")

