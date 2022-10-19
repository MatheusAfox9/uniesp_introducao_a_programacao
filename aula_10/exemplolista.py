'''frutas = ["Pêra", "Uva", "Maçã", "Kiwi"]

#print(f"Juliana gosta de {frutas[3]}")


#Inserindo novos objetos
frutas.insert(2, "Morango")

# Alterando um objeto por outro
frutas[0] = "Melancia"

print(frutas)
indice_fruta = frutas.index("Melancia")
print(f"O índice da fruta é {indice_fruta}")
del frutas[indice_fruta]
print(frutas)'''

lista_mercado = []

while True:
    op = int(input("1 - Adicionar frutas\n \
                    2 - Remover frutas \n \
                    3 - Lista frutas \n \
                    0 - Sair do programa \n \
                    Digite a opção: "))
    
    if op == 1:
        item = input("Digite um item: ")
        lista_mercado.append(item)

    elif op == 2:
        # Remover objetos da lista
        item = input("Digite o item que será removido:")
        indice_item = lista_mercado.index(item)
        del lista_mercado[indice_item]

    elif op == 3:

        for item in lista_mercado:
            print(item)

    elif op == 0:
        break
