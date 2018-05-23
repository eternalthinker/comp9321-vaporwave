from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database import *
from datasets import IMDB

engine = create_engine('sqlite:///imdb.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

from datasets import IMDB

titles = IMDB().title_basics()
episodes = IMDB().episodes()
ratings = IMDB().ratings()

parentTconst = 'tt0944947'
all_episodes = episodes.loc[episodes['parentTconst']==parentTconst]
all_episodes = all_episodes['tconst'].tolist()

for ep in all_episodes:

    title = titles.loc[titles['tconst']==ep].to_dict('records')[0]
    episode = episodes.loc[episodes['tconst']==ep].to_dict('records')[0]
    rating = ratings.loc[ratings['tconst']==ep].to_dict('records')

    if rating:
      rating = rating[0]
      averageRating = rating['averageRating']
      numVotes = rating['numVotes']
    else:
        averageRating = 0
        numVotes = 0

    seasonNumber = episode['seasonNumber']
    episodeNumber = episode['episodeNumber']

    seasonNumber = seasonNumber if len(seasonNumber) == 2 else '0' + seasonNumber
    episodeNumber = episodeNumber if len(episodeNumber) == 2 else '0' + episodeNumber


    EID = seasonNumber + episodeNumber

    eps = Episodes(EID=EID,
                   tconst=ep,
                   seasonNumber=seasonNumber,
                   episodeNumber=episodeNumber,
                   title=title['originalTitle'],
                   averageRating=averageRating,
                   numVotes=numVotes,
                   duration=title['runtimeMinutes']
                   )

    session.add(eps)
    session.commit()

session.close()