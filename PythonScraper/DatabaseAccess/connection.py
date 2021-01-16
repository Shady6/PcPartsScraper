import pyodbc 

def connect():    
    conn = pyodbc.connect('Driver={SQL Server};'
                        'Server=DESKTOP-CVC40GK;'
                        'Database=skateSpot2TestDb;'
                        'Trusted_Connection=yes;')

    cursor = conn.cursor()
    return cursor