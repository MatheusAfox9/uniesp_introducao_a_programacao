'''matriz = [
    [0.0, 0.1, 0.2]
    [1.0, 1,1, 2.2]
]'''


# Solução 1
'''mtz = [
    [78, 90, 100],
    [56, 77, 93],
    [10, 4, 73]
]

print(mtz[0][0])
print(mtz[1][1])
print(mtz[2][2])'''


matriz = [
    [78, 90, 100, 98, 7],
    [56, 72, 93, 150, 4],
    [10, 4, 73, 200, 4],
    [5, 7, 3, 15, 4],
    [0, 4, 3, 0, 2]

]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        if l == c:
            print(matriz[l][c])

        if(matriz[l][c] %2) ==0:
            print(f"{matriz[l][c]} -> É par!")
        else:
            print(f"{matriz[l][c]} -> É ímpar!")


       
