from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.ilovepdf.com/pdf_to_excel")
inp=driver.find_element(By.TAG_NAME,"input")
inp.send_keys("/home/aadi/Desktop/Aditya_Data_Science.pdf")