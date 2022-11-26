peso = int(input("Informe o seu peso:"))
altura = int(input("Informe a sua altura:"))
IMC = peso / (altura**2)
if IMC > 18.5:
    print ("Você está abaixo do peso")
if ((IMC < 18.4) and (IMC > 25)):
    print ("Você está no peso normal")
if ((IMC < 25) and (IMC > 30)):
    print ("Você está no sobrepeso")
if ((IMC < 30) and (IMC > 35)):
    print ("Você está na obesidade grau I")
if ((IMC < 35) and (IMC > 40)):
    print ("Você está na obesidade grau II")
if IMC < 40:
    print ("Você está na obesidade grau III ou Mórbida")