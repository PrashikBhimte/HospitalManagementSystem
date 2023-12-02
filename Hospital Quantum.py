import tkinter as tk
import mysql.connector as ms
from tkinter import messagebox

db = ms.connect(
    host="localhost",
    user="root",
    password="yash29",
    database="ppmd"
)

cursor = db.cursor()

loginsuccessfully = False

def getLoginDetails() :
    global loginsuccessfully

    cursor.execute("SELECT * FROM LOGIN")
    loginDetails = cursor.fetchone()

    username = loginDetails[0]
    password = loginDetails[1]

    if username == str(userName.get())  and password == str(passWord.get()):
        messagebox.showinfo("Message", "Login Successfully......")
        loginsuccessfully = True
        window.destroy()
    else:
        messagebox.showinfo("Message", "Wrong credentials")
        loginsuccessfully = False
 
window = tk.Tk()
window.title('Login....')
window.geometry('330x130')
    
tk.Label(window, text='UserName : ').grid(column= 0, row= 0, padx=40, pady=20)
userName = tk.Entry(window)
userName.grid(column= 1, row= 0)
tk.Label(window, text='Password : ').grid(column= 0, row= 1, padx=40, pady=2)
passWord = tk.Entry(window, show="*")
passWord.grid(column= 1, row= 1)

submit = tk.Button(window, text='Submit', width=10, height=1, command=getLoginDetails)
submit.grid(column=1, row=2, pady=10)

window.bind('<Return>', lambda event: getLoginDetails())

window.mainloop()

if loginsuccessfully:
    import mainscreen

db.close()