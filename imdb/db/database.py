from sqlalchemy import create_engine, Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import sys



Base = declarative_base()

class Episodes(Base):
    __tablename__ = 'episodes'
    EID = Column(String, primary_key=True)
    tconst = Column(String)
    seasonNumber = Column(String)
    episodeNumber = Column(String)
    title = Column(String)
    averageRating = Column(Numeric)
    numVotes = Column(Integer)
    duration = Column(Integer)

    def __repr__(self):
        return {'EID': self.EID, 'tconst': self.tconst,
                'seasonNumber': self.seasonNumber,
                'episodeNumber': self.episodeNumber, 'title': self.title,
                'averageRating': self.averageRating, 'numVotes': self.numVotes,
                'duration': self.duration}


class EpisodeCharacters(Base):
    __tablename__ = 'episode_characters'
    EID = Column(String, ForeignKey('episodes.EID'), primary_key=True)
    CID = Column(String, ForeignKey('characters.CID'), primary_key=True)

    def __repr__(self):
        return {'EID': self.EID, 'CID': self.CID}


class Characters(Base):
    __tablename__ = 'characters'
    CID = Column(String, primary_key=True)
    name = Column(String)
    url = Column(String)
    actor = Column(String)
    episode_of_death = Column(String)
    means_of_death = Column(String)
    role = Column(String)
    killed_by = Column(String)

    def __repr__(self):
        return {'CID': self.CID, 'name': self.name, 'url': self.url,
                'actor': self.actor, 'episode_of_death ':self.episode_of_death, 
                'means_of_death': self.means_of_death, 'role': role,
                'killed_by': self.killed_by}


class Quotes(Base):
    __tablename__ = 'quotes'
    QID = Column(String, primary_key=True)
    EID = Column(String, ForeignKey('episodes.EID'))
    quote_text = Column(String)

    def __repr__(self):
        return {'QID': self.QID, 'EID': self.EID, 'quote_text': self.quote_text}


class CharacterQuotes(Base):
    __tablename__ = 'character_quotes'
    CID = Column(String, ForeignKey('characters.CID'), primary_key=True)
    QID = Column(String, ForeignKey('quotes.QID'), primary_key=True)

    def __repr__(self):
        return {'CID': self.CID, 'QID': self.QID}


if __name__ == '__main__':

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

        print(rating)

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