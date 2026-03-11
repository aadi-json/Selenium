"""
write a script for dws digital download product 
1.opne the browser
2.maximize the browser
3.click on digital download
4.perform select all actions in remining two dropdown menu 
like display and view as
"""


from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
drop1=driver.find_element(By.ID,"products-pagesize")
sel=Select(drop1)
apple=sel.options
index=0
dropdown_2=driver.find_element(By.ID,"products-viewmode")
drops_2=Select(dropdown_2)
sel=drops_2.options
index1=0
for app in apple:
    drop1=driver.find_element(By.ID,"products-pagesize")
    sel=Select(drop1)
    time.sleep(1)
    sel.select_by_index(index)
    index+=1
    time.sleep(1)
    dropdown_2=driver.find_element(By.ID,"products-viewmode")
    drops_2=Select(dropdown_2)
    time.sleep(1)
    drops_2.select_by_index(index1)
    index1+=1


















