import pyodbc


def connect():
    connection = pyodbc.connect('Driver={PostgreSQL Unicode};'
                                'Server=localhost;'
                                'Port:5432;'
                                'Database=PcPartScrap;'
                                'Uid=postgres;'
                                'PWD=123;'
                                'Trusted_Connection=yes;')

    return connection
