import sqlite3

db = sqlite3.connect('project.db')
cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS movies")
cursor.execute("DROP TABLE IF EXISTS directors")

sql_query = """
    CREATE TABLE IF NOT EXISTS directors 
    (director_id INTEGER PRIMARY KEY, last_name TEXT, first_name TEXT)
    """
cursor.execute(sql_query)
sql_query = """
    CREATE TABLE IF NOT EXISTS movies 
    (movie_id INTEGER PRIMARY KEY, title TEXT, year_released INT, director INT,
    FOREIGN KEY (director) REFERENCES directors(director_id))
    """
cursor.execute(sql_query)

insert_movie = f"INSERT INTO movies (title, year_released, director) VALUES (?, ?, ?)"
insert_director = f"INSERT INTO directors (last_name, first_name) VALUES (?, ?)"

movies = {
    'Iron Man': [2008, 'Jon Favreau'], 
    'Captain America: The First Avenger': [2011, 'Joe Johnston'], 
    "The Avengers" : [2012, 'Joss Whedon'],
    'Guardians of the Galaxy': [2014, 'James Gunn'], 
    'Black Panther': [2018, 'Ryan Coogler'], 
    'Spider-Man: Homecoming': [2017, 'Jon Watts'], 
    'Black Widow': [2021, 'Cate Shortland'],
    'The Princess Bride': [1987, 'Rob Reiner']
}

for (title, data) in movies.items():
    cursor.execute(insert_movie, (title, data[0], data[1]))

for director_data in movies.values():
    names = director_data[1].split()
    cursor.execute(insert_director, (names[1], names[0]))
db.commit()
db.close()