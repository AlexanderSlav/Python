import os

from flask import Flask, render_template, request
from table_classes import *
from credentials import *

password = os.getenv("POSTGRES_PASSWORD")
credentials = Credentials('Final_Project',password)
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = credentials.DB_CONN_URI_DEFAULT
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
