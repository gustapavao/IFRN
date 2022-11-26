Número = int(input("Informe um Número Inteiro"))
Resto = Número % 2
print("\n**************************\n")
if Resto == 0 and Número > 0:
    print ("O número é Par e Positivo")
if Resto == 0 and Número < 0:
    print ("O número é Par e Negativo")
if Resto == 1 and Número > 0:
    print ("O número é Ímpar e Positivo")
if Resto == 1 and Número < 0:
    print ("O número é Ímpar e Negativo")
if Número == 0:
    print ("O número é Nulo")