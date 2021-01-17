import pyodbc 

def connect():    
    connection = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-CVC40GK;'
                        'Database=skateSpot2TestDb;'
                        'Trusted_Connection=yes;')

    return connection