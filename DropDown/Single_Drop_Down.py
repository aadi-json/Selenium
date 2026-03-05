from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///home/aadi/Downloads/demo%20(1).html")
single=driver.find_element(By.ID,"standard_cars")
sel=Select(single)
sel.select_by_visible_text("Ford")
time.sleep(2)
sel.select_by_value("lr")
time.sleep(2)
sel.select_by_index(2)
time.sleep(1)
sel.deselect_all() #raise NotImplementedError("You may only deselect all options of a multi-select")
                   #NotImplementedError: You may only deselect all options of a multi-select
