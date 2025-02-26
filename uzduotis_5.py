from tkinter import *

langas = Tk()


def keliamieji_metai():
    atsakymas = ""
    metai = int(laukas.get())
    if metai % 100 == 0:
        if metai % 400 == 0:
            atsakymas = "keliamieji metai"
        else:
            atsakymas = "nekeliamieji metai"
    elif metai % 4 == 0:
        atsakymas = "keliamieji metai"
    else:
        atsakymas = "nekeliamieji metai"
    atsakymas_lange["text"] = laukas.get() + " yra " + atsakymas


remelis1 = Frame(langas)
remelis2 = Frame(langas)
uzrasas = Label(remelis1, text="iveskite metus")
laukas = Entry(remelis1)
mygtukas = Button(remelis1, text="Patvirtini", command=keliamieji_metai)
atsakymas_lange = Label(remelis2)

remelis1.pack()
remelis2.pack(side=BOTTOM)
uzrasas.pack(side=LEFT)
laukas.pack(side=LEFT)
mygtukas.pack()
atsakymas_lange.pack()

langas.mainloop()
