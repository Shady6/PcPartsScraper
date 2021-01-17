from DatabaseAccess.connection import connect
from datetime import datetime


def saveAll(pcParts, producentCodes):
    conn = connect()
    with conn:
        cursor = conn.cursor()
        savePcParts(cursor, pcParts)


def savePcParts(cursor, pcParts):
    bulk_insert(cursor, "PCPartsScrap.dbo.PCParts", "C:\\Mikolaj\\DEV\Python\\PcPartsScrap\\PythonScraper\\_csv\\pcPartsDbFormat.csv")

def bulk_insert(cursor, table_name, file_path):
    query = "BULK INSERT {} FROM '{}' WITH (FORMAT = 'CSV');"
    cursor.execute(query.format(table_name, file_path))    
