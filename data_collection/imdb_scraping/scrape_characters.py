from bs4 import BeautifulSoup
import requests, re, lxml
from pathlib import Path
from classes import *

def scrape_characters(episode_id):

	if episode_id == "test":
		episode_id = "tt5655178"
		html_file = open("test_characters.html", 'r')		# This is tt5655178
		soup = BeautifulSoup(html_file, "lxml")
		html_file.close()
	else: 
		url_string = "https://www.imdb.com/title/" + episode_id + "/fullcredits?ref_=tt_cl_sm#cast"
		r  = requests.get(url_string)
		data = r.text
		soup = BeautifulSoup(data, "lxml")

	# print("\n\n\n\n")

	# Characters are contained in table rows with class "even" or "odd".
	# For the purposes of this, each "sodatext" is a quote, even if it contains a conversation with several characters.
	# If it's a conversation, the "quote" is attributed to each of them.

	# Get episode info
	title_link = soup.find("a", class_="subnav_heading")
	episode_title = title_link.contents[0].strip()
	print("Episode title: " + episode_title)


	for table in soup.find_all("table", class_="cast_list"):
		for char_row in table.find_all("tr"):

			# print(char_row.contents)

			# Get character name
			char_name = ""
			for name_row in char_row.find_all("td", class_="character"):

				# Check if character name is enclosed in a link or not
				char_link = name_row.find("a")
				if char_link:
					char_name = char_link.contents[0].replace('(uncredited)', '').strip()
				else:
					char_name = name_row.contents[0].replace('(uncredited)', '').strip()
				print("Character: " + char_name)

			if char_row.find("span", class_="itemprop"):
				actor_name = char_row.find("span", class_="itemprop").contents[0].strip()
				print("Played by: " + actor_name)

			character = get_character_by_name(char_name)
			if character:
				character.add_episode(episode_id)
				character.set_played_by(actor_name)
			else:
				if char_name != "":
					character = Character(char_name)
					character.add_episode(episode_id)
					character.set_played_by(actor_name)
					all_characters.append(character)





			






