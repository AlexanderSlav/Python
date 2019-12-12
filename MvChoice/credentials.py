class Credentials:
    """
    credentials maker for connection to database using url
    params:
    db_name - database name
    password - password from the user
    """
    def __init__(self, db_name, password):
        self.DB_CONFIG_DICT = {
                'user': 'postgres',
                'password': password,
                'host': 'localhost',
                'port': 5432,
        }

        self.DB_CONN_FORMAT = "postgresql://{user}:{password}@{host}:{port}/{database}"
        self.DB_CONN_URI_DEFAULT = (self.DB_CONN_FORMAT.format(
            database= db_name,
            **self.DB_CONFIG_DICT))
    def new_database(self,new_db_name):
        self.DB_CONN_URI_NEW = (self.DB_CONN_FORMAT.format(
            database= new_db_name,
            **self.DB_CONFIG_DICT))
