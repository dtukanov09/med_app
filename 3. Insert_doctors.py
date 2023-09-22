import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Data to Insert

doc_id = '123ghp'
name = 'Пупкин Василий Геннадиевич'
specialization = 'Терапевт'
tel_num = '+780503452345'

list_to_insert = [(doc_id,name,specialization,tel_num)]

#Insert Data into Table specialists
cur.executemany(""" INSERT INTO specialists VALUES (?,?,?,?)""",list_to_insert)

#Commit command
conn.commit()

#Close connection
conn.close()
