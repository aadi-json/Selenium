from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///home/aadi/Downloads/demo%20(1).html")

#single dropdown

# sigleDropDown=driver.find_element(By.ID,"standard_cars")
# sel=Select(sigleDropDown)
# sleep(2)
# sel.select_by_visible_text("Audi")
# sleep(2)
# sel.select_by_index(4)
# sleep(2)
# sel.select_by_value("vol")
# sleep(1)

# print(sel.is_multiple())

# opt=sel.options
# for i in range(len(opt)):
#     sel.select_by_index(i)
#     sleep(1)



#multiple dropdown

# multiDropDown=driver.find_element(By.ID,"multiple_cars")
# sel=Select(multiDropDown)
# sel.select_by_index(1)
# sleep(1)
# sel.select_by_visible_text("Ford")
# sleep(1)
# sel.select_by_value("vol")
# sleep(1)
# print(sel.is_multiple)
# sleep(1)
# sel.deselect_all()
# sleep(1)

# options=sel.options

# for i in range(len(options)):
#     sel.select_by_index(i)
#     sleep(1)

# print(sel.first_selected_option)
# print(sel.all_selected_options)

# sel.deselect_all()


