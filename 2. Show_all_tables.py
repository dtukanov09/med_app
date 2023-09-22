import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()


#Swows all tables from db
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
