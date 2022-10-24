clubes = ["Palmeiras", "Flamengo", "Real Madrid", "Manchester City", "Liverpool", "Chelsea", "Corinthians", "Barcelona", "Santos", "São Paulo"]

opcao = input("Digite o nome de um clube: ")

for i in range(len(clubes)):
    if opcao == clubes[i]:
        print(f"Achei, o clube é o {clubes[i]}")
    else:
        print("Não achei")     