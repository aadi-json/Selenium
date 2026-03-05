from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///home/aadi/Downloads/demo%20(1).html")
multi=driver.find_element(By.ID,"multiple_cars")
sel=Select(multi)

multi=driver.find_element(By.ID,"standard_cars")
sel=Select(multi)

sel.select_by_visible_text("BMW")
time.sleep(1)
sel.select_by_value("jgr")
time.sleep(1)
sel.select_by_index(3)
time.sleep(1)
sel.deselect_by_value("jgr")
time.sleep(1)
sel.deselect_by_index(3)
time.sleep(1)
sel.deselect_by_visible_text("BMW")
sel.deselect_all()
print(sel.is_multiple) #Trueref=sel.is_multiple
if ref:
    sel.select_by_visible_text("BMW")
    time.sleep(1)
    sel.select_by_value("jgr")
    time.sleep(1)
    sel.select_by_index(3)
    time.sleep(2)
    sel.deselect_all()
  
else:
    print("The dropdown is not multiple")

ref=sel.is_multiple
if ref:
    sel.select_by_visible_text("BMW")
    time.sleep(1)
    sel.select_by_value("jgr")
    time.sleep(1)
    sel.select_by_index(3)
    time.sleep(2)
    sel.deselect_all()
  
else:
    print("The dropdown is not multiple")


options=sel.options
for ele in range(1,len(options)):
    time.sleep(0.3)
    sel.select_by_index(ele)
    time.sleep(0.3)
sel.deselect_all()
driver.close()

cars=sel.options

count=0
for car in cars:
    time.sleep(0.5)
    sel.select_by_index(count)
    count+=1


