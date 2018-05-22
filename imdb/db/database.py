from sqlalchemy import create_engine, Column, Integer, String, Real
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Episodes(Base):
    __tablename__ = 'episodes'
    EID = Column(String, primary_key=True)
    tconst = Column(String)
    seasonNumber = Column(String)
    episodeNumber = Column(String)
    title = Column(String)
    averageRating = Column(Real)
    numVotes = Column(Integer)
    duration = Column(Integer)

    def __repr__(self):
        return {'EID': self.EID, 'tconst': self.tconst,
                'seasonNumber': self.seasonNumber,
                'episodeNumber': self.episodeNumber, 'title': self.title,
                'averageRating': self.averageRating, 'numVotes': self.numVotes,
                'duration', self.duration}


class EpisodeCharacters(Base):
    __tablename__ = 'episode_characters'
    EID = Column(String, ForeignKey('episodes.EID'), nullable=False)
    CID = Column(String, ForeignKey('characters.CID'), nullable=False)

    def __repr__(self):
        return {'EID': self.EID, 'CID': self.CID}


class Characters(Base):
    __tablename__ 'characters'
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
    CID = Column(String, ForeignKey('characters.CID'))
    QID = Column(String, ForeignKey('quotes.QID'))

    def __repr__(self):
        return {'CID': self.CID, 'QID': self.QID}