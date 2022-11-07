numero = int(input("Qual o fatorial de: ") )

resultado=1
valor = 1

while valor <= numero:
    resultado *= valor
    valor += 1

print(resultado)
