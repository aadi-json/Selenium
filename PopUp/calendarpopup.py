from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep, time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime,timedelta
opt = webdriver.ChromeOptions()
opt.add_experimental_option("detach",True)
opt.add_argument("--disable-notifications")

driver = webdriver.Chrome(options=opt)
actions = ActionChains(driver)
driver.maximize_window()
# driver.get("https://demo.automationtesting.in/Datepicker.html")
# sleep(2)
# driver.find_element(By.ID,"datepicker2").send_keys("24/05/2004")
# sleep(2)
# driver.find_element(By.ID,"datepicker1").click()
# driver.find_element(By.XPATH,"(//td[@data-year='2026' and @data-month='1'])[24]/a").click()

driver.get("https://www.easemytrip.com/")
curr_date = datetime.now()
next_date = curr_date + timedelta(days=120)

d_date = curr_date.strftime("%d/%m/%Y")
r_date = next_date.strftime("%d/%m/%Y")
first_loop=int(curr_date.strftime("%m"))
last_loop=int(next_date.strftime("%m"))
print(first_loop,last_loop)
sleep(2)
driver.find_element(By.ID, "ddate").click()
sleep(1)
driver.find_element(By.ID, f"frth_2_{d_date}").click()
sleep(1)
driver.find_element(By.ID, "divRtnCal").click()
sleep(1)
# for i in range(first_loop,last_loop):
#     driver.find_element(By.XPATH,"//img[@id='img2Nex']").click()
#     sleep(1)
# driver.find_element(By.ID, f"frth_3_{r_date}").click()





# print(d_date,r_date,type(d_date),type(r_date))
# print(f"frth_2_{d_date},frth_3_{r_date}")

# sleep(2)
# driver.find_element(By.ID, "ddate").click()
# sleep(1)
# driver.find_element(By.ID, f"frth_2_{d_date}").click()
# sleep(1)
# driver.find_element(By.ID, "divRtnCal").click()
# sleep(1)
# driver.find_element(By.ID, f"frth_3_{r_date}").click()
