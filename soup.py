from bs4 import BeautifulSoup
import requests
import lxml

r  = requests.get("http://time.com/3924852/every-game-of-thrones-death/")
data = r.text
soup = BeautifulSoup(data, "lxml")	

#Iterate through character listicle items
for listicle_item in soup.find_all("div", class_="listicle-item"):

	#The main character name is in a div with class "headline", the first and only item ([0])
	name = listicle_item.find("div", class_="headline").contents[0].strip()
	print("Name:" + name);

	

