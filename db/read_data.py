import numpy as np 
import datasets


kaggle = datasets.KAGGLE()
imdb = datasets.IMDB()

# print('name basics: ', imdb.name_basics().columns.values)
# print('title akas: ', imdb.title_akas().columns.values)
# print('title basics: ', imdb.title_basics().columns.values)
# print('title crew: ', imdb.title_crew().columns.values)
# print('title episode: ', imdb.title_episoce().columns.values)
# print('title principals: ', imdb.title_principals().columns.values)
# print('title ratings: ', imdb.title_ratings().columns.values)

print('battles: ', kaggle.battles().columns.values)
print('deathes: ', kaggle.deaths().columns.values)
print('predictions: ', kaggle.predictions().columns.values)