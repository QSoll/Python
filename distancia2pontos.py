import math

x1 = float(input('Digite o ponto x1:'))
x2 = float(input('Digite o ponto x2:'))

y1 = float(input('Digite o ponto y1:'))
y2 = float(input('Digite o ponto y2:'))

dxy = math.sqrt ((x1-x2)**2) + ((y1-y2)**2)

if (dxy == 10 or dxy > 10):
    print("Longe")
else:
    print ("Perto")