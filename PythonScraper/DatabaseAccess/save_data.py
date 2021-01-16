from DatabaseAccess.connection import connect

cursor = connect()

def savePcParts(pcParts):
    query = "INSERT"