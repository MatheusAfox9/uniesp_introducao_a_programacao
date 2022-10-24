
n = input("Insira um número: ")

numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '1', '2', '2', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1', '2', '3', '4', '5', '6', '7', '8', '9', '1']

numeros.sort()

rep = 0

for i in range(0, len(numeros)-1):
    if(numeros[i] == numeros[i+1]):
        rep += 1
    else:
        print(numeros[i],",",rep+1)
        rep=0    





'''opcao = input("Digite um número: ")

for i in numeros:
    if opcao == numeros.count'''


