from flask_table import Table, Col

class Movie_Table(Table):
    id = Col('ID')
    name = Col('Name')
    year = Col('Year')
    budget = Col('Budget(mln $)')
    fees = Col('Fees(mln $)')
    country = Col('Country')
    rate = Col('Rate')
    duration = Col('Duration (mn)')
    plot_description = Col('Plot Description')

class Actors_Table(Table):
    id = Col('ID')
    name = Col('Name')
    birth_date = Col('Birth_date')
    nationality = Col('Nationality')
    gender = Col('Gender')
    age = Col('Age')


class Cast_Table(Table):
    id = Col('ID')
    f_id = Col('Film ID')
    a_id = Col('Actor ID')
    role = Col('Role')

class Movie_Genre_Table(Table):
    id = Col('ID')
    f_id = Col('Film ID')
    g_id = Col('Genre ID')

class Genre_Table(Table):
    id = Col('ID')
    genre = Col('Genre')

class Movie(object):
    def __init__(self, id, name,year,budget,fees,country,rate,duration,plot_description):
        self.id = id
        self.name = name
        self.year =year
        self.budget = budget
        self.fees = fees
        self.country = country
        self.rate = rate
        self.duration = duration
        self.plot_description = plot_description

class Actor(object):
    def __init__(self, id, name,birth_date,nationality,gender,age):
        self.id = id
        self.name = name
        self.birth_date =birth_date
        self.nationality = nationality
        self.gender = gender
        self.age = age

class Cast(object):
    def __init__(self, id, f_id,a_id,role):
        self.id = id
        self.f_id = f_id
        self.a_id =a_id
        self.role = role

class Genre(object):
    def __init__(self, id, genre):
        self.id = id
        self.genre = genre

class Movie_Genre(object):
    def __init__(self, id, f_id,g_id):
        self.id = id
        self.f_id = f_id
        self.g_id =g_id


def create_table_view_for_flask(table_type,table_data):
    items = []

    if table_type == 'movies':
        print(type(table_data))
        for movie in table_data:
            items.append(Movie(movie.id,movie.name,movie.year,movie.budget,
            movie.fees,movie.country,movie.rate,movie.duration,movie.plot_description))
        table = Movie_Table(items)

    elif table_type == 'actors':
        for actor in table_data:
            items.append(Actor(actor.id,actor.name,actor.birth_date,actor.nationality,
            actor.gender,actor.age))
        table = Actors_Table(items)

    elif table_type == 'roles':
        for role in table_data:
            items.append(Cast(role.id,role.f_id,role.a_id,role.role))
        table = Cast_Table(items)

    elif table_type == 'genres':
        for genre in table_data:
            items.append(Genre(genre.id, genre.genre))
        table = Genre_Table(items)

    elif table_type == 'genre of the movie':
        for m_g in table_data:
            items.append(Movie_Genre(m_g.id, m_g.f_id, m_g.g_id))
        table = Movie_Genre_Table(items)
    return table
