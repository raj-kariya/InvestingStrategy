from Task1 import typeconversion
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
import psycopg2
from psycopg2 import sql

connection = psycopg2.connect(
    user="rajkariya",
    password="Enter",
    host="127.0.0.1",
    port="5432",
    database="postgres_db")


connection.close()
path1 = "/Users/rajkariya/Documents/projects/Assesment/HINDALCO_1D.csv"
df = pd.read_csv(path1)
# df["datetime"] = pd.to_datetime(df["datetime"])
df = typeconversion(df)
df2 = df[df['instrument'] == 'HINDALCO']
df2['short_moving_average'] = df2['close'].rolling(window=20).mean()
df2['long_moving_average'] = df2['close'].rolling(window=70).mean()

print("Calculating Moving Average(MA) based on the crossover startegy")
df2['signal'] = 0
# When the short-term MA crosses above the long-term MA , set signal to 1(buy)
df2.loc[df2["short_moving_average"] > df2["long_moving_average"], 'signal'] = 1
#When the short-term MA crosses below the long-term MA , set signal to -1(sell)
df2.loc[df2["short_moving_average"] < df2["long_moving_average"], 'signal'] = -1
print("Plotting Graphs with the results")
plt.figure(figsize=(12,6))
plt.plot(df2["datetime"],df2["close"],label='Closing Price',alpha=0.5)
plt.plot(df2["datetime"],df2["short_moving_average"],label='Short-term MA(20 days)')
plt.plot(df2["datetime"],df2["long_moving_average"],label='Long-term MA(50 days)')
plt.title('Simple Moving Average CrossOver')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()