# Crie um programa em Python que solicite um número do usuário, depois some este número com 1357, multiplique por 8, divida por 5 e eleve ao quadrado.

#numero = int(input("Digite um número: "))
#numero2 = numero + 1357
#numero3 = numero2 * 8
#numero4 = numero3 / 5
#numero5 = numero4 ** 2
#print(f"A some é: {numero2}, A multiplicação é: {numero3}, A divisão é: {numero4}, A elevação é: {numero5}.")

numero = int(input("Digite um número: "))
resultado = ((((numero + 1357)*8)/5)**2)
print(f"{resultado : .2f}")