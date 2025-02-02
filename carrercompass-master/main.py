from pygame.examples.video import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

path = "C:/Users/kiran/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe"
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
time.sleep(5)

tot_jobs = driver.find_element(By.XPATH,'//*[@id="left-column"]/div[1]/h1').text

job_list = []
all_jobs = driver.find_elements(By.CLASS_NAME,'JobCard_jobCardContainer__arQlW')
time.sleep(5)
for job in all_jobs:
    try:
        company_name = job.find_element(By.CLASS_NAME, 'EmployerProfile_compactEmployerName__9MGcV').text
        try:
            rating = job.find_element(By.CLASS_NAME, 'rating-single-star_RatingText__XENmU').text
        except Exception:
            rating = "N/A"  # Assign "N/A" if rating is missing
        # rating = job.find_element(By.CLASS_NAME, 'rating-single-star_RatingText__XENmU').text
        role_name = job.find_element(By.CLASS_NAME, 'JobCard_jobTitle__GLyJ1').text
        print(company_name, role_name, rating)
        job_list.append({
            'Company': company_name,
            'Rating': rating,
            'Role_name': role_name
        })
    except Exception as e:
        # Handle missing elements or other exceptions
        print(f"Error fetching details for a job card: {e}")

print(job_list)
df=pd.DataFrame(job_list)
print(df)
# file_path = 'C:/Users/kiran/Documents/data.xlsx'
# df.to_excel(file_path,index=False)
# print(f"DataFrame has been saved to {file_path}")
# EmployerProfile_employerNameContainer__ptolz











