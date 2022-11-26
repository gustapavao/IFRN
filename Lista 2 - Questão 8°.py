# Calcular as Raízes de uma Equação do 2º Grau
a = int(input('Informe o valor de a: '))
b = int(input('Informe o valor de b: '))
c = int(input('Informe o valor de c: '))
d = (b**2 - 4*a*c)
x1= -b+ (d**1/2)/2*a
x2= -b-(d**1/2)/2*a
if a==0:
    print ('Se a=0, não é uma equação do 2° Grau')
elif d<0:
    print('Delta é menor que 0.')
elif d==0:
    print (f"As raízes são {x1}")
else:
    print (f"As raízes são {x1} e {x2}")