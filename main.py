from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


path = "D:/selenium/chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Prevents the browser from closing automatically

s = Service(path)
driver = webdriver.Chrome(service=s, options=chrome_options)
driver.get("https://www.glassdoor.co.in/index.htm")

# Mail Section
time.sleep(10)
box = driver.find_element(By.XPATH, '//*[@id="inlineUserEmail"]')
box.send_keys("sandeep.csedvit@gmail.com")
box.send_keys(Keys.ENTER)

#Password Section
time.sleep(5)
password = driver.find_element(By.XPATH, '//*[@id="inlineUserPassword"]')
password.send_keys("Sandeep@123")
password.send_keys(Keys.ENTER)


#Jobs Section
time.sleep(10)
driver.find_element(By.XPATH,'//*[@id="ContentNav"]/li[2]/a').click()
time.sleep(5)
job = driver.find_element(By.XPATH,'//*[@id="searchBar-jobTitle"]')
job.send_keys("Software Engineer")
location = driver.find_element(By.XPATH,'//*[@id="searchBar-location"]')
location.send_keys("Hyderabad")
location.send_keys(Keys.ENTER)







