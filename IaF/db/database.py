from sqlalchemy import create_engine, Column, Integer, String, Real
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Characters(Base):
    __tablename__ 'characters'
    CID = Column(String, primary_key=True)
    name = Column(String)
    gender = Column(String)
    culture = Column(String)
    title = Column(String)
    aliases = Column(String)
    father = Column(String)
    mother = Column(String)
    spouse = Column(String)
    allegiances = Column(String)
    seasons = Column(String)
    actor = Column(String)

    def __repr__(self):
        return {'CID': self.CID, 'name': self.name, 'gender': self.gender,
                'culture': self.culture, 'title': self.title,
                'aliases': self.aliases, 'father': self.father,
                'mother': self.mother, 'spouse': self.spouse,
                'allegiances': self.allegiances, 'seasons', self.seasons,
                'actor':, self.actor}


class Houses(Base):
    __tablename__ = 'houses'
    HID = Column(String, primary_key=True)
    name = Column(String)
    region = Column(String)
    coatOfArms = Column(String)
    words = Column(String)
    titles = Column(String)
    seats = Column(String)
    currentLord = Column(String)
    overlord = Column(String)
    swornMembers = Column(String)

    def __repr__(self):
        return {'HID': self.HID, 'name': self.name, 'region': self.region,
                'coatOfArms': self.coatOfArms, 'words': self.words,
                'titles': self.titles, 'seats': self.seats,
                'currentLord': self.currentLord, 'overlord': self.overlord,
                'swornMembers': self.swornMembers}