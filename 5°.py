Ano = int(input("Informe um ano entre 1900 e 2100:"))
Bissexto = Ano % 4
if ((Bissexto == 0) and (Ano <= 2100) and (Ano >= 1900)):
    print ("O ano é Bissexto")
if ((Ano > 2100) or (Ano < 1900)):
    print ("O ano não está entre 1900 e 2100")
if Bissexto != 0:
    print ("O ano não é Bissexto")