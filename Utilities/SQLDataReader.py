import mysql.connector
from Utilities.ConfigReader import configReader

sql_config = {'user': configReader.getDBUser(),
              'password': configReader.getDBPassword(),
              'host': configReader.getDBHost(),
              'database': configReader.getDBName()
              }


def getSQLData(query):
    connection = mysql.connector.connect(**sql_config)

    cursor = connection.cursor()

    cursor.execute(query)

    rows = cursor.fetchall()

    connection.close()

    return rows
