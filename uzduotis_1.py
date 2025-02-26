from tkinter import Tk, Label, Entry, Button, Frame, LEFT, BOTTOM


def spausdinti():
    ivesta = laukas.get()
    labas["text"] = "Labas " + ivesta + "!"


langas = Tk()

remelis1 = Frame(langas)
remelis2 = Frame(langas)
uzrasas = Label(remelis1, text="iveskite varda")
laukas = Entry(remelis1)
mygtukas = Button(remelis1, text="Patvirtinti", command=spausdinti)
labas = Label(remelis2)

langas.bind("<Return>", lambda event: spausdinti())

remelis1.pack()
remelis2.pack(side=BOTTOM)
uzrasas.pack(side=LEFT)
laukas.pack(side=LEFT)
mygtukas.pack(side=LEFT)
labas.pack(side=BOTTOM)
langas.mainloop()
