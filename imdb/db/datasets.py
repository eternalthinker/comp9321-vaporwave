import numpy as np 
import pandas as pd 
from os import path
import requests
import json


class IMDB:

    def __init__(self):
        self.data_dir = '../data/imdb/'
        self.uri = 'https://datasets.imdbws.com/'

    def get_file(self, file):
        file_path = self.data_dir + file
        if not path.exists(file_path):
            r = requests.request('get', self.uri + file, allow_redirects=True)
            open(file_path, 'wb').write(r.content)
        return pd.read_table(self.data_dir + file, sep='\t', header=0)

    def actor_basics(self):
        """
        Parameters:

        Returns:
        :nconst:            unique identifier
        :primaryName:       name
        :birhtYear:         in YYYY format
        :deathYear:         in YYYY format
        :primaryProfession: top-3 professions of the person
        :knownForTitles:    titles the person is known for
        """
        file = 'name.basics.tsv.gz'
        return self.get_file(file)

    def title_akas(self):
        """
        Parmaters:

        Returns:
        :tconst:            unique identifier
        :ordering:          # to uniquely identify rows for a given tconst
        :title:             the localized title
        :region:            the region for this version of the title
        :language:          the language of the title
        :types:             {alternative, dvd, festival, tv, video, working, original, imdbDisplay}
        :attributes:        additional terms
        :isOriginalTitle:   boolean {0 not original, 1 original}
        """
        file = 'title.akas.tsv.gz'
        return self.get_file(file)

    def title_basics(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifier
        :titleType:         {move, short, tvseries, tvepisode, video}
        :primaryTitle:      the more popular title 
        :originalTitle:     original title in original language
        :isAdult:           boolean {0 not adult, 1 adult}
        :startYear:         YYYY release
        :endYear:           YYYY TV series end year
        :runtimeMinutes:    primary runtime of the title in minutes
        :genres:            top-3 genres associated with the tile
        """
        file = 'title.basics.tsv.gz'
        return self.get_file(file)

    def crews(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifier
        :directors:         array of nconsts
        :writers:           writers of the given titles
        """
        file = 'title.crew.tsv.gz'
        return self.get_file(file)

    def episodes(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifer
        :parentTconst:      unique identifier
        :seasonNumber:      season number the episode belongs to
        :episodeNumber:     episode number of the tconst in the TV series
        """
        file = 'title.episode.tsv.gz'
        return self.get_file(file)

    def principals(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifier
        :principalCast:     array of nconst
        """
        file = 'title.principals.tsv.gz'
        return self.get_file(file)

    def casts(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifier
        :principalCast:     array of nconst
        """
        file = 'title.principals.tsv.gz'
        return self.get_file(file)

    def ratings(self):
        """
        Parameters:

        Returns:
        :tconst:            unique identifier
        :averageRating:     weighter average of all the individual user ratings
        :numVotes:          number of votes the title has received
        """
        file = 'title.ratings.tsv.gz'
        return self.get_file(file)

class IceAndFire:

    def __init__(self):
        self.data_dir = '../data/iceandfire/'

    def get_file(self, file, uri):
        file_path = self.data_dir + file
        if not path.exists(file_path):
            r = requests.request('get', uri)
            with open(file_path, 'w') as out:
                json.dump(r.json(), out)
        return pd.read_json(self.data_dir + file)

    def houses(self):
        """
        Parameters:

        Returns:
        :url:
        :name:
        :region:
        :coatOfArms:
        :words:
        :titles:
        :seats:
        :currentLord:
        :heir:
        :overlord:
        :founded:
        :founder:
        :diedOut:
        :ancestralWeapons:
        :cadetBranches:
        :swornMembers:
        """
        uri = 'https://anapioficeandfire.com/api/houses/'
        file = 'houses.json'
        return self.get_file(file, uri)

    def book(self):
        """
        Parameters:

        Returns:
        :url:
        :name:
        :authors:
        :publisher:
        :country:
        :mediaType:
        :released:
        :characters:        A list of the uri for each character

        """
        file = 'book.json'
        uri = 'https://www.anapioficeandfire.com/api/books/1'
        return self.get_file(file, uri)

    def character(self, name):
        """
        Parameter:
        :CID:           String              

        Returns:
        :url:           String              The hypermedia URL of this resource
        :name:          String              The name of this character
        :gender:        String              The gender of this character
        :culture:       String              The culture that this character belongs to
        :born:          String              Textual representation of when and where this character was born
        :died:          String              Textual representation of when and where this character died
        :titles:        Array of Strings    The titles that this character goes by
        :alaiases:      Array of Strings    The aliases that this character goes by
        :father:        String              The character resource URL of this character's father
        :mother:        String              The character resource URL of this character's mother
        :spouse:        String              An array of character resource URLs that has had a POV-chapter in this book
        :allegiances:   Array of Strings    An array of House resource URLs that this character is loyal to
        :books:         Array of Strings    An array of Book resource URLs that this character has been in
        :povBooks:      Array of Strings    An array of Book resource URLs that this character has had a a POV-chapter in
        :tvSeries:      Array of Strings    An array of names of the seasons of Game of Thrones that this character has been in
        :playedBy:      Array of Strings    An array of actor names that has played this character in the TV show Game of Thrones
        """
        file = string(name) + '.json'
        uri = 'https://www.anapioficeandfire.com/api/characters/?name=<name>'
        return self.get_file(file, uri)


if __name__ == '__main__':
    imdb = IMDB()
    imdb.download('title.ratings.tsv.gz')