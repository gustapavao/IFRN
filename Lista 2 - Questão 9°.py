a = int(input('Primeiro lado: '))
b = int(input('Segundo  lado: '))
c = int(input('Terceiro lado: '))

if a**2 < b**2 + c**2:
    print ('É um Triângulo acutângulo.')
elif a**2 == b**2 + c**2:
    print ('É um Triângulo retângulo.')
elif a**2 > b**2 + c**2:
    print ('É um Triângulo obtusângulo.')