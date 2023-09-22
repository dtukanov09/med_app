import sqlite3

#Connect to database
conn = sqlite3.connect('med_app_db.db')


#Create a cursor
cur = conn.cursor()

#Create a General Table For Specialist
cur.execute ("""
           CREATE TABLE specialists (
                  doct_id TEXT,
                  doc_name TEXT,
                  specializaton TEXT,
                  tel_num  TEXT,
                  PRIMARY KEY (doct_id)
                                    )                
           """)

#In_deep Specialists Data
cur.execute ("""
           CREATE TABLE specialists_data(
                  doct_id TEXT,
                  date_of_birth TEXT,
                  specializaton TEXT,
                  institute TEXT,
                  diploma   TEXT,
                  date_of_grad TEXT,
                  science_grad TEXT,
                  extra_info TEXT,
                  FOREIGN KEY (doct_id) REFERENCES specialists(doct_id)
                                         )                
           """)
#Patience Data
cur.execute ("""
           CREATE TABLE patiences (
                  pac_id TEXT,
                  pac_name TEXT,
                  sex TEXT,
                  date_of_birth TEXT,
                  age INT,
                  tel_num  TEXT,
                  adress TEXT,
                  PRIMARY KEY (pac_id)                    )                
           """)

#Treatment Data
cur.execute ("""
           CREATE TABLE treat_data(
                  pac_id TEXT,
                  doct_id TEXT,
                  diagnosis TEXT,
                  complaints TEXT,
                  observation_data TEXT,
                  current_treat TEXT,
                  drugs TEXT,
                  operation_etc TEXT,
                  extra_info TEXT,
                  images BLOB,
                  FOREIGN KEY (pac_id) REFERENCES patiences(pac_id)
                  FOREIGN KEY (doct_id) REFERENCES specialists(doct_id)
                                         )                
           """)

#Commit command
conn.commit()

#Close connection
conn.close()


