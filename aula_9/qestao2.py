gatilho = 0.8
lista_vendedores = [0.8, 0.9, 0.5, 1.2, 1.0] 


result_soma = 0

for vendedor in lista_vendedores:
    result_soma += vendedor

media = result_soma / len(lista_vendedores)

maior_vendedor = 0
menor_vendedor = 500

if media >= gatilho:
    print("Campanha válida! Equipe de parabéns!!")
    for vendedor in lista_vendedores:
        if vendedor > maior_vendedor:
            maior_vendedor = vendedor
        elif vendedor < menor_vendedor:
            menor_vendedor =  vendedor
        else:
            print("O vendedor é igual, perdeu a vez!")

else:
    print("A campanha foi um desastre!")


print(f"O maior vendedor, vendeu {maior_vendedor}")
print(f"O menor vendedor, vendeu {menor_vendedor}")




