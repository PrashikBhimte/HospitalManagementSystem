from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def seFrameDP(frame):

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

        for ind_data in data:
            if str(p_n.get()) == ind_data[0] :
                sql = "DELETE FROM patients \nWHERE Name = %s"
                var = (p_n.get(), )

                cursor.execute(sql, var)
                db.commit()

                messagebox.showinfo("Delete", "Data deleted successfully...")

            else:
                messagebox.showinfo("ERROR", "Data not found")

        db.close()


    l1 = Label(frame, text="Name: ").grid(column=0, row=0, padx=30, pady=15)
    p_n = Entry(frame, width=50)
    p_n.grid(column=1, row=0, padx=30, pady=15)

    b1 = Button(frame, text="Delete", command=get).grid(column=1, row=2, padx=30, pady=15)
    frame.bind('<Return>', lambda event: get())