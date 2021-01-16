from DatabaseAccess.connection import connect
from datetime import datetime

cursor = connect()

def saveAll(pcParts, producentCodes):
    savePcParts(pcParts)

def savePcParts(pcParts):
    bulk_insert("PCPartsScrap.dbo.PCParts", "C:\\Mikolaj\\DEV\Python\\PcPartsScrap\\PythonScraper\\_csv\\pcPartsDbFormat.csv")

def bulk_insert(table_name, file_path):
    query = "BULK INSERT {} FROM '{}' WITH (FORMAT = 'CSV');"
    cursor.execute(query.format(table_name, file_path))
    cursor.commit()
