#Extracting the data from IMDB to check the movie name,year of release ,ratings and storing it in CSV file.We have used Beautiful soup for scraping the data and pandas to store the data in CSV files.The data have been sorted according to ratings.
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
driver = webdriver.Firefox()
titles=[]
years=[]
ratings=[]
driver.get("https://www.imdb.com/list/ls041612955/")
content = driver.page_source
soup = BeautifulSoup(content) 
for container in soup.findAll('div', attrs={'class':'lister-item-content'}):
	title = container.find('a',href=True)
	year = container.find('span',attrs={'class':'lister-item-year text-muted unbold'})
	rating = container.find('span',attrs={'class':'ipl-rating-star__rating'})

	titles.append(title.text)
	years.append(year.text)
	ratings.append(rating.text)

df = pd.DataFrame({'Movie Name':titles,'Year':years,'Ratings':ratings})
df.to_csv('imdb.csv', index=False,encoding='utf-8')

data = pd.read_csv("imdb.csv")
data.sort_values(["Ratings"],axis=0,ascending=False,inplace=True)
print(data)
