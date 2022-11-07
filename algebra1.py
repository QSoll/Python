import random
import os
import requests
from tkinter import *

# para abrir a janela tkinter escrever o codigo from tkinter import # e abaixo e depois na barra inferior, clicar em terminal e digitar python nomearquivo.py e dar enter e vai abrir a tela
#menu_inicial = Tk()
#menu_inicial.title("Sol Morcillo")
#menu_inicial.mainloop()

menu_inicial = Tk()
menu_inicial.title("Sol Morcillo")
menu_inicial.mainloop()


erros=0
sorteado=random.randrange(0,100)
jogador=int(input("Tente adivinhar o número que estou pensando.Digite um número de 0 a 100:"))
while(sorteado!=jogador):
    os.system('cls')
    if(sorteado>jogador):
        print("Errou, o número é maior.")
    elif(sorteado<jogador):
        print("Errou, o número é menor.")
    erros+=1
    jogador=int(input("Digite outro número: "))
print("Número " + str(jogador) + ", você acertou em " + str(erros+1) + " tentativas")