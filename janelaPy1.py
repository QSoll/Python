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
#posicionamento no centro da tela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2
#geometry
#janela.geometry ("%dx%d+%d+%d" % (largura, altura, posx, posy))
#print(largura_screen, altura_screen)


label_1 = Label (janela,
    text = " Frase 1 \n Frase 2 \n Frase 3 ",
    bg="yellow",
    fg="black",
    font="Verdana 18",
    width=20,
    height=5,
    bd=1, relief="solid", #bd =bordawidth e relief tem o solid, o ridge, o groove, o flat, raised, sunken (afundado)
    #se todas as labels tiverem a mesma borda, por ex 1, é só escrever border=1 antes de todas as labels
    anchor=CENTER  #N alinha a ferase a norte, S ao sul, L a leste, Se a sudeste e assim por diante e center alinha ao centro
   
    )


label_2 = Label (janela,
    text = " Mensagem 2 \n Mensagem 2 \n Mensagem 3 ",
    bg="white",
    fg="red",
    font="Arial 20 bold italic",
    padx=10, pady=20, #padding
    justify = CENTER
    )

cmd = Button(janela, text = "Executar")

label_1.grid(row=0, column=0)
label_2.grid(row=0, column=1)

#label_1.pack()
#label_2.pack()
#cmd.pack()

janela.mainloop() # fecha a janela


