from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    budget = db.Column(db.Float, nullable=False)
    fees = db.Column(db.Float, nullable=False,)
    country = db.Column(db.String, nullable=False)
    rate = db.Column(db.Float, nullable=True)
    duration = db.Column(db.Integer, nullable=False)
    plot_description = db.Column(db.String, nullable=True)

class Actor(db.Model):
    __tablename__ = "actors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    birth_date = db.Column(db.String, nullable=False)
    nationality = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)

class Cast(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    f_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    a_id =  db.Column(db.Integer, db.ForeignKey("actors.id"), nullable=False)
    role = db.Column(db.String, nullable=False)

class Genre(db.Model):
    __tablename__ = "genres"
    id = db.Column(db.Integer, primary_key=True)
    genre = db.Column(db.String, nullable=False)

class Movie_Genre(db.Model):
    __tablename__ = "movie_genre"
    id = db.Column(db.Integer, primary_key=True)
    f_id = db.Column(db.Integer, db.ForeignKey("movies.id"), nullable=False)
    g_id =  db.Column(db.Integer, db.ForeignKey("genres.id"), nullable=False)
