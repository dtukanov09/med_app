import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Patience1 to Insert
pac_id_1='333ghp'
doct_id_1='123ghp'
diagnosis_1='Воспаление хитрожопного нерва'
complaints_1='Болит всё и сразу. Причем с утра. Легчает только после стопаря. '
observation_data_1='На лицо ярковыраженный синильный синдром'
current_treat_1='Консервативное. Назначено регулярно посещение вытрезвителя. Тренировка силы воли. '
drugs_1='Рассол перорально. В периоды обострения внутревенно'
operation_etc_1='Пока нет смысла. Организм проспиртован'
extra_info_1='Во время прошлого приема спиздил у меня сто рублей'
images_1=0


#Patience2 to Insert
pac_id_2='444ghp'
doct_id_2='123ghp'
diagnosis_2='Первичный диагноз - понос. Вторичный - запор. Возможно, наоборот'
complaints_2='Симптомы типичные. Обострения наблюдаются после употребления шаурмосодержащих продуктов'
observation_data_2='На коже, в стуле, в моче, поте и прочих выделениях организма все признаки передозировки майонеза. Интоксикация организма мясом животных рода кошачих и собачих'
current_treat_2='Консервативное. Прием сорбентов перед, после и во время еды '
drugs_2='Уголь активированный, деактивированный, антрацит.'
operation_etc_2='Назначен отсос продуктов полураспада шаурмы из желудка методом прямого сквозного протока'
extra_info_2='Во время приема пациент заляпал стол каплями майонеза'
images_2=0


#Patience3 to Insert
pac_id_3='555ghp'
doct_id_3='123ghp'
diagnosis_3='Прыщ на попе'
complaints_3='Чувство морального угнетения и психологического дискомфорта, вызванные наличием красного прыщеобразного образования на мягких тканях задней поверхности бедра'
observation_data_3='Наличие прыща подтверждено многочисленными лабораторными исследованиями'
current_treat_3='Современной медицинской наукой лечение не предусмотрено'
drugs_3='Местно - мазь, йод'
operation_etc_3='В связи с отсутствием квалифицированных специалистов оперативное вмешатльство невозможно'
extra_info_3='Ржали всей больницей'
images_3=0



list_to_insert = [(pac_id_1,doct_id_1, diagnosis_1, complaints_1, observation_data_1, current_treat_1, drugs_1, operation_etc_1,extra_info_1,images_1),
                  (pac_id_2,doct_id_2, diagnosis_2, complaints_2, observation_data_2, current_treat_2, drugs_2, operation_etc_2,extra_info_2,images_2),
                  (pac_id_3,doct_id_3, diagnosis_3, complaints_3, observation_data_3, current_treat_3, drugs_3, operation_etc_3,extra_info_3,images_3)
                  ]


#Insert Data into Table specialists
cur.executemany(""" INSERT INTO treat_data VALUES (?,?,?,?,?,?,?,?,?,?)""",list_to_insert)


#Commit command
conn.commit()

#Close connection
conn.close()
