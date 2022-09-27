'''Seja criativo ao desenvolver este programa.

a. Crie uma lista de convidados para um jantar em sua casa, com pelo menos 5 celebridades.

lista_amigos = ["Neymar", "Vini Jr", "Bruxo", "Fenomeno", "Messi"]
b. Envie um convite para cada uma dessas pessoas. Com a mesma mensagem e nome personalizado.


c. Sabendo que uma dessas pessoas não poderá ir ao seu jantar, você deverá enviar novos
convites. Imprima o nome das pessoas que não poderão comparecer.

d. Modifique sua lista, substitua os desistentes por novos convidados.

e. Exiba um novo convite para cada pessoa que continua presente em sua lista.'''

convidados = ["Neymar", "Vini Jr", "Bruxo", "Fenomeno", "Messi"]

for nome in convidados:
    mensagem = f"Bora pra balada, {nome}!"
    print(mensagem)
    

#Quem não poderá ir
print("Bruxo: Infelizmente não posso estar no mesmo ambiente que o Fenomeno")
print("Fenomeno: Infelizmente não posso estar no mesmo ambiente que o Bruxo")

#Novos convidados

convidados[2] = "Matheus"
convidados[0] = "Michel"

for nome in convidados:
    mensagem = f"Bora pra balada, {nome}!"
    print(mensagem)
    
   