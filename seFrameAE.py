from tkinter import *
from tkinter import messagebox
import mysql.connector as ms

def seFrameAE(frame):

    db = ms.connect(
        host="localhost",
        user="root",
        password="yash29",
        database="ppmd"
    )

    cursor = db.cursor()

    def getAE():
        Name = str(nameE.get())
        Sex = str(sexE.get())
        Age = str(ageE.get())
        Phonenumber = str(phonenumberE.get())
        Address = str(addressE.get())
        Email = str(emailE.get())
        Dob = str(dobE.get())
        Jioningdate = str(jioningdateE.get())
        Designatio = str(designatioE.get())
        Salary = str(salaryE.get())

        var = "INSERT INTO EMPLOYEES VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"%(Name, Sex, Age, Phonenumber, Address, Email, Dob, Jioningdate, Designatio, Salary)
        cursor.execute(var)
        db.commit()

    Label(frame, text="Name: ").grid(column=0, row=0, padx=30, pady=15)
    nameE =  Entry(frame, width=50)
    nameE.grid(column=1, row=0, padx=30, pady=15)
    
    sexE = StringVar()
    Label(frame, text="Sex:").grid(column=0, row=1)
    male_radio = Radiobutton(frame, text="Male", variable=sexE, value="Male")
    male_radio.grid(column=1, row=1)
    female_radio = Radiobutton(frame, text="Female", variable=sexE, value="Female")
    female_radio.grid(column=2, row=1)

    Label(frame, text="Age: ").grid(column=0, row=2, padx=30, pady=15)
    ageE =  Entry(frame, width=50)
    ageE.grid(column=1, row=2, padx=30, pady=15)

    Label(frame, text="Phone Number: ").grid(column=0, row=3, padx=30, pady=15)
    phonenumberE =  Entry(frame, width=50)
    phonenumberE.grid(column=1, row=3, padx=30, pady=15)

    Label(frame, text="Email: ").grid(column=0, row=4, padx=30, pady=15)
    emailE =  Entry(frame, width=50)
    emailE.grid(column=1, row=4, padx=30, pady=15)

    Label(frame, text="Address: ").grid(column=0, row=5, padx=30, pady=15)
    addressE =  Entry(frame, width=50)
    addressE.grid(column=1, row=5, padx=30, pady=15)

    Label(frame, text="Date of Birth: ").grid(column=0, row=6, padx=30, pady=15)
    dobE =  Entry(frame, width=50)
    dobE.grid(column=1, row=6, padx=30, pady=15)

    Label(frame, text="Joining date: ").grid(column=0, row=7, padx=30, pady=15)
    jioningdateE =  Entry(frame, width=50)
    jioningdateE.grid(column=1, row=7, padx=30, pady=15)

    Label(frame, text="Designation: ").grid(column=0, row=8, padx=30, pady=15)
    designationE =  Entry(frame, width=50)
    designationE.grid(column=1, row=8, padx=30, pady=15)

    Label(frame, text="Salary: ").grid(column=0, row=9, padx=30, pady=15)
    salaryE =  Entry(frame, width=50)
    salaryE.grid(column=1, row=9, padx=30, pady=15)

    Button(frame, text="Submit", width=10, command=getAE).grid(column=1, row=10)

    db.close()