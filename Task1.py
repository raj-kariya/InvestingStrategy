from datetime import datetime

import pandas as pd
import psycopg2
from psycopg2 import sql
def typeconversion(df):
    types = {'open' : 'float64', 'volume':'int64', 'close' : 'float64', 'high' : 'float64', 'low' : 'float64', 'datetime': 'datetime64[ns]', 'instrument' : 'string'}
    df = df.astype(types)
    return df

if __name__ == '__main__':
    connection = psycopg2.connect(
        user="rajkariya",
        password="Enter",
        host="127.0.0.1",
        port="5432",
        database="postgres_db")

    # Create a cursor object to interact with the database
    cursor = connection.cursor()
    path1 = "/Users/rajkariya/Documents/projects/Assesment/HINDALCO_1D.csv"
    df = pd.read_csv(path1)
    #Define the table schema
    table_name = "stock_data"

    create_table_query = sql.SQL(
        '''
        CREATE TABLE IF NOT EXISTS {} (
            id SERIAL PRIMARY KEY,
            datetime TIMESTAMP,
            close NUMERIC,
            high NUMERIC,
            low NUMERIC,
            open NUMERIC,
            volume INTEGER,
            instrument VARCHAR(50)
        );
        ''').format(sql.Identifier(table_name))

    cursor.execute(create_table_query)

    # Insert data into the table
    insert_query = """
        INSERT INTO {} (datetime, close, high, low, open, volume, instrument)
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """.format(table_name)
    print("Converting the type conversion...")
    # df['datetime'] = pd.to_datetime(df['datetime'])
    df = typeconversion(df)
    data = [tuple(row) for row in df.values]
    print("Inserting Data into the Database...")
    cursor.executemany(insert_query, data)

    connection.commit()

    cursor.close()
    connection.close()
