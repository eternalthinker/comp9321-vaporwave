import numpy as np 
import pandas as pd 
from os import path


class KAGGLE:

    def __init__(self, dir='data/kaggle/'):
        self.dir = dir

    def battles(self):
        """
        Parameters:

        Returns:
        :name:
        :year:
        :battle_number:
        :attacker_king:
        :defender_king:
        :attacker_1:
        :attacker_2:
        :attacker_3:
        :attacker_4:
        :defender_1:
        :defender_2:
        :defender_3:
        :defender_4:
        :attacker_outcome:
        :battle_type:
        :major_death:
        :major_capture:
        :major_capture:
        :attacker_size:
        :defender_size:
        :attacker_commander:
        :defender_commander:
        :summer:
        :location:
        :region:
        :note:
        """
        return pd.read_csv(self.dir + 'battles.csv', sep=',', header=0)

    def deaths(self):
        """
        Parameters:

        Returns:
        :Name:
        :Allegiances:
        :Death Year:
        :Book of Death:
        :Death Chapter:
        :Book Intro Chapter:
        :Gender:
        :Nobility:
        :GoT:
        :CoK:
        :SoS:
        :FfC:
        :DwD:
        """
        return pd.read_csv(self.dir + 'character-deaths.csv', sep=',', header=0)
    
    def predictions(self):
        """
        Parameters:

        Returns:
        :S.No:
        :actual:
        :pred:
        :alive:
        :plod:
        :name:
        :title:
        :male:
        :culture:
        :dateOfBirth:
        :dateOfDeath:
        :mother:
        :father:
        :heir:
        :house:
        :spouse:
        :book1:
        :book2:
        :book3:
        :book4:
        :book5:
        :isAliveMother:
        :isAliveFather:
        :isAliveHeir:
        :isAliveSpouse:
        :isMarried:
        :isNoble:
        :age:
        :numDeadRelations:
        :boolDeadRelations:
        :isPopular:
        :popularity:
        :isAlive:
        """
        return pd.read_csv(self.dir + 'character-predictions.csv', sep=',', header=0)

class IMDB:

    def __init__(self, dir='data/imdb/', id='tt0944947', title='Game of Thrones'):
        self.dir = dir
        self.id = id
        self.title = title

    def actor_basics(self, nconst):
        """
        Parameters:
        :nconst:            unique identifier

        Returns:
        :nconst:            unique identifier
        :primaryName:       name
        :birhtYear:         in YYYY format
        :deathYear:         in YYYY format
        :primaryProfession: top-3 professions of the person
        :knownForTitles:    titles the person is known for
        """
        df =  pd.read_table(self.dir + 'name.basics.tsv.gz', sep='\t', header=0)
        return df.loc[df['nconst'] == nconst].as_matrix()[0]

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
        df = pd.read_table(self.dir + 'title.akas.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == self.id].as_matrix()[0]

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
        df = pd.read_table(self.dir + 'title.basics.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == self.id].as_matrix()[0]

    def crew(self, episode):
        """
        Parameters:
        :episode:           tconst unique identifier

        Returns:
        :tconst:            unique identifier
        :directors:         array of nconsts
        :writers:           writers of the given titles
        """
        df = pd.read_table(self.dir + 'title.crew.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == episode].as_matrix()[0]

    def episode(self, episode):
        """
        Parameters:
        :episode:           tconst unique identifier

        Returns:
        :tconst:            unique identifer
        :parentTconst:      unique identifier
        :seasonNumber:      season number the episode belongs to
        :episodeNumber      episode number of the tconst in the TV series
        """
        df = pd.read_table(self.dir + 'title.episode.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == episode].as_matrix()[0]

    def principals(self, episode):
        """
        Parameters:
        :episode:           unique identifier

        Returns:
        :tconst:            unique identifier
        :principalCast:     array of nconst
        """
        df = pd.read_table(self.dir + 'title.principals.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == episode]

    def cast(self, episode):
        """
        Parameters:
        :episode:           unique identifier

        Returns:
        :tconst:            unique identifier
        :principalCast:     array of nconst
        """
        df = pd.read_table(self.dir + 'title.principals.tsv.gz', sep='\t', header=0)
        return df.loc[(df['tconst'] == episode) & df['category'].isin(('actor', 'actress'))]

    def ratings(self, episode):
        """
        Parameters:
        :episode:           tconst unique identifier

        Returns:
        :tconst:            unique identifier
        :averageRating:     weighter average of all the individual user ratings
        :numVotes:          number of votes the title has received
        """
        df = pd.read_table(self.dir + 'title.ratings.tsv.gz', sep='\t', header=0)
        return df.loc[df['tconst'] == episode].as_matrix()[0]

    def all_episodes(self):
        """
        Parameters:

        Returns:
        :tconstt:           array of all GOT epidosdes
        """
        df = pd.read_table(self.dir + 'title.episode.tsv.gz', sep='\t', header=0)
        df = df.loc[df['parentTconst'] == self.id]
        return df['tconst'].as_matrix()