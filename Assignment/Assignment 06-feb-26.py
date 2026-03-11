# write a script for ecommers links which is present in footer section
# 1.open the browser
# 2.maximaze the browser
# 3.after maximimizing click facebook, twitter, RSS, youtute and google

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.get("https://demowebshop.tricentis.com/")
socials=driver.find_elements(By.XPATH,"//div[@class='footer-menu-wrapper']/div[4]/ul/li/a")
print(socials)
for social in socials:
    if social==socials[3]:
        driver.back()
    time.sleep(2)
    social.click()
    time.sleep(2)
    

  


# write the script for gift card product 
# 1.open the browser 
# 2.maximize the browser 
# 3.click gift card section
# 4.add 25 doller virtual gift card
# 5.fill all the details of gift card
# 6.and update the product quantity 2 and add the product to the shopping card
# 7.remove the gift card from the shopping card
# 8.at last close the browser

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.ChromeOptions
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
driver.find_element(By.XPATH,"//div[@class='header-menu']/ul/li[7]/a").click()
add_cart=driver.find_elements(By.XPATH,"//div[@class='add-info']/div[2]/input")
for items in add_cart:
    if items==add_cart[3]:
        driver.find_element(By.XPATH,"(//div[@class='add-info'])[4]/div[2]/input").click()
    else:
        items.click()
        time.sleep(2)
        driver.find_element(By.XPATH,"//div[@class='giftcard']/div/input").send_keys("Aditya")
        time.sleep(1)
        driver.find_element(By.XPATH,"(//div[@class='giftcard']/div/input)[2]").send_keys("Aditya123@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH,"(//div[@class='giftcard']/div/input)[3]").send_keys("Aditya")
        time.sleep(1)
        driver.find_element(By.XPATH,"(//div[@class='giftcard']/div/input)[4]").send_keys("Aditya12@gmail.com")
        time.sleep(1)
        driver.find_element(By.XPATH,"//div[@class='giftcard']/div[5]/textarea").send_keys("Aditya")
        time.sleep(2)
        value=driver.find_element(By.XPATH,"//div[@class='add-to-cart-panel']/input")
        value.clear()
        time.sleep(1)
        value.send_keys(2)
        time.sleep(2)
        driver.find_element(By.XPATH,"(//div[@class='add-to-cart-panel']/input)[2]").click()
        time.sleep(2)
        driver.back()
    
