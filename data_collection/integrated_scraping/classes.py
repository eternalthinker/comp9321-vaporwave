
import re

# Simple data structures to store characters and quotes
# Script can just put the info into these data structures, and we can iterate through them for db later
# Perhaps it would be more useful to make an "Episode" class, this can be done....
all_characters = []
all_quotes = []
all_episodes = []

#create character id from slug


# Character class
class Episode:
	def __init__(self, name, id):
		self.episode_name = name
		self.episode_id = id
		self.characters = [] 	# List of character slugs

	def add_character(self, character_name):
		character_slug = generate_slug(character_name)
		if not character_slug in self.characters:
			self.characters.append(character_slug)

# Character class
class Character:
	def __init__(self, name, url=""):
		self.name = self.clean_name(name)
		self.quotes = []		# List of Quote objects for every quote the character says (or is part of, in conversation)
		self.url = url			# The imdb URL could be scraped for each character, if this is useful
		self.episodes = []		# Episodes that the character is in, list of imdb episode ids. 
		self.played_by = ""
		self.slug = generate_slug(name)
		self.season_of_death = 0
		self.episode_of_death = 0
		self.means_of_death = ""
		self.role = ""

	def clean_name(self, name):
		name = re.sub(r'\n', '', name).strip()
		name = name = re.sub(r' +', ' ', name)
		return name	

	def add_quote(self, quote):
		self.quotes.append(quote)

	def add_episode(self, episode_id):
		if not episode_id in self.episodes:
			self.episodes.append(episode_id)

	def set_played_by(self, actor_name):
		self.played_by = actor_name

	def set_season_of_death(self, season_num):
		self.season_of_death = season_num

	def set_episode_of_death(self, episode_num):
		self.episode_of_death = episode_num

	def set_means_of_death(self, means_of_death_string):
		self.means_of_death = means_of_death_string

	def set_role(self, roles_string):
		self.role = roles_string


# Quote class
class Quote:
	def __init__(self, quote_text, characters, quote_episode):
		self.quote_text = quote_text
		self.quote_episode = quote_episode	# quote_episode is the episode id, e.g. tt3658014
		self.length = 0						# this attribute could be computed if some quotes too long to display
		self.characters = characters        # list of character NAMES involved in the quote (quotes can be conversations) (not Character objects)


# General helper functions

# Get character object with either name or slug
# Matches by slug, which should help consolidate characters
def get_character_by_name(name):
	print("looking for " + name)
	slug = generate_slug(name)
	print("looking for slug " + slug)
	for char in all_characters:
		print(char.slug)
		if char.slug == slug:
			return char
	return 0

# Generate slug (character id)
def generate_slug(name):
	name = re.sub(r'\'.*\'', '', name).strip() 				# Remove nicknames, as in Petyr 'Littlefinger' Baelish
	name = re.sub(r'\".*\"', '', name).strip() 				# Remove nicknames, as in Petyr "Littlefinger" Baelish
	name = re.sub(r'\(.*\)', '', name).strip() 				# Remove nicknames, as in Brynden Tully (The Blackfish)
	name = re.sub(r'^The ', '', name)						# Remove titles from slug
	name = re.sub(r'^Ser ', '', name)						# Remove titles from slug
	name = re.sub(r'^Young ', '', name)						# Remove titles from slug
	name = re.sub(r'^Magister ', '', name)					# Remove titles from slug
	name = re.sub(r'^Lady ', '', name)						# Remove titles from slug
	name = re.sub(r'^Black ', '', name)						# Remove titles from slug
	name = re.sub(r'^Lord ', '', name)						# Remove titles from slug
	name = re.sub(r'^King ', '', name)						# Remove titles from slug
	name = re.sub(r'^Khal ', '', name)						# Remove titles from slug
	name = re.sub(r'^Great', '', name).strip()				# Remove titles from slug
	name = re.sub(r'II', '', name)							# Remove titles from slug, e.g. Aerys II Targaryen
	name = re.sub(r' Assassin', '', name)					# Nicknames
	name = re.sub(r' Halfhand', '', name)					# Nicknames
	name = re.sub(r'^Karl$', 'Karl Tanner', name)			# Nicknames
	name = re.sub(r'^Ned$', 'Eddard', name).strip()			# Nicknames
	name = re.sub(r'^Eddard$', 'Eddard Stark', name)		# Nicknames
	name = re.sub(r'^Lancel$', 'Lancel Lannister', name)	# Nicknames
	name = re.sub(r'^Kraznys$', 'Kraznys mo Nakloz', name)	# Nicknames
	name = re.sub(r'^Pyp$', 'Pypar', name)					# Nicknames
	name = re.sub(r'^Lem$', 'Lem Lemoncloak', name)			# Nicknames
	name = re.sub(r'^The Mountain$', 'Gregor Clegane', name)# Nicknames
	name = re.sub(r'Weg Wun Dar', '', name)					# Nicknames
	name = re.sub(r'Robin Arryn', 'Robert Arryn', name)		# Nicknames
	name = re.sub(r'Florel', 'Forel', name)					# typos
	name = re.sub(r'[^a-zA-Z0-9 ]+', '', name).strip()		# Remove random characters, e.g. apostrophe, hash.
	slug = re.sub(r' +', '_', name)							# Replace space with "_"
	slug = slug.lower()										# Ignore case
	return slug

# Get episode by id
def get_episode_by_id(id):
	for e in all_episodes:
		if e.episode_id == id:
			return e
	return 0



