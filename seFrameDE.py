from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def seFrameDE(frame):

    def get(): 

        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        var = "SELECT * FROM employees;"
        cursor.execute(var)
        data = cursor.fetchall()

        for ind_data in data:
            if str(e_n.get()) == ind_data[0] :
                var = "DELETE FROM employees WHERE Name = %s"%(e_n.get(), )
                cursor.execute(var)
                db.commit()
                messagebox.showinfo("Delete", "Data deleted successfully...")

            else:
                messagebox.Dialog("ERROR", "Data not found")

        db.close()


    l1 = Label(frame, text="Name: ").grid(column=0, row=0, padx=30, pady=15)
    e_n = Entry(frame, width=50)
    e_n.grid(column=1, row=0, padx=30, pady=15)

    b1 = Button(frame, text="Delete", command=get).grid(column=1, row=2, padx=30, pady=15)
    frame.bind('<Return>', lambda event: get())