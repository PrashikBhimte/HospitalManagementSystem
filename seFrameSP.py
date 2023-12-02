from tkinter import *
import mysql.connector as ms
from tkinter import messagebox

def seFrameSP(frame):

    l1 = Label(frame, text="Name: ")
    l1.grid(column=0, row=0, padx=30, pady=15)
    p_n = Entry(frame, width=50)
    p_n.grid(column=1, row=0, padx=30, pady=15)

    def get(): 
        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        var = "SELECT * FROM PATIENTS;"
        cursor.execute(var)
        data = cursor.fetchall()

        var = ('Name', 'patient_id', 'Sex', 'Age', 'Bloodgroup', 'Phonenumber', 'Email', 'Address', 'Admitdate', 'Discharge', 'Dob')
        found = False
        found_data = ()

        for ind_data in data:
            if str(p_n.get()) == ind_data[0] :
                found = True
                found_data = ind_data

        if found == True :
            l1.grid_remove()
            p_n.grid_remove()
            b1.grid_remove()
            for i in range(0, 11):
                x = var[i] + " :                             " + str(found_data[i])
                Label(frame, text=x, font=('Areal', 15)).pack(padx=250, pady=5)

        else:
            messagebox.showinfo("ERROR", "Data not found")
        
        db.close()

    b1 = Button(frame, text="Search", command=get)
    b1.grid(column=1, row=2, padx=30, pady=15)

    frame.bind('<Return>', lambda event: get())