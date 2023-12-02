from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def seFrameSE(frame):

    l1 = Label(frame, text="Name: ")
    l1.grid(column=0, row=0, padx=30, pady=15)
    e_n = Entry(frame, width=50)
    e_n.grid(column=1, row=0, padx=30, pady=15)

    def get(): 

        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        var = "SELECT * FROM EMPLOYEES;"
        cursor.execute(var)
        data = cursor.fetchall()
        
        var = ('Name', 'Sex', 'Age', 'Phone Number', 'Address', 'Email', 'Date of Birth', 'Joining date', 'Desgination', 'Salary')
        found = False
        found_data = ()

        for ind_data in date:
            if str(e_n_n.get()) == ind_data[0] :
                found = True
                found_data = ind_data

        if found :
            l1.grid_remove()
            e_n.grid_remove()
            b1.grid_remove()
            for i in range(0, 10):
                x = var[i] + " :                             " + str(found_data[i])
                Label(frame, text=x, font=('Areal', 15)).pack(padx=250, pady=5)

        else:
            messagebox.Dialog("ERROR", "Data not found")

        db.close()

    b1 = Button(frame, text="Search", command=get)
    b1.grid(column=1, row=2, padx=30, pady=15)

    frame.bind('<Return>', lambda event: get())