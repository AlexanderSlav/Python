import csv
import os
from subprocess import call
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from credentials import *
from table_classes import *

password = os.getenv("POSTGRES_PASSWORD")
credentials = Credentials('Final_Project',password)
engine_default = create_engine(credentials.DB_CONN_URI_DEFAULT)
db = scoped_session(sessionmaker(bind=engine_default))

def fill_movie_table(file):
    with open(file) as f:
        reader = csv.reader(f)

        for name, year, budget,fees, country, rate, duration, plot_description in reader:
            movie = Movie(name= name,year=year, budget=budget, fees=fees,
                          country=country,rate=rate, duration=duration,
                          plot_description=plot_description)
            db.add(movie)
            print("Added new movie -> {}".format(name))
            db.commit()

def fill_actors_table(file):
    with open(file) as f:
        reader = csv.reader(f)

        for name, birth_date, nationality, gender, age in reader:
            actor = Actor(name= name, birth_date=birth_date, nationality=nationality,
                          gender=gender, age=age)
            db.add(actor)
            print("Added new actor -> {}".format(name))
            db.commit()

def fill_cast_table(file):
    with open(file) as f:
        reader = csv.reader(f)

        for f_id, a_id, role in reader:
            cast = Cast(f_id=f_id, a_id=a_id, role=role)
            db.add(cast)
            print("Added new role")
            db.commit()

def fill_genres_table(file):
    with open(file) as f:
        reader = csv.reader(f)
        for genre in reader:
            genre = Genre(genre=genre)
            db.add(genre)
            print("Added new Genre -> {}".format(genre))
            db.commit()

def fill_movie_genre_table(file):
    with open(file) as f:
        reader = csv.reader(f)
        for f_id, g_id in reader:
            mov_genre = Movie_Genre(f_id=f_id, g_id=g_id)
            db.add(mov_genre)
            print("Added new dependecies between movie and genre")
            db.commit()
def parse_args():
    parser = argparse.ArgumentParser(description='Drop tables if needeed')
    parser.add_argument('--drop', default=False, help='set True if you want dropp tables')
    opt = parser.parse_args()
    return opt

def main():
    args = parse_args()
    if args.drop:
        for table in ['roles','movie_genre','genres','actors','movies']:
            db.execute("DROP TABLE {};".format(table))
            db.commit()
        call(["python", "create.py"])
    #
    # fill_movie_table("movies.csv")
    # fill_actors_table("actors.csv")
    # fill_cast_table("cast.csv")
    # fill_genres_table("genre.csv")
    # fill_movie_genre_table("movie-genre.csv")
    movie_info = db.execute("select  * from Movie_Info;").fetchall()
    print(movie_info)
    db.commit()
if __name__ == "__main__":
    main()
