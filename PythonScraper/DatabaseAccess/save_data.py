from DatabaseAccess.connection import connect
from datetime import datetime
from CurrencyAPI.exchange_rates import loadExchangeRates

def saveAll():
    conn = connect()
    with conn:
        cursor = conn.cursor()
        savePcParts(cursor)
        saveExchangeRates(cursor)


def savePcParts(cursor):
    bulkInsert(cursor, "PCPartsScrap.dbo.PCParts", "C:\\Mikolaj\\DEV\Python\\PcPartsScrap\\PythonScraper\\_csv\\pcPartsDbFormat.csv")


def bulkInsert(cursor, table_name, file_path):
    query = "BULK INSERT {} FROM '{}' WITH (FORMAT = 'CSV');"
    cursor.execute(query.format(table_name, file_path))    


def saveExchangeRates(cursor):
    exchangeRates = loadExchangeRates()

    for exchangeRate in exchangeRates:
        key = list(exchangeRate.keys())[0]
        query = f"""IF NOT EXISTS (SELECT * FROM PCPartsScrap.dbo.ExchangeRates WHERE from_to = '{key}'
        AND date = '{exchangeRate[key]["timestamp"]}' AND value = {exchangeRate[key]["val"]})
        BEGIN
            insert into PCPartsScrap.dbo.ExchangeRates (from_to, [value], [date])
            values ('{key}', {exchangeRate[key]["val"]}, '{exchangeRate[key]["timestamp"]}');
        END"""
        cursor.execute(query)        