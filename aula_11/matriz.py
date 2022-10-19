#Exemplo 1

'''matriz = [
    [[4, 5, 6], [7, 8, 9], [10, 11, 12]],
    [2, 4 ,6],
    [4, 8, 12]


]

print(matriz[0])
print(matriz[1][1])
print(matriz[2][2])

# Exemplo 2 usando dois FOR

matriz = [
    [4, 5, 6], 
    [2, 4 ,6],
    [4, 8, 12]
]

for linha in matriz:
    for coluna in linha:
        print(coluna)'''


#Exemplo 3 - for selecionando uma lista expecífica 

matriz = [
    (1, 2, 3), 
    [2, 4 ,6],
    [4, 8, 12]
]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])

#Exemplo 4


