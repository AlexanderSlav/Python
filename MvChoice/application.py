import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from credentials import *
from tables_for_flask import *
tables = [{'name':'movies'},{'name':'actors'},{'name':'roles'}
            ,{'name':'genres'},{'name':'genre of the movie'}]
movies_parametres = [{'name':name } for name in ['Name', 'Year','Plot']]
actors_parametres = [{'name':name } for name in ['Name', 'Age','Nationality']]


app = Flask(__name__)
password = os.getenv("POSTGRES_PASSWORD")
credentials = Credentials('Final_Project',password)
engine = create_engine(credentials.DB_CONN_URI_DEFAULT)
db = scoped_session(sessionmaker(bind=engine))

# Home page with tables list
@app.route("/")
def index():
    return render_template('welcome_page.html')


@app.route("/view_tables",methods=["POST","GET"])
def tables_view():
    table = request.form.get("table_name")
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
    return render_template('error.html',table = table, message='There is no such table -> ')


@app.route("/tables")
def tables_choice():
    return render_template('index.html',tables=tables)


@app.route("/search_m")
def search_m():

    return render_template('search_m.html',parameters=movies_parametres)

@app.route("/search_a")
def search_a():

    return render_template('search_a.html',parameters=actors_parametres)

@app.route("/search_in_movie_by_exac_param",methods=["POST","GET"])
def mov_search():

    search_parameter = request.form.get("param_name")
    search_value = request.form.get("param_value")
    table = 'movies'
    if search_parameter == 'Name':
        result = db.execute(f"select  * from Search_Movie_By_Name(\'%{search_value}%\');").fetchall()
        html_table = create_table_view_for_flask(table, result)
        return render_template('tables_window.html',html_table = html_table)
    if search_parameter == 'Plot':
        result = db.execute(f"select * from  Search_Movie_By_Plot(\'%{search_value}%\');").fetchall()
        html_table = create_table_view_for_flask(table, result)
        return render_template('tables_window.html',html_table = html_table)
    if search_parameter == 'Year':
            if search_value[0] == '<':
                search_value = search_value[1:]
                comparison_type = 'less'
            elif search_value[0] == '>':
                search_value = search_value[1:]
                comparison_type = 'greater'
            else:
                comparison_type = 'equal'
            result = db.execute(f"select * from  Search_Movie_By_Year({search_value},\'{comparison_type}\');").fetchall()
            html_table = create_table_view_for_flask(table, result)
            return render_template('tables_window.html',html_table = html_table)

@app.route("/search_in_actors_by_exac_param",methods=["POST","GET"])
def actors_search():
        search_parameter = request.form.get("param_name")
        search_value = request.form.get("param_value")
        table = 'actors'
        if search_parameter == 'Name':
            result = db.execute(f"select  * from Search_Actor_By_Name(\'%{search_value}%\');").fetchall()
            html_table = create_table_view_for_flask(table, result)
            return render_template('tables_window.html',html_table = html_table)
        if search_parameter == 'Age':
            if search_value[0] == '<':
                search_value = search_value[1:]
                comparison_type = 'less'
            elif search_value[0] == '>':
                search_value = search_value[1:]
                comparison_type = 'greater'
            else:
                comparison_type = 'equal'
            result = db.execute(f"select * from  Search_Actor_By_Age({search_value},\'{comparison_type}\');").fetchall()
            html_table = create_table_view_for_flask(table, result)
            return render_template('tables_window.html',html_table = html_table)
        if search_parameter == 'Nationality':
            result = db.execute(f"select  * from Search_Actor_By_Nationality(\'%{search_value}%\');").fetchall()
            html_table = create_table_view_for_flask(table, result)
            return render_template('tables_window.html',html_table = html_table)
