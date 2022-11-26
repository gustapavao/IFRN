a = int(input('Primeiro lado: '))
b = int(input('Segundo  lado: '))
c = int(input('Terceiro lado: '))
if (a + b < c) or (a + c < b) or (b + c < a):
    print('Não é um triangulo')
elif (a == b) and (a == c):
    print('O triângulo é Equilatero')
elif (a==b) or (a==c) or (b==c):
    print ('O triângulo é Isósceless')
else:
    print ('O triângulo é Escaleno')