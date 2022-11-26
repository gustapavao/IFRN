x = int(input("Informe a coordenada de X: "))
y = int(input("Informe a coordenada de Y: "))
if x == 0 and y == 0:
    quadrante = 0
elif x == 0 or y==0:
    quadrante = -1
elif x>0:
    if y>0:
        quadrante= 1
    elif y<0:
        quadrante=4
elif x<0:
    if y>0:
        quadrante=2
    elif y < 0:
        quadrante = 3

print ("O ponto (%d, %d) pertence ao quadrante %d."%(x,y,quadrante))
