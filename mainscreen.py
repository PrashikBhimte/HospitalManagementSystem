import tkinter as tk
import seFrameAE, seFrameAP, seFrameDE, seFrameDP, seFrameSE, seFrameSP, seFrameUE, seFrameUP
from tkinter import messagebox

def AP():
    frameAP.grid(column=1, row=0)
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def SP():
    frameAP.grid_remove()
    frameSP.grid(column=1, row=0)
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def UP():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid(column=1, row=0)
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def DP():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid(column=1, row=0)
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def AE():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid(column=1, row=0)
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def SE():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid(column=1, row=0)
    frameUE.grid_remove()
    frameDE.grid_remove()
    first_frame.grid_remove()

def UE():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid(column=1, row=0)
    frameDE.grid_remove()
    first_frame.grid_remove()

def DE():
    frameAP.grid_remove()
    frameSP.grid_remove()
    frameUP.grid_remove()
    frameDP.grid_remove()
    frameAE.grid_remove()
    frameSE.grid_remove()
    frameUE.grid_remove()
    frameDE.grid(column=1, row=0)
    first_frame.grid_remove()

def EX():
    var = messagebox.askquestion("Exit", "Do you want to exit?")
    print(var)
    if var == "yes":
        root.destroy()
    

def mainframe(frame):
    tk.Button(frame, text="Add new Patient", width=30, height=1, command=AP).pack(padx=30, pady=15)
    tk.Button(frame, text="Show patient Details", width=30, height=1, command=SP).pack(padx=30, pady=15)
    tk.Button(frame, text="Update patient Details", width=30, height=1, command=UP).pack(padx=30, pady=15)
    tk.Button(frame, text="Delete patient Details", width=30, height=1, command=DP).pack(padx=30, pady=15)
    tk.Button(frame, text="Add new employee", width=30, height=1, command=AE).pack(padx=30, pady=15)
    tk.Button(frame, text="Show employee Details", width=30, height=1, command=SE).pack(padx=30, pady=15)
    tk.Button(frame, text="Update employeeq Details", width=30, height=1, command=UE).pack(padx=30, pady=15)
    tk.Button(frame, text="Delete employeeq Details", width=30, height=1, command=DE).pack(padx=30, pady=15)
    tk.Button(frame, text="Exit", width=30, height=1, command=EX).pack(padx=30, pady=15)

root = tk.Tk()
root.title("Hospital Management System PPMD")
root.geometry('990x560')
frame = tk.Frame(root, bg='blue')
frame.grid(column=0, row=0)
    
mainframe(frame)
    
frameAP = tk.Frame(root)
seFrameAP.seFrameAP(frameAP)

frameSP = tk.Frame(root)
seFrameSP.seFrameSP(frameSP)

frameUP = tk.Frame(root)
seFrameUP.seFrameUP(frameUP)

frameDP = tk.Frame(root)
seFrameDP.seFrameDP(frameDP)

frameAE = tk.Frame(root)
seFrameAE.seFrameAE(frameAE)

frameSE = tk.Frame(root)
seFrameSE.seFrameSE(frameSE)

frameUE = tk.Frame(root)
seFrameUE.seFrameUE(frameUE)

frameDE = tk.Frame(root)
seFrameDE.seFrameDE(frameDE)

first_frame = tk.Frame(root)
tk.Label(first_frame, text="Welcome To PPMD application.", font=("Arial", 25)).pack(padx=150)
first_frame.grid(column=1, row=0)

root.mainloop()