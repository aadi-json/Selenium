#write a script for dws digital download product 
#1.opne the browser
#2.maximize the browser
#3.click on digital download
#4.add all product to shopping cart
#5.remove the product which is having highest price

from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/digital-downloads")
cart_ele=driver.find_elements(By.XPATH,"//div[@class='add-info']/div[2]/input")
for ele in cart_ele:
    ele.click()
    sleep(1)
driver.find_element(By.XPATH,"(//span[@class='cart-label'])[1]").click()
prices=driver.find_elements(By.XPATH,"//span[@class='product-subtotal']")
highest_price=[]
for price in prices:
    list_price=float(price.text)
    highest_price.append(list_price)
max_price=max(highest_price)
max_price_index=highest_price.index(max_price)
remove_elements=driver.find_elements(By.XPATH,"//td[@class='remove-from-cart']/input")
remove_elements[max_price_index].click()
driver.find_element(By.XPATH,"//div[@class='common-buttons']/input[1]").click()

