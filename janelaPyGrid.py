from tkinter import *
from tkinter.tix import COLUMN
from turtle import width

janela=Tk() # abre a janela
janela.title("Sol Morcillo")
janela.iconbitmap(default="favicon.ico")
janela["bg"]= "IndianRed"

largura = 600
altura = 350
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()

label_1 = Label (janela,
    text = " Frase 1 ",
    bg="yellow",
    fg="black",
    font="Verdana 18"
    )

label_2 = Label (janela,
    text = " Mensagem 2",
    bg="white",
    fg="red",
    font="Arial 20 bold italic"
    )
label_3 = Label(janela,text="Texto3", bg="red")

btn1 = Button (janela, text="botao1")
btn2 = Button (janela, text="botao2")
btn3 = Button (janela, text="botao3")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)
label_3.grid(row=0, column=2)

btn1.grid(row=1,column=0)
btn2.grid(row=1,column=1)
btn3.grid(row=1,column=2)

janela.mainloop() # fecha a janela


