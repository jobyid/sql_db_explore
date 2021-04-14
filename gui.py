from tkinter import *
import database_funcs as dbf

def set():
    d = my_entry.get()
    print(type(d))
    se = my_entry2.get()
    print(se)
    if se.split()[0].lower() == "select":
        res = dbf.pandas_select_query(se, d, True)
        resVar.set(res)
    elif se.split()[0].lower() == "create":
        res = dbf.create_table(d, se)
        resVar.set(res)
    var.set("Good-Bye Cruel World")
    print(type(my_entry.get()))
    print(my_entry2.get())

root = Tk()
root.geometry("600x600")

frame = Frame(root)
frame.pack()

var = StringVar()
var.set("What SQL do you want to run?")
resVar = StringVar()
resVar.set("")
label = Label(frame, textvariable=var)
label.pack()
my_entry = Entry(frame, width=200)
my_entry.insert(0, 'db path')
my_entry.pack(padx=5, pady=5)

my_entry2 = Entry(frame, width=150)
my_entry2.insert(0, 'sentence')
my_entry2.pack(padx=5, pady=5)

button = Button(frame, text="run", command=set)
button.pack()
label2 = Label(frame, textvariable=resVar)
label2.pack()
root.mainloop()
