from os import path
from sqlite3


class dB:

    def __init__(self, database='got.db'):
        self.db = database

    def connect(self):
        """
        Parameters:

        Returns:
        :db connection:
        """
        return sqlite3.connect(self.db)

    def cursor(self):
        """
        Parameters:

        Returns:
        :cursor:            cursor for GOT database
        """
        return self.connect().cursor()

    def query(self, query):
        """
        Parameters:
        :query:             sql statement

        Returns:
        :tuples:            db query output
        """
        return pd.read_sql_query(query, self.connect())

    def insert(self, table, df):
        """
        Parameters:
        :table:
        :df:

        Returns:
        """
        df.to_sql(table, self.connect())