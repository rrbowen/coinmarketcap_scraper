from bs4 import BeautifulSoup
import urllib.request
import pandas
import os
import glob
print("lil buddy")

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

for file_name in glob.glob("html_files/*.html"):


scrape_time = os.path.basename(file_name).replace("coinmarketcap")
f = open(file_name, "r" )
# r means reading

#file_content = f.read

soup = BeautifulSoup(f.read(),"html.parser")
f.close()

tbody = soup.find("tbody")
currency_rows = tbody.find_all("tr")


for currency_rows in currency_rows:

	currency_row = currency_rows[0]
	currency_name = currency_columns = currency_row.find_all("td")

	if len(currency_columns)>10:
		currency_name = (currency_columns[2].find("p").text)    
		currency_price = (currency_columns[2].find("a" ,{"class":"coin-item-symbol"}).text)
		currency_symbol = (currency_columns[6].find("p").,find("span",{class:""}).text)
		currency_marketcap = (currency_columns[3].find("a").text) 
		currency_link = currency_columns[2].find("a")["href"]
		currency_image = (currency_columns[2].find("img")[""]

		df = df.append({
			'time': scrape_time
			'name': currency_name,		
			'price': currency_price,
			'symbol': currency_symbol,
			'marketcap': currency_marketcap,
			'image': currency_image

			}, ignore_index = True)


df.to_csv("parsed_files/coinmarketcap_dataset.csv")

