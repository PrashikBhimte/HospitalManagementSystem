from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def seFrameUP(frame):

    def upAP():

        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        Name = str(name.get())
        Sex = str(sex.get())
        Age = str(age.get())
        Bloodgroup = str(bloodgroup.get())
        Phonenumber = str(phonenumber.get())
        Email = str(email.get())
        Address = str(address.get())
        Dob = str(dob.get())
        Admitdate = str(admitdate.get())
        Discharge = str(discharge.get())

        sql = "update patients\n set sex = %s, age = %s, blood_group = %s, phone_number = %s, email = %s, address = %s, admit_date = %s, discharge_date = %s, date_of_birth = %s \n where Name = %s"
        var = (Sex, Age, Bloodgroup, Phonenumber, Email, Address, Dob, Admitdate, Discharge, Name)

        cursor.execute(sql, var)
        db.commit()

        messagebox.showinfo("Update", "Data successfully updated...")

        db.close()

    def search():
        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        found = False
        found_data = ()

        var = "select * from patients"
        cursor.execute(var)

        data = cursor.fetchall()

        Name = str(name.get())

        for new_data in data:
            for i in range(0, 11):
                if Name == new_data[0]:
                    found = True
                    found_data = new_data

        if found:
            if found_data[2] == 'Male':
                male_radio.invoke()
            else :
                female_radio.invoke()
            age.insert(END, found_data[3])
            bloodgroup.insert(END, found_data[4])
            phonenumber.insert(END, found_data[5])
            email.insert(END, found_data[6])
            address.insert(END, found_data[7])
            admitdate.insert(END, found_data[8])
            discharge.insert(END, found_data[9])
            dob.insert(END, found_data[10])

        else:
            messagebox.showinfo("Update", "Data not found...")

        db.close()

    Label(frame, text="Name: ").grid(column=0, row=0, padx=30, pady=15)
    name =  Entry(frame, width=50)
    name.grid(column=1, row=0, padx=30, pady=15)

    Button(frame, text="Search", width=10, command=search).grid(column=2, row=0, padx=10, pady=15)
    
    sex = StringVar()
    Label(frame, text="Sex:").grid(column=0, row=1)
    male_radio = Radiobutton(frame, text="Male", variable=sex, value="Male")
    male_radio.grid(column=1, row=1)
    female_radio = Radiobutton(frame, text="Female", variable=sex, value="Female")
    female_radio.grid(column=2, row=1)

    Label(frame, text="Age: ").grid(column=0, row=2, padx=30, pady=15)
    age =  Entry(frame, width=50)
    age.grid(column=1, row=2, padx=30, pady=15)

    Label(frame, text="Blood Group: ").grid(column=0, row=3, padx=30, pady=15)
    bloodgroup =  Entry(frame, width=50)
    bloodgroup.grid(column=1, row=3, padx=30, pady=15)

    Label(frame, text="Phone Number: ").grid(column=0, row=4, padx=30, pady=15)
    phonenumber =  Entry(frame, width=50)
    phonenumber.grid(column=1, row=4, padx=30, pady=15)

    Label(frame, text="Email: ").grid(column=0, row=5, padx=30, pady=15)
    email =  Entry(frame, width=50)
    email.grid(column=1, row=5, padx=30, pady=15)

    Label(frame, text="Address: ").grid(column=0, row=6, padx=30, pady=15)
    address =  Entry(frame, width=50)
    address.grid(column=1, row=6, padx=30, pady=15)

    Label(frame, text="Date of Birth: ").grid(column=0, row=7, padx=30, pady=15)
    dob =  Entry(frame, width=50)
    dob.grid(column=1, row=7, padx=30, pady=15)

    Label(frame, text="Admit Date: ").grid(column=0, row=8, padx=30, pady=15)
    admitdate =  Entry(frame, width=50)
    admitdate.grid(column=1, row=8, padx=30, pady=15)

    Label(frame, text="Discharge Date: ").grid(column=0, row=9, padx=30, pady=15)
    discharge =  Entry(frame, width=50)
    discharge.grid(column=1, row=9, padx=30, pady=15)


    Button(frame, text="Update", width=10, command=upAP).grid(column=1, row=10)
    frame.bind('<Return>', lambda event: upAP())