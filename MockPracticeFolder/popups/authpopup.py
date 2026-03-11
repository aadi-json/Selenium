from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")
sleep(3)
driver.get("https://demoapps.qspiders.com/ui/fileUpload?sublist=0")
file=driver.find_element(By.ID,"resume")
file.send_keys("/home/aadi/Desktop/Aditya_Resume Data_Analyst.pdf")