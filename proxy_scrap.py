#Extracting the data from SSL Proxies to store the proxy address in CSV file.We have used Beautiful soup for scraping the data and pandas to store the data in CSV files.
from bs4 import BeautifulSoup
import requests
import pandas as pd
import notify2
def crawl_proxies():
	proxies=[]
	link = "https://www.sslproxies.org/"

	r = requests.get(link)
	s = BeautifulSoup(r.text,"html.parser")
	for i in s.find_all("tr")[:30]:
		try:
			data = i.find_all("td")
			address = data[0].text
			port = data[1].text
			proxy = address + ":" + port
			proxies.append(proxy)
		except:
			pass

	return proxies

proxies = crawl_proxies()
df = pd.DataFrame({'Proxy address':proxies})
df.to_csv('proxy_address.csv', index=False,encoding='utf-8')
notify2.init('Proxy Scrapping Done!')
n = notify2.Notification('Proxy Scrapping Done!', 'The CSV file is stored in your system at path /Home/Desktop/scrapprojects named as proxy_address.csv')
n.set_timeout(15000)
n.show()


