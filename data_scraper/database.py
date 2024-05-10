import sqlite3
import pandas as pd
from IFSC_scraper import tobys_data


# create database & cursor
connection = sqlite3.connect('IFSC.db')

cursor = connection.cursor()

# create table
cursor.execute('create table toby_roberts (placement integer, date text)')

cursor.executemany('INSERT INTO toby_roberts VALUES (?, ?)', tobys_data)



connection.close()