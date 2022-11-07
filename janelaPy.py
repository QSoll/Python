from tkinter import *

janela=Tk() # abre a janela
janela.title("Sol Morcillo")
janela.iconbitmap(default="favicon.ico")
janela["bg"]= "IndianRed"
janela.geometry("250x250+100+100") # tamLargura x tamAltura + posicaox + posiçaoy
janela.minsize(550,550)
janela.maxsize(500,300)
janela.resizable(True, True)

# janela.state("zoomed")  # janela aparece maximizada

#botão
#btn=Button(janela,text="Executar")
#btn.pack() #para o botao aparecer

def cmd_Click(mensagem): # este codigo def tem que ficar antes do command
    print(mensagem)

    #primeiro botao
btn_Executar=Button (janela, text="Executar", command=lambda: cmd_Click("Mensagem de executar"))
btn_Executar.pack()

    #segundo botao
btn_Comprar=Button (janela, text="Comprar", command=lambda: print("ok"))
btn_Comprar.pack()




janela.mainloop() # fecha a janela


