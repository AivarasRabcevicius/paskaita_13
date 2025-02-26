from tkinter import Tk, Label, Entry, Button, Frame, LEFT, BOTTOM, Menu, StringVar

langas = Tk()

tekstas = StringVar()


def spausdinti():
    ivesta = laukas.get()
    tekstas.set(ivesta)
    labas["text"] = "Labas " + tekstas.get() + "!"


def trinti():
    labas["text"] = ""


def atkurti():
    labas["text"] = "Labas " + tekstas.get() + "!"


def iseiti():
    langas.destroy()


remelis1 = Frame(langas)
remelis2 = Frame(langas)

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)

uzrasas = Label(remelis1, text="iveskite varda")
laukas = Entry(remelis1)
mygtukas = Button(remelis1, text="Patvirtinti", command=spausdinti)
labas = Label(remelis2)

langas.bind("<Return>", lambda event: spausdinti())

remelis1.pack()
remelis2.pack(side=BOTTOM)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Isvalyti", command=trinti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Iseiti", command=iseiti)

uzrasas.pack(side=LEFT)
laukas.pack(side=LEFT)
mygtukas.pack(side=LEFT)
labas.pack(side=BOTTOM)
langas.mainloop()