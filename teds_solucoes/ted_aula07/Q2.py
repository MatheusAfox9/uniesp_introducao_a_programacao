#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = 2022
ano_nascimento = int(input("Em que ano você nasceu? "))

idade_eleicao = ano_atual - ano_nascimento

if idade_eleicao >= 16:
    print ("Você pode votar!")

else:
    print("você não pode votar")