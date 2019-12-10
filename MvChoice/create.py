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

# def create_database():
#     conn = engine_default.connect()
#     conn.execute("COMMIT")
#     if database_exists(DB_CONN_URI_NEW):
#         print('Database already exists')
#         conn.close()
#         return 0
#     # Do not substitute user-supplied database names here.
#     conn.execute("CREATE DATABASE %s" % NEW_DB_NAME)
#     conn.close()
#     return 1
#
# def drop_database():
#     conn = engine_default.connect()
#     conn.execute("COMMIT")
#     # Do not substitute user-supplied database names here.
#     conn.execute("DROP DATABASE %s" % NEW_DB_NAME)
#     conn.close()
#
# def main():
#     # f = open("flights.csv")
#     # reader = csv.reader(f)
#     # for origin, destination, duration in reader:
#     if create_database() == 1:
#       print('{} was created.'.format(NEW_DB_NAME))
#     #drop_database()
#     #  print('{} was dropped.'.format(NEW_DB_NAME))
#
#     # (origin, destination, duration) VALUES (:origin, :destination, :duration)",
#     #                 {"origin": origin, "destination": destination, "duration": duration}
#     # print(f"Added flight from {origin} to {destination} lasting {duration} minutes.")
#     #print('Selected from Покупатель')
#     db.commit()
