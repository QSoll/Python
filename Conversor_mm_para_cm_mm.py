from sys import maxsize
from tkinter import *
from turtle import width

# converter mm para cm e m
def calcular():
    Mm = float(textbox1.get())
    Cm = Mm / 10
    M = Mm / 1000
    result.set(str(round (Cm, 2)) + " centímetros (cm)")
    final.set(str(round (M, 4)) + " metros (m)")

# guid
root = Tk()
root.title("Sol Morcillo - CONVERSOR")
root.iconbitmap("favicon.ico")
root.minsize(350,373)
root.maxsize(350,373)

final = StringVar ()
result = StringVar ()

img=PhotoImage(file="logo_volteSempre.fw.png")

#widgets mm para cm e m
label1 = Label(root, text="MILÍMETROS (mm)  para:\nCentímetros (cm)  e  metros (m)\nUsar ponto no lugar da vírgula", width=40,  height=4, bg="yellow", font="Arial 12", padx="5", pady="5")
textbox1 = Entry(root, justify=CENTER, font="Arial 12")
button1 = Button (root,text="Converter", command=calcular, bg="yellow", font="Arial 12", pady="3")
label_resulta = Label(root, textvariable=result, font="Arial 20", pady="20")
label_resultado = Label(root, textvariable=final, font="Arial 20", pady="20")



#widgets  fahrenheit para celsius
#label3 = Label(root, text="Fahrenheit para Graus Celsius", width=40,  height=4, bg="orange", font="Arial 12", padx="5", pady="5")
#textbox2 = Entry(root, justify=CENTER, font="Arial 12")
#button2 = Button (root,text="Converter", command=converter, bg="yellow", font="Arial 12", pady="3")
#label_resulta = Label(root, textvariable=result, font="Arial 20", pady="20")

label_2 = Label(root, image=img)
#label3 = Label (root, text="Volte sempre !!!", font="Arial 12", padx="132", pady="20", bg="DeepSkyBlue")

#layouts

label1.grid()
textbox1.grid()
button1.grid()
label_resulta.grid()
label_resultado.grid()
label_2.grid()

#label3.grid()
#textbox2.grid()
#button2.grid()
#label_resulta.grid()

#label3.grid()






root.mainloop()