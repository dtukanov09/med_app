import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Show Table specialists 
cur.execute ("""SELECT * FROM specialists """)

#cur.execute ("""SELECT * FROM specialists_data """)

print(cur.fetchall())




#Commit command
conn.commit()

#Close connection
conn.close()
