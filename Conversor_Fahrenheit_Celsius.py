from sys import maxsize
from tkinter import *
from turtle import width

# converter celsius para fahrenheit - formula: F = 5/9 *(C - 32)
#def calcular():
#    C = float(textbox1.get())
#    F = ((9 * C) /5) + 32
#    final.set(str(round (F, 1)) + " Fahrenheit")

# converter fahrenheit para celsius- formula: 5*
def converter():
    F = float(textbox2.get())
    C = (F - 32) * 5/9
    result.set(str(round (C, 1)) + " Graus celsius")

# guid
root = Tk()
root.title("Sol Morcillo - CONVERSOR")
root.iconbitmap("favicon.ico")
root.minsize(350,298)
root.maxsize(350,298)

#final = StringVar ()
result = StringVar ()

img=PhotoImage(file="logo_volteSempre.fw.png")

#widgets celsius para fahrenheit
#label1 = Label(root, text="GRAUS CELSIUS  para  FAHRENHEIT\nUsar ponto no lugar da vírgula", width=40,  height=4, bg="yellow", font="Arial 12", padx="5", pady="5")
#textbox1 = Entry(root, justify=CENTER, font="Arial 12")
#button1 = Button (root,text="Converter", command=calcular, bg="yellow", font="Arial 12", pady="3")
#label_resultado = Label(root, textvariable=final, font="Arial 20", pady="20")


#widgets  fahrenheit para celsius
label3 = Label(root, text="FAHRENHEIT para GRAUS CELSIUS\nUsar ponto no lugar da vírgula", width=40,  height=4, bg="yellow", font="Arial 12", padx="5", pady="5")
textbox2 = Entry(root, justify=CENTER, font="Arial 12")
button2 = Button (root,text="Converter", command=converter, bg="yellow", font="Arial 12", pady="3")
label_resulta = Label(root, textvariable=result, font="Arial 20", pady="20")

label_2 = Label(root, image=img)
#label3 = Label (root, text="Volte sempre !!!", font="Arial 12", padx="132", pady="20", bg="DeepSkyBlue")

#layouts

#label1.grid()
#textbox1.grid()
#button1.grid()
#label_resultado.grid()
#label_2.grid()

label3.grid()
textbox2.grid()
button2.grid()
label_resulta.grid()

label_2.grid()


root.mainloop()