import tkinter as tk
import sqlite3

#Main window
window = tk.Tk()
window.title("Ввод данных врача")
window.eval("tk::PlaceWindow . center")

#Create a frame on main window
frame1 = tk.Frame(window, width = 500, height = 600, bg = "#3d6466")
frame1.grid(row = 0, column = 0)
frame1.pack_propagate(False)

#Общая информация
gen_label = tk.Label(frame1, text = "Общая информация",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",14))
gen_label.pack()


#ФИО
label_fio = tk.Label(frame1,text = "ФИО",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_fio.place(x=10, y = 40)

entry_fio = tk.Entry(frame1, width = 80)
entry_fio.place(x=10, y = 65)
 
#Телефон
label_tel = tk.Label(frame1,text = "Телефон",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_tel.place(x=10, y = 90)

entry_tel = tk.Entry(frame1, width = 80)
entry_tel.place(x=10, y = 115)

#Специализация
label_spc = tk.Label(frame1,text = "Специализация",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_spc.place(x=10, y = 140)

entry_spc = tk.Entry(frame1, width = 80)
entry_spc.place(x=10, y = 165)


#Подробная информация 
gen_label_2 = tk.Label(frame1, text = "Подробная информация",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",14))
gen_label_2.place(x=145, y = 190)

#Дата рождения
label_birth = tk.Label(frame1,text = "Дата рождения",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_birth.place(x=10, y = 220)

entry_birth = tk.Entry(frame1, width = 30)
entry_birth.place(x=10, y = 245)

#Специальность
label_spc_2 = tk.Label(frame1,text = "Специальность",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_spc_2.place(x=300, y = 220)

entry_spc_2 = tk.Entry(frame1, width = 30)
entry_spc_2.place(x=300, y = 245)


#ВУЗ
label_vuz = tk.Label(frame1,text = "ВУЗ",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_vuz.place(x=10, y = 270)

entry_vuz = tk.Entry(frame1, width = 30)
entry_vuz.place(x=10, y = 295)

#Номер диплома
label_dip = tk.Label(frame1,text = "Номер диплома",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_dip.place(x=300, y = 270)

entry_dip = tk.Entry(frame1, width = 30)
entry_dip.place(x=300, y = 295)


#Год окончания ВУЗа
label_end = tk.Label(frame1,text = "Год окончания ВУЗа",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_end.place(x=10, y = 320)

entry_end = tk.Entry(frame1, width = 30)
entry_end.place(x=10, y = 345)


#Ученая степень
label_phd = tk.Label(frame1,text = "Ученая степень",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_phd.place(x=300, y = 320)

entry_phd = tk.Entry(frame1, width = 30)
entry_phd.place(x=300, y = 345)


#Дополнительная информация
label_ext = tk.Label(frame1,text = "Доп. информация",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_ext.place(x=10, y = 370)

entry_ext = tk.Entry(frame1, width = 30)
entry_ext.place(x=10, y = 395)

#id
label_id = tk.Label(frame1,text = "ID",
                     bg = "#3d6466",
                     fg = "#FFF8DC",
                     font = ("TkMenuFont",12))

label_id.place(x=300, y = 370)

entry_id = tk.Entry(frame1, width = 30)
entry_id.place(x=300, y = 395)

#Создание функции ввода данных врача
def submit_doc():
    #Connect to database
    conn = sqlite3.connect('med_app_db.db')
    #Create a cursor
    cur = conn.cursor()

    #Get values to insert
    id_doc = entry_id.get()
    fio = entry_fio.get()
    tel = entry_tel.get()
    spc = entry_spc.get()

    d_of_birth = entry_birth.get()
    spc_2 = entry_spc_2.get()
    vuz = entry_vuz.get()
    diploma = entry_dip.get()
    end_of_vuz = entry_end.get()
    phd = entry_phd.get()
    extra_info = entry_ext.get()

    #Values to insert into specialists table
    spec_insert = [id_doc,fio,spc,tel]

    #Values to insert into specialists_data table
    spec_data_insert = [id_doc,d_of_birth,spc_2,vuz,diploma,end_of_vuz,phd,extra_info]

    #Insert Data into Tables
    cur.execute("""INSERT INTO specialists VALUES(?,?,?,?)""",spec_insert)
    cur.execute("""INSERT INTO specialists_data VALUES(?,?,?,?,?,?,?,?)""",spec_data_insert)
    
    #Commit command
    conn.commit()
    #Close connection
    conn.close()

    #Clear the entry forms
    entry_id.delete(0, 'end')
    entry_ext.delete(0, 'end')
    entry_phd.delete(0, 'end')
    entry_dip.delete(0, 'end')
    entry_end.delete(0, 'end')
    entry_vuz.delete(0,'end')
    entry_spc_2.delete(0, 'end')
    entry_birth.delete(0,'end')
    entry_spc.delete(0, 'end')
    entry_tel.delete(0, 'end')
    entry_fio.delete(0, 'end')

#Кнопка ввода данных
button_entry_doc = tk.Button(text = "ВВЕСТИ", width = 30, bg = "#53868B",
                     fg = "#F0F8FF",
                     font = ("TkMenuFont",16),command = submit_doc)
button_entry_doc.place(x=65, y = 450, height = 80)




window.mainloop()
