# Simple data structures to store characters and quotes
# Script can just put the info into these data structures, and we can iterate through them for db later
all_characters = []
all_quotes = []


# Character class
class Character:
	def __init__(self, name, url=""):
		self.name = name
		self.quotes = []
		self.url = url

	def add_quote(self, quote):
		self.quotes.append(quote)

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
		self.length = 0
		self.characters = characters