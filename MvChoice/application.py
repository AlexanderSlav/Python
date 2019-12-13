import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from credentials import *
from tables_for_flask import *
from sqlalchemy_utils.functions import database_exists
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

@app.route("/get_database_name")
def get_database_name():
    return render_template('get_database_name_to_create.html')


@app.route("/update_movie",methods=["POST","GET"])
def update_movie():
    option = request.form.get("update_option")
    value = request.form.get("param_value")
    t_id = request.form.get("target_id")
    if option == 'rate':
        if value[0] in {'+', '-'}:
            sign, value = value[0], value[1]
        else:
            sign, value = '+', value
        result = db.execute(f"select  * from Update_Rate({t_id},{value},\'{sign}\');").fetchall()
        db.commit()
        return render_template('success.html')
    elif option == 'fees':
        result = db.execute(f"select  * from Update_Fees({t_id},{value});").fetchall()
        db.commit()
        return render_template('success.html')
    else:
        return render_template('error.html')


@app.route("/update_option")
def update_option_movie():
    return render_template('choose_update_variable.html')

@app.route("/drop_database_name")
def drop_database_name():
    return render_template('get_database_name_to_delete.html')

@app.route("/create_database",methods=["POST","GET"])
def create_database():
    db_name = request.form.get("database_name")
    db_name = db_name.lower()
    conn = engine.connect()
    conn.execute("COMMIT")
    credentials.new_database(db_name)
    if database_exists(credentials.DB_CONN_URI_NEW):
        print('Database already exists')
        conn.close()
        return  render_template('error.html')
    conn.execute("CREATE DATABASE %s" % db_name)
    conn.close()
    return render_template('success.html')

@app.route("/drop_database", methods=["POST", "GET"])
def drop_database():
    db_name = request.form.get('database_name')
    db_name = db_name.lower()
    conn = engine.connect()
    conn.execute("COMMIT")
    credentials.new_database(db_name)
    if database_exists(credentials.DB_CONN_URI_NEW):
        conn.execute("DROP DATABASE %s" % db_name)
        conn.close()
        return render_template('success.html')
    else:
        conn.close()
        return render_template('error.html')


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


@app.route("/get_insert_actors_parameters")
def get_actor_parameters():
    return render_template('insert_actor.html')

@app.route("/get_delete_parameters")
def get_delete_parameters():
    return render_template('delete.html')

@app.route("/delete_object",methods=["POST","GET"])
def delete_object():
    html_table = None
    table_type = request.form.get("table_type")
    object_to_delete = request.form.get("object_to_delete")
    if table_type:
        result = db.execute(f"select delete_data_by_name(\'{table_type}\',\'{object_to_delete}\')").fetchall()

    else:
        result = db.execute("call clear_all_Tables()")
        # new_films = db.execute("select  * from Movie_Info;").fetchall()
        # html_table = create_table_view_for_flask(table_type, new_films)
    if table_type == 'actors':
        new_actors = db.execute("select  * from Actors_Info;").fetchall()
        html_table = create_table_view_for_flask(table_type, new_actors)
    elif table_type == 'movies':
        new_films = db.execute("select  * from Movie_Info;").fetchall()
        html_table = create_table_view_for_flask(table_type, new_films)
    db.commit()



    return render_template('tables_window.html',html_table = html_table)


@app.route("/insert_actor_in_db",methods=["POST","GET"])
def insert_actor():
    search_parameters = [request.form.get(name) for name in ("name_value","birth_date","nationality",
                                                            "gender","age")]


    result = db.execute(f"select insertIntoActors(\'{search_parameters[0]}\',\'{search_parameters[1]}\',\'{search_parameters[2]}\',\'{search_parameters[3]}\',{search_parameters[4]})").fetchall()
    table = 'actors'
    new_actors = db.execute("select  * from Actors_Info;").fetchall()
    html_table = create_table_view_for_flask(table, new_actors)
    db.commit()
    return render_template('tables_window.html',html_table = html_table)


@app.route("/get_insert_movies_parameters")
def get_movie_parameters():
    return render_template('insert_m.html')

@app.route("/insert_movie_in_db",methods=["POST","GET"])
def insert_movie():
    search_parameters = [request.form.get(name) for name in ("name_value","year_value","budget_value",
                                                            "fees_value","country_value","rate_value",
                                                            "duration_value","plot_description_value")]


    result = db.execute(f"select insertIntoMovie(\'{search_parameters[0]}\',{search_parameters[1]},{search_parameters[2]},{search_parameters[3]}, \'{search_parameters[4]}\',{search_parameters[5]},{search_parameters[6]},\'{search_parameters[7]}\')").fetchall()
    table = 'movies'
    new_movies = db.execute("select  * from Movie_Info;").fetchall()
    html_table = create_table_view_for_flask(table, new_movies)
    db.commit()
    return render_template('tables_window.html',html_table = html_table)



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
