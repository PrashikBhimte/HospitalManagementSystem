from tkinter import *
import mysql.connector as ms
from tkinter import messagebox

def seFrameAP(frame):
    def getAP():

        db = ms.connect(
            host="localhost",
            user="root",
            password="yash29",
            database="ppmd"
        )

        cursor = db.cursor()

        Name = str(name.get())
        patient_id = 5
        Sex = str(sex.get())
        Age = age.get()
        Bloodgroup = str(bloodgroup.get())
        Phonenumber = phonenumber.get()
        Email = str(email.get())
        Address = str(address.get())
        Dob = str(dob.get())
        Admitdate = str(admitdate.get())
        Discharge = str(discharge.get())

        sql = "INSERT INTO patients (Name, sex, age, blood_group, phone_number, email, address, admit_date, discharge_date, date_of_birth) \n VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        var = (Name, Sex, Age, Bloodgroup, Phonenumber, Email, Address, Admitdate, Discharge, Dob)
        cursor.execute(sql, var)
        db.commit()

        messagebox.showinfo("Submit", "Data successfully added.")

        db.close()


    Label(frame, text="Name: ").grid(column=0, row=0, padx=30, pady=15)
    name =  Entry(frame, width=50)
    name.grid(column=1, row=0, padx=30, pady=15)
    
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


    Button(frame, text="Submit", width=10, command=getAP).grid(column=1, row=10)
    frame.bind('<Return>', lambda event: getAP())