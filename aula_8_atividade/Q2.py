import math


x1 = float(input("Digite o valor de X1: "))
y1 = float(input("Digite o valor de Y1: "))
x2 = float(input("Digite o valor de X2: "))
y2 = float(input("Digite o valor de Y2: "))

D = math.sqrt((x1-y1)*2 + (x2 - y2)*2)

print(f"A distância destes pontos {x1},{y1},{x2} e {y2} é de: {D}")
