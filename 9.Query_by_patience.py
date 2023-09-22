import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Показываеь данные для конкретного пациент по имени. 
#Показываем имя пациента, имя врача, диагноз, текущее лечение и назначенные препараты     

name = 'Петров Петр Петрович'

cur.execute ( """ SELECT pac_name AS name,
                         doc_name AS doct_name,
                         diagnosis AS diagnosis,
                         current_treat AS treatment,
                         drugs AS drugs
                 FROM patiences AS t
                 LEFT JOIN treat_data AS s
                 ON t.pac_id = s.pac_id
                 LEFT JOIN specialists AS g
                 ON s.doct_id = g.doct_id
                 WHERE t.pac_name LIKE "%Петров Петр Петрович%";""")

results = cur.fetchall()

for result in results:
    print(result)

    
#Commit command
conn.commit()

#Close connection
conn.close()
