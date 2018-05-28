from bs4 import BeautifulSoup
import requests, re, lxml
from pathlib import Path
import time, sys
from random import randint
import urllib

cast_url = "https://www.hbo.com/game-of-thrones/cast-and-crew"

def scrape_images():

	# Avoid re-scraping 
	my_file = Path("./game-of-thrones-cast-and-crew.html")
	if my_file.is_file():
		html_file = open("game-of-thrones-cast-and-crew.html", 'r')
		soup = BeautifulSoup(html_file, "lxml")
		html_file.close()
	else:
		r  = requests.get(cast_url)
		data = r.text
		html_file = open("game-of-thrones-cast-and-crew.html", "w")
		html_file.write(data)
		soup = BeautifulSoup(data, "lxml")
		html_file.close()


	# Iterate through character listicle items and scrape attributes
	i=0
	for listicle_item in soup.find_all("div", class_="modules/Cast--castMember"):

		print(str(i))
		i=i+1

		img = listicle_item.find("img", src=True)
		link = "https://www.hbo.com" + img['src']

		print(link)

		r  = requests.get(link)
		time.sleep(randint(1, 2))

		# # The main character name is in a div with class "headline"
		# # the first and only item ([0])
		# name = listicle_item.find("div", class_="headline").contents[0].strip()

		# # All other character details are in paragraphs
		# details = listicle_item.find_all("p")
		
		# # Role
		# role = details[0].contents[1].strip()

		# # Season and episode of death
		# time_of_death = str(details[1].contents)
		# match = re.search(r'Season ([0-9]*)', time_of_death)
		# season_of_death = int(match.group(1))
		# match = re.search(r'Episode ([0-9]*)', time_of_death)
		# episode_of_death = int(match.group(1))

		# # Means of death
		# means_of_death = details[2].contents[1].strip()


# if __name__ == "__main__":
# 	print(scrape_characters('tt1480055'))



			






