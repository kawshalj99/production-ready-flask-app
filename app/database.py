import mysql.connector
import os


def get_connection():

    connection = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST"),
        database=os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD")
    )

    return connection