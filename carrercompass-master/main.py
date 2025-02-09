from pygame.examples.video import driver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

for _ in range(4):
    findmore = driver.find_element(By.XPATH, '// *[ @ id = "left-column"] / div[2] / div / div / button')
    findmore.send_keys(Keys.ENTER)
    time.sleep(4)

wait = WebDriverWait(driver, 10)
tot_jobs = driver.find_element(By.XPATH,'//*[@id="left-column"]/div[1]/span/div/h1').text

job_list = []
all_jobs = driver.find_elements(By.CLASS_NAME,'JobCard_jobCardContainer__arQlW')
time.sleep(5)

for job in all_jobs:
    try:
        job.click()
        time.sleep(1)
        company_name = job.find_element(By.CLASS_NAME, 'EmployerProfile_compactEmployerName__9MGcV').text
        try:
            salary_estimate = job.find_element(By.CLASS_NAME, 'JobCard_salaryEstimate__QpbTW').text
        except Exception:
            salary_estimate = "N/A"
        try:
            rating = job.find_element(By.CLASS_NAME, 'rating-single-star_RatingText__XENmU').text
        except Exception:
            rating = "N/A"  # Assign "N/A" if rating is missing
        role_name = job.find_element(By.CLASS_NAME, 'JobCard_jobTitle__GLyJ1').text

        try:
            recommend_percent = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'JobDetails_employerStatsDonuts__uWTLY'))
            ).text
        except Exception:
            recommend_percent = "N/A"
        try:
            pros_text = job.find_element(By.XPATH, '//*[@id="app-navigation"]/div[4]/div[2]/div[2]/div/div[1]/section/section[5]/div/div[1]/ul').text
        except:
            pros_text = "No Pros Available"

        try:
            cons_text = job.find_element(By.XPATH, '//*[@id="app-navigation"]/div[4]/div[2]/div[2]/div/div[1]/section/section[5]/div/div[2]/ul').text
        except:
            cons_text = "No Cons Available"
        print(company_name, role_name, rating, salary_estimate)
        print("\n")
        print(recommend_percent)
        print("\n")
        print(pros_text)
        print("\n")
        print(cons_text)
        job_list.append({
            'Company': company_name,
            'Rating': rating,
            'Role_name': role_name,
            'Salary_Estimate': salary_estimate,
            'Pros': pros_text,
            'Cons': cons_text,
            'Recommend %': recommend_percent
        })
    except Exception as e:
        print(f"Error fetching details for a job card: ")

print("\n")
print(tot_jobs)
print(job_list)
df=pd.DataFrame(job_list)
df.to_csv("glassdors_jobs.csv",index=False,encoding='utf-8')
print("Data Saved to glassdoors_jobs.csv successfully")














