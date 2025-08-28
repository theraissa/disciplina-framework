"""
Questão 8. A Federação Gaúcha de Futebol contratou você para desenvolver um programa que colete estatísticas
sobre os resultados de vários GRENAIS. Escreva um algoritmo para ler o número de gols marcados pelo Inter
e o número de gols marcados pelo GRÊMIO em um GRENAIS, exibindo o nome do time vencedor ou
a palavra "EMPATE". Imediatamente após o resultado, escreva a mensagem: Novo GRENAL 1. Sim 2. Não?.
Se a resposta for 1, o algoritmo deve ser executado novamente, solicitando o número de gols marcados
pelos times em uma nova partida; caso contrário, deve ser encerrado, exibindo o resultado final.

a) Quantos GRENAIS fizeram parte das estatísticas?
b) O número de vitórias do Inter
c) O número de vitórias do Grêmio
d) O número de empates
e) Qual time venceu mais GRENAIS ou se não houve vencedor

"""

vitorias_inter = 0
vitorias_gremio = 0
empates = 0
total_grenais = 0

while True:
    try:
        gols_inter = int(input("Gols do Inter: "))
        gols_gremio = int(input("Gols do Grêmio: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue 

    total_grenais += 1

    if gols_inter > gols_gremio:
        print("Inter venceu!")
        vitorias_inter += 1
    elif gols_gremio > gols_inter:
        print("Grêmio venceu!")
        vitorias_gremio += 1
    else:
        print("EMPATE")
        empates += 1
    
    try:
        continuar = int(input("Novo GRENAL? 1. Sim 2. Não?: "))
        if continuar == 2:
            break  
        elif continuar != 1:
            print("Opção inválida. O programa será encerrado.")
            break
    except ValueError:
        print("Opção inválida. O programa será encerrado.")
        break
        
print(f"\nTotal de Grenais: {total_grenais}")
print(f"Vitórias do Inter: {vitorias_inter}")
print(f"Vitórias do Grêmio: {vitorias_gremio}")
print(f"Empates: {empates}")

if vitorias_inter > vitorias_gremio:
    print("O Inter venceu mais Grenais.")
elif vitorias_gremio > vitorias_inter:
    print("O Grêmio venceu mais Grenais.")
else:
    print("Não houve vencedor, Inter e Grêmio empataram em número de vitórias.")