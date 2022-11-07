segundos = input("Por favor, entre com o número de segundos que deseja converter: ")
totalSegundos = int(segundos)

a = totalSegundos // (3600 * 24)
seg1 = totalSegundos % (3600 * 24)

b = seg1 // 3600                 
seg2 = seg1 % 3600
         
c = seg2 // 60
              
d = seg2 % 60  

print(a, "dias, ", b, "horas, ", c, "minutos e", d, "segundos.")