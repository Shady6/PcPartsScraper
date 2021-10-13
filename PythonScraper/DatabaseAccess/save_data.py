from DatabaseAccess.connection import connect
from CurrencyAPI.exchange_rates import loadExchangeRates


def saveAll():
    conn = connect()
    with conn:
        cursor = conn.cursor()
        savePcParts(cursor)
        saveExchangeRates(cursor)


def savePcParts(cursor):
    bulkInsert(cursor)


def bulkInsert(cursor):
    cursor.execute(
        "COPY public.pcparts(shopname, productname,category,detailedname,price,producentcode,listingdate) FROM 'D:/DEV/Python/PcPartsScrap/PythonScraper/_csv/_all_pcPartsDbFormat.csv' WITH (FORMAT csv);")


def saveExchangeRates(cursor):
    exchangeRates = loadExchangeRates()

    for exchangeRate in exchangeRates:
        key = list(exchangeRate.keys())[0]
        # IF NOT EXISTS(SELECT * FROM public.ExchangeRates WHERE from_to='{key}'
        # AND date='{exchangeRate[key]["timestamp"]}' AND value={exchangeRate[key]["val"]})
        query = f"""        
        insert into public.ExchangeRates (from_to, value, date)
        values ('{key}', {exchangeRate[key]["val"]}, '{exchangeRate[key]["timestamp"]}');"""
        cursor.execute(query)
