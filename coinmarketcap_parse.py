from bs4 import BeautifulSoup
import urllib.request
import pandas
import os
print("lil buddy")

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

file_name = "html_files/testing20210923145124.html"
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
		print(currency_columns[2].find("p").text)    
		print(currency_columns[2].find("p",{"class":"coin-item-symbol"}).text)
		print(currency_columns[6].find("p").,find("span",{class:""}).text)
		print(currency_columns[3].find("a").text)   
		print(currency_columns[2].find("a")["href"]

df.to_csv("parsed_files/coinmarketcap_dataset.csv")

