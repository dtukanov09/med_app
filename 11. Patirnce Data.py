import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import ttk


#Main window
window = tk.Tk()
window.title("Данные пациента")
window.eval("tk::PlaceWindow . center")

#Connect to database
conn = sqlite3.connect('med_app_db.db')
#Create a cursor
cur = conn.cursor()


#Create a frame on main window
frame2 = tk.Frame(window, width = 500, height = 750, bg = "#3d6466")
frame2.grid(row = 0, column = 0)
frame2.pack_propagate(False)

#Общая информация
pat_label = tk.Label(frame2, text = "Пациент",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",16))
pat_label.pack()


#Поле выбора пациента
list_to_combobox = []
cur.execute(""" SELECT pac_name FROM patiences""")
list_patiences = cur.fetchall()
for pat in list_patiences:
    list_to_combobox.append(pat[0])
 
patiences = ttk.Combobox(width = 75, height = 20,values=list_to_combobox)
patiences.place(x=10, y = 40)

#Get values for patience
def get_patience_data():
    
    #Delete previous query
    pat_sex.delete("1.0",'end')
    birth.delete("1.0",'end')
    age.delete("1.0",'end')
    pat_tel.delete("1.0",'end')
    pat_ad.delete("1.0",'end')
    diagnosis.delete("1.0",'end')
    state.delete("1.0",'end')
    observ.delete("1.0",'end')
    treatment.delete("1.0",'end')
    drugs.delete("1.0",'end')
    procedure.delete("1.0",'end')
    extra_info.delete("1.0",'end')

    #Connect to database
    conn = sqlite3.connect('med_app_db.db')
    #Create a cursor
    cur = conn.cursor()

    
    patience_to_chose = patiences.get()
    params = {'name':patience_to_chose}
    
    data_list =  []
    cur.execute("""SELECT sex,
                           date_of_birth,
                           age,
                           tel_num,
                           adress,
                           diagnosis,
                           complaints,
                           observation_data,
                           current_treat,
                           drugs,
                           operation_etc,
                           extra_info
                    FROM patiences AS t
                    LEFT JOIN treat_data AS s
                    ON t.pac_id = s.pac_id
                    WHERE t.pac_name = :name""",params)
    pat_data = cur.fetchall()
    for data in pat_data:
        data_list.append(data)

    pat_sex.insert("1.0", data_list[0][0])
    birth.insert ("1.0", data_list[0][1])
    age.insert("1.0", data_list[0][2])
    pat_tel.insert("1.0", data_list[0][3])
    pat_ad.insert("1.0", data_list[0][4])
    diagnosis.insert("1.0", data_list[0][5])
    state.insert("1.0", data_list[0][6])
    observ.insert("1.0", data_list[0][7])
    treatment.insert("1.0", data_list[0][8])
    drugs.insert("1.0", data_list[0][9])
    procedure.insert("1.0", data_list[0][10])
    extra_info.insert("1.0", data_list[0][11])


    #Commit command
    conn.commit()
    #Close connection
    conn.close()



#Кнопка выбора пациента
button_chose_pat = tk.Button(text = "ВЫБОР", width = 38, bg = "#53868B",
                     fg = "#F0F8FF",
                     font = ("TkMenuFont",16),command = get_patience_data)
button_chose_pat.place(x=14, y = 70, height = 40)

#Данные пациента
data_label = tk.Label(frame2, text = "Данные пациента",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",16))
data_label.place(x=160, y = 110)

#Отображение данных пациента
#Год рождения
label_birth_pat = tk.Label(frame2,text = "Год рождения",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_birth_pat.place(x=10, y = 140)

birth = tk.Text(height =1, width = 15, font=("TkMenuFont",10))
birth.place(x=10, y = 160)

#Возраст
label_age = tk.Label(frame2,text = "Возраст",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_age.place(x=180, y = 140)

age = tk.Text(height =1, width = 15, font=("TkMenuFont",10))
age.place(x=180, y = 160)

#Пол
label_sex = tk.Label(frame2,text = "Пол",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_sex.place(x=350, y = 140)

pat_sex = tk.Text(height =1, width = 15, font=("TkMenuFont",10))
pat_sex.place(x=350, y = 160)

#Телефон
label_pat_tel = tk.Label(frame2,text = "Телефон",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_pat_tel.place(x=10, y = 180)

pat_tel = tk.Text(height =1, width = 64, font=("TkMenuFont",10))
pat_tel.place(x=10, y = 200)

#Адрес
label_pat_ad = tk.Label(frame2,text = "Адрес",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_pat_ad.place(x=10, y = 220)

pat_ad = tk.Text(height =1, width = 64, font=("TkMenuFont",10))
pat_ad.place(x=10, y = 240)

#Диагноз
label_diagnosis = tk.Label(frame2,text = "Диагноз",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_diagnosis.place(x=10, y = 260)

diagnosis = tk.Text(height = 2, width = 64, font=("TkMenuFont",10))
diagnosis.place(x=10, y = 280)

#Жалобы, течение заболевания
label_state = tk.Label(frame2,text = "Жалобы, течение заболевания",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_state.place(x=10, y = 320)

state = tk.Text(height = 4, width = 64, font=("TkMenuFont",10))
state.place(x=10, y = 340)

#Данные обследований
label_observ = tk.Label(frame2,text = "Данные обследований",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_observ.place(x=10, y = 410)

observ = tk.Text(height = 4, width = 64, font=("TkMenuFont",10))
observ.place(x=10, y = 430)

#Текущее лечение
label_treatment = tk.Label(frame2,text = "Текущее лечение",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_treatment.place(x=10, y = 500)

treatment= tk.Text(height = 2, width = 64, font=("TkMenuFont",10))
treatment.place(x=10, y = 520)

#Назначенные препараты
label_drugs = tk.Label(frame2,text = "Назначенные препараты",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_drugs.place(x=10, y = 560)

drugs= tk.Text(height = 2, width = 64, font=("TkMenuFont",10))
drugs.place(x=10, y = 580)

#Процедуры, операции
label_procedure = tk.Label(frame2,text = "Процедуры, операции",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_procedure.place(x=10, y = 620)

procedure= tk.Text(height = 2, width = 64, font=("TkMenuFont",10))
procedure.place(x=10, y = 640)

#Дополнительная информация
label_extra_info = tk.Label(frame2,text = "Дополнительная информация",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",10))

label_extra_info.place(x=10, y = 680)

extra_info= tk.Text(height = 2, width = 64, font=("TkMenuFont",10))
extra_info.place(x=10, y = 700)



#Commit command
conn.commit()
#Close connection
conn.close()

window.mainloop()

