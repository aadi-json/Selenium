from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
single=driver.find_element(By.ID,"products-orderby")
sel=Select(single)
ops=sel.options
for op in ops:
    single=driver.find_element(By.ID,"products-orderby")
    sel=Select(single)
    time.sleep(0.5)
    sel.select_by_index(index)
    index+=1
