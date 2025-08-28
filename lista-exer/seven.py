"""
Questão 7. Algum tempo atrás, foi realizada uma pesquisa em Porto Alegre, com um número desconhecido 
de pessoas. De cada entrevistado(a) foram escolhidos os seguintes dados:

a) clube de preferência (1-Grêmio; 2-Internacional; 3-Outros);
b) cidade de origem (0-Porto Alegre; 1-Outras).

Deseja-se saber:
a) número de torcedores por clube;
b) número de pessoas nascidas em Porto Alegre que não torcem por nenhum dos dois primeiros clubes;
c) número de pessoas entrevistadas.
Para inserir os dados, o tempo fornecido deve ser igual a zero
"""

num_entrev = 0
gremio = 0
inter = 0
outro_clube = 0
poa_n_torcem = 0
porto_alegre = 0
outra_cidade = 0
continuar = 'S'

while continuar.upper() == 'S':
    print("\n--- Inserir dados da entrevista ---")
    clube_pref = int(input("clube de preferência (1-Grêmio; 2-Internacional; 3-Outros) "))
    
    if (clube_pref == 1):
        gremio += 1
    elif (clube_pref == 2):
        inter += 1
    elif (clube_pref == 3):
        outro_clube += 1
    else:
        print("Informe o seu clube de preferência")
        continue    
    
    cidade_origem = int(input("cidade de origem (0-Porto Alegre; 1-Outras) "))
    
    if (cidade_origem == 0 and clube_pref == 3):
        poa_n_torcem += 1
    elif (cidade_origem == 0):
        porto_alegre += 1
    elif (cidade_origem == 1):
        outra_cidade += 1
    else:
        print("Informe sua cidade de origem")
        continue
    
    num_entrev += 1
    continuar = input("Deseja inserir mais um habitante? (S/N): ")

print("\n--- Resultados da Pesquisa ---")
if num_entrev > 0:
    print("\nnúmero de torcedores por clube:")
    print(f"- Grêmio: {gremio}")
    print(f"- Internacional: {inter}")
    print(f"- Outros: {outro_clube}")
    
    print(f"\nnúmero de pessoas nascidas em Porto Alegre que não torcem por nenhum dos dois primeiros clubes: {poa_n_torcem}")
    print(f"número de pessoas entrevistadas: {num_entrev}")
else:
    print("Nenhum dado foi inserido para análise.")