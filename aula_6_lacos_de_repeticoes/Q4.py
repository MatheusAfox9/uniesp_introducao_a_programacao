''' Faça um programa que receba um número e que calcule e mostre a tabuada desse número..'''

numero = int(input("Digite o número: " ))

for numero in range(1,11):
    print(f"Tabuada do {numero}")

for numero2 in range(1,11):
    resultado = numero * numero2
    print(f"{numero} x {numero2} = {resultado}") 
