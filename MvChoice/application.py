import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from credentials import *
from tables_for_flask import *
tables = [('movies'),('actors'),('roles'),('genres'),('genre of the movie')]
app = Flask(__name__)
password = os.getenv("POSTGRES_PASSWORD")
credentials = Credentials('Final_Project',password)
engine = create_engine(credentials.DB_CONN_URI_DEFAULT)
db = scoped_session(sessionmaker(bind=engine))

# Home page with tables list
@app.route("/")
def index():
    return render_template('index.html',tables=tables)


@app.route("/tables",methods=["POST","GET"])
def tables_view():
    table = request.form.get("table")
    if table == 'movies':
        movies = db.execute("select  * from Movie_Info;").fetchall()
        html_table = create_table_view_for_flask(table, movies)
        return render_template('tables_window.html',html_table = html_table)
    if table == 'actors':
        movies = db.execute("select  * from Actors_Info;").fetchall()
        html_table = create_table_view_for_flask(table, movies)
        return render_template('tables_window.html',html_table = html_table)
    if table == 'genres':
        movies = db.execute("select  * from Genre_Info;").fetchall()
        html_table = create_table_view_for_flask(table, movies)
        return render_template('tables_window.html',html_table = html_table)
    if table == 'genre of the movie':
        movies = db.execute("select  * from Movie_Genre_Info;").fetchall()
        html_table = create_table_view_for_flask(table, movies)
        return render_template('tables_window.html',html_table = html_table)
    if table == 'roles':
        movies = db.execute("select  * from Cast_Info;").fetchall()
        html_table = create_table_view_for_flask(table, movies)
        return render_template('tables_window.html',html_table = html_table)
    return ('Nothing')
