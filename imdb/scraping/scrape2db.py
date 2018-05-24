import sqlite3
import sys
from sqlite3 import Error

from scrape_deaths import scrape_deaths
from classes import generate_slug
from scrape_characters import scrape_characters


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None


def get_episodes(conn):
	cur = conn.cursor()
	q = '''
		SELECT * FROM episodes;
	'''
	cur.execute(q)
	return cur

def insert_character_death(conn, value):
	''' insert_character_death(conn, ('jon', 'JON SNOW', '01', '10', 'dagger', 'lord')) '''
	cur = conn.cursor()
	q = '''
		INSERT INTO characters
		(CID, name, season_of_death, episode_of_death, means_of_death, role)
		VALUES (?, ?, ?, ?, ?, ?)
	'''
	cur.execute(q, value)
	return cur.lastrowid

def insert_new_character(conn, value):
	cur = conn.cursor()
	q = '''
		INSERT INTO characters
		(CID, name, actor)
		VALUES (?, ?, ?)
	'''
	cur.execute(q, value)
	return cur.lastrowid

def update_character(conn, value):
	cur = conn.cursor()
	q = '''
		UPDATE characters
		SET actor=?
		WHERE CID=?
	'''
	cur.execute(q, value)
	return cur

def db_has_character(conn, value):
	cur = conn.cursor()
	q = '''
		SELECT CID, name from characters
		WHERE CID=?
	'''
	cur.execute(q, value)
	return (cur.fetchone() is not None)

def populate_deaths(conn):
	for death in scrape_deaths():
		value = tuple([generate_slug(death[0])]) + death
		insert_character_death(conn, value)
	print('All deaths inserted in DB')

def main():
	conn = create_connection('imdb.db')
	populate_deaths(conn)
	episodes = get_episodes(conn)
	for episode_info in episodes:
		eid, tconst, season, episode = episode_info[:4]
		print("Processing Season {} Episode {} ...".format(season, episode))
		characters = scrape_characters(tconst)
		for character in characters:
			name, actor = character
			slug = generate_slug(name)
			if db_has_character(conn, (slug,)):
				update_character(conn, (actor, slug))
			else:
				insert_new_character(conn, (slug, name, actor))

	conn.commit()
	conn.close()


if __name__ == "__main__":
	main()