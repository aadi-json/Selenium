from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint

class AutoLogin:
    email="aditya"+str(randint(0,100))+"@gmail.com"
    password="Aditya@"+str(randint(0,100))
    def create_account(self):
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        driver=webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li[1]/a").click()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div/div/label[1]").click()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[2]/input[1]").send_keys("adity")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[3]/input").send_keys("Gawnaade")
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[2]/div[2]/div[4]/input").send_keys(self.email)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div/input[1]").send_keys(self.password)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[3]/div[2]/div[2]/input[1]").send_keys(self.password)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div[2]/div[4]/input").click()

    def login(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get("https://demowebshop.tricentis.com/")
        driver.find_element(By.XPATH, "/html/body/div[4]/div/div/div[2]/div/ul/li[2]/a").click()
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[2]/input").send_keys(self.email)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[3]/input").send_keys(self.password)
        driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/div/div[2]/div/div[2]/div[2]/form/div[5]/input").click()

Obj=AutoLogin()
Obj.create_account()
Obj.login()
