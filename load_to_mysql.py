import pandas as pd
import mysql.connector

def load_to_mysql_data():

    df = pd.read_csv("data/weather.csv")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Arunima@2001",
        database="weather_db"
    )

    cursor = conn.cursor()

    for i, row in df.iterrows():
        sql = """
        INSERT INTO weather_data (city, temperature, humidity, weather, description, datetime)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        values = tuple(row)
        cursor.execute(sql, values)

    conn.commit()
    conn.close()
    print(" Data inserted into MySQL database.")

