print("hello new puppy")
import urllib.request
import os 
import datetime
import time

for i in range(5):
	current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
	#print(current_time)
	f = open("html_files/testing" + current_time + ".html", "wb" )
	response = urllib.request.urlopen("https://coinmarketcap.com")
	html = response.read()
	f.write(html)
	f.close()
	time.sleep(30)

print("hello little buddy")