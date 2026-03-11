"""
write a script for build your cheap computer products
1.opne the browser
2.maximize the browser
3.verify by page by url
4.add the product built your own cheap computer to the shopping cart
5.select high configuration features and change teh quantity to 2 
and add to shopping cart
6.before filling the detail verify this page by using title.
7.after adding the product verify the product is successfully added to shopping cart or not
8.once the veification is done remove the product from the shopping cart or not
9.close the browser
"""
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time
from random import randint

from selenium.webdriver.support.select import Select

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=options)
driver.maximize_window()


driver.get("https://demowebshop.tricentis.com/")

# step1:verifying the page by url:
expected_url="https://demowebshop.tricentis.com/"
actual_url=driver.current_url
print(actual_url)
if expected_url==actual_url:
    print("im in my targeted page")
    driver.find_element(By.XPATH, "(//input[contains(@value,'Add to cart')])[3]").click()
    driver.find_element(By.LINK_TEXT, "Build your own cheap computer").click()

    expected_title = "Demo Web Shop. Build your own cheap computer"
    actual_title = driver.title
    if expected_title == actual_title:
        print("Success!")
        driver.find_element(By.ID, "product_attribute_72_5_18_65").click()
        driver.find_element(By.ID, "product_attribute_72_6_19_91").click()
        driver.find_element(By.ID, "product_attribute_72_3_20_58").click()
        driver.find_element(By.ID, "product_attribute_72_8_30_94").click()
        driver.find_element(By.ID, "addtocart_72_EnteredQuantity").clear()
        driver.find_element(By.ID, "addtocart_72_EnteredQuantity").send_keys("2")
        driver.find_element(By.ID, "add-to-cart-button-72").click()

        driver.find_element(By.LINK_TEXT, "Shopping cart").click()
        driver.find_element(By.CLASS_NAME, "cart-label").click()

        product_name = driver.find_element(By.CLASS_NAME, "product-name").text
        print(product_name)

        if "Build your own cheap computer" in product_name:
            print("Correct product added")
        else:
            print("Wrong product or product not added")

        driver.find_element(By.NAME, "removefromcart").click()
        driver.find_element(By.NAME, "updatecart").click()

    else:
        raise Exception("Wrong product page")
    time.sleep(5)
    driver.quit()
else:
    print("im not in my targeted page")
    time.sleep(5)
    driver.quit()