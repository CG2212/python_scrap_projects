#Extracting the data from Naukri.com to extract the job title,company title,company location,experience required for the job and incentives recieved from the job and storing it in CSV file.We have used Beautiful soup for scraping the data and pandas to store the data in CSV files.
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Firefox()
job_title=[]
company_name=[]
job_location=[]
job_experience=[]
job_package=[]
driver.get("https://www.naukri.com/web-developer-jobs-in-pune?k=web%20developer&l=pune")
content = driver.page_source
soup = BeautifulSoup(content)
for a in soup.findAll('div',attrs={'class':'info fleft'}):
	title_job = a.find('a',attrs={'class':'title fw500 ellipsis'})
	name_co = a.find('a',attrs={'class':'subTitle ellipsis fleft'})
	location = a.find('li',attrs={'class':'fleft grey-text br2 placeHolderLi location'})
	experience = a.find('li',attrs={'class':'fleft grey-text br2 placeHolderLi experience'})
	package = a.find('li',attrs={'class':'fleft grey-text br2 placeHolderLi salary'})
	job_title.append(title_job.text)
	company_name.append(name_co.text)
	job_location.append(location.text)
	job_experience.append(experience.text)
	job_package.append(package.text)
df = pd.DataFrame({'Job Title':job_title,'Company Name':company_name,'Location':job_location,'Experience':job_experience,'Package':job_package})
df.to_csv('job.csv', index=False,encoding='utf-8')
