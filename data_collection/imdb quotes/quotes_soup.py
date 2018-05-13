import time, sys
from random import randint
from scrape_page import *

# Usage: python3 quotes_soup.py [episode id]
# Episode id is optional, in case you just want to scrape one ID
# Currently set to just scrape episode_ids_test

episode_ids = ['tt1480055', 'tt1668746', 'tt1829962', 'tt1829963', 
'tt1829964', 'tt1837862', 'tt1837863', 'tt1837864', 'tt1851397', 
'tt1851398', 'tt1971833', 'tt2069318', 'tt2069319', 'tt2070135',
'tt2074658', 'tt2084342', 'tt2085238', 'tt2085239', 'tt2085240', 
'tt2112510', 'tt2178772', 'tt2178782', 'tt2178784', 'tt2178788',
'tt2178796', 'tt2178798', 'tt2178802', 'tt2178806', 'tt2178812',
'tt2178814', 'tt2816136', 'tt2832378', 'tt2972426', 'tt2972428', 
'tt3060782', 'tt3060856', 'tt3060858', 'tt3060860', 'tt3060876',
'tt3060910', 'tt3658012', 'tt3658014', 'tt3846626', 'tt3866826', 
'tt3866836', 'tt3866838', 'tt3866840', 'tt3866842', 'tt3866846', 
'tt3866850', 'tt3866862', 'tt4077554', 'tt4131606', 'tt4283016',
'tt4283028', 'tt4283054', 'tt4283060', 'tt4283074', 'tt4283088', 
'tt4283094', 'tt5654088', 'tt5655178', 'tt5775840', 'tt5775846', 
'tt5775854', 'tt5775864', 'tt5775874', 'tt5924366', 'tt6027908', 
'tt6027912', 'tt6027914', 'tt6027916', 'tt6027920']

episode_ids_test = ['tt1480055', 'tt1668746', 'tt1829962'] 


# First command line argument can be used to pass an episode id. 
# If none exists, assume that we're gathering data for all episodes
if len(sys.argv) < 2:

	for e_id in episode_ids_test:
		scrape_page(e_id)
		time.sleep(randint(1, 3))

	#Testing
	for c in all_characters:
		print(c.name + ": " + str(len(c.quotes)) + " scraped quotes")

else:
	e_id = sys.argv[1]
	if e_id == "test":
		scrape_page("test")
	elif not e_id in episode_ids:
		print("Invalid episode id")
		exit(1)

	scrape_page(e_id)

	#Testing
	for c in all_characters:
		print(c.name + ": " + str(len(c.quotes)) + " scraped quotes")



