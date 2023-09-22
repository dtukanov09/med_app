import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Patience1 to Insert
pac_id_1 = '333ghp'
name_1 = 'Петров Петр Петрович'
sex_1 = 'Мужской'
date_of_birth_1 = '1987-05-12'
age_1 = 41
tel_num_1 = '+780503452345'
adress_1 = 'г.Москвабад, ул. Пригожина, 43/34'


#Patience2 to Insert
pac_id_2 = '444ghp'
name_2 = 'Иванов Иван Иванович'
sex_2 = 'Мужской'
date_of_birth_2 = '1989-12-02'
age_2 = 34
tel_num_2 = '+7805035637'
adress_2 = 'г.Москвабад, ул. Навального, 14/88'


#Patience3 to Insert
pac_id_3 = '555ghp'
name_3 = 'Войцеховский ВАцлав Станиславович'
sex_3 = 'Транс'
date_of_birth_3 = '1992-09-08'
age_3 = 31
tel_num_3 = '+78050345777'
adress_3 = 'пгт.Мухосранск, тупик Эволюционный, 15'



list_to_insert = [(pac_id_1,name_1,sex_1,date_of_birth_1,age_1,tel_num_1,adress_1),
                  (pac_id_2,name_2,sex_2,date_of_birth_2,age_2,tel_num_2,adress_2),
                  (pac_id_3,name_3,sex_3,date_of_birth_3,age_3,tel_num_3,adress_3)
                  ]


#Insert Data into Table specialists
cur.executemany(""" INSERT INTO patiences VALUES (?,?,?,?,?,?,?)""",list_to_insert)

#Commit command
conn.commit()

#Close connection
conn.close()
