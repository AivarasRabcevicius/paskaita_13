from tkinter import Tk, Label, Entry, Button, Frame, LEFT, BOTTOM, Menu, StringVar, X
from tkinter.constants import SUNKEN

langas = Tk()

tekstas = StringVar()


def spausdinti():
    ivesta = laukas.get()
    tekstas.set(ivesta)
    labas["text"] = "Labas " + tekstas.get() + "!"
    status["text"] = "Sukurta"


def trinti():
    labas["text"] = ""
    status["text"] = "Isvalyta"


def atkurti():
    labas["text"] = "Labas " + tekstas.get() + "!"
    status["text"] = "Atkurta"


def iseiti():
    langas.destroy()


remelis1 = Frame(langas)
remelis2 = Frame(langas)

status = Label(langas, bd=2, relief=SUNKEN)
meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

uzrasas = Label(remelis1, text="iveskite varda")
laukas = Entry(remelis1)
mygtukas = Button(remelis1, text="Patvirtinti", command=spausdinti)
labas = Label(remelis2)

langas.bind("<Return>", lambda event: spausdinti())
langas.bind("<Escape>", lambda event2: iseiti())

remelis1.pack()

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=trinti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

uzrasas.pack(side=LEFT)
laukas.pack(side=LEFT)
mygtukas.pack(side=LEFT)
labas.pack(side=BOTTOM)
status.pack(side=BOTTOM, fill=X)
remelis2.pack(side=BOTTOM)
langas.mainloop()
