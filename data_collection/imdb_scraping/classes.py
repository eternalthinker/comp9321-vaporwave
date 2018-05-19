# Simple data structures to store characters and quotes
# Script can just put the info into these data structures, and we can iterate through them for db later
# Perhaps it would be more useful to make an "Episode" class, this can be done....
all_characters = []
all_quotes = []
all_episodes = []

#create character id from slug


class Episode:
	def __init__(self, name, id):
		self.episode_name = name
		self.episode_id = id


# Character class
class Character:
	def __init__(self, name, url=""):
		self.name = name
		self.quotes = []		# List of Quote objects for every quote the character says (or is part of, in conversation)
		self.url = url			# The imdb URL could be scraped for each character, if this is useful
		self.episodes = []
		self.played_by = ""

	def add_quote(self, quote):
		self.quotes.append(quote)

	def add_episode(self, episode_id):
		if not episode_id in self.episodes:
			self.episodes.append(episode_id)

	def set_played_by(self, actor_name):
		self.played_by = actor_name


def get_character_by_name(name):
	for char in all_characters:
		if char.name == name:
			return char
	return 0


# Quote class
class Quote:
	def __init__(self, quote_text, characters, quote_episode):
		self.quote_text = quote_text
		self.quote_episode = quote_episode	# quote_episode is the episode id, e.g. tt3658014
		self.length = 0						# this attribute could be computed if some quotes too long to display
		self.characters = characters        # list of character NAMES involved in the quote (quotes can be conversations) (not Character objects)