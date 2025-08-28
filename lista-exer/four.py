"""
Questão 4. Foi realizada uma pesquisa de algumas características físicas da população 
de uma determinada região, a qual coletou os seguintes dados referentes a 
cada habitante para serem analisados:

a) sexo (masculino e feminino)
b) cor dos olhos (azuis, verdes ou castanhos)
c) cor dos cabelos (louros, castanhos, pretos)
d) idade
e) altura
f) peso

Ao final, a média da idade dos participantes, a média do peso e altura dos seus habitantes
e a porcentagem de pessoas do sexo feminino, a porcentagem de pessoas do masculino. As pessoas
possuem olhos verdes e cabelos louros. A cada iteração deve ser perguntado ao usuário se desejar
continuar ou não. Os resultados deverão ser apresentados apenas quando o usuário não desejar 
inserir mais dados
"""

soma_idades = 0
soma_pesos = 0
soma_alturas = 0
total_pessoas = 0

total_feminino = 0
total_masculino = 0
total_olhos_verdes_cabelos_louros = 0

continuar = 'S'

while continuar.upper() == 'S':
    print("\n--- Inserir dados do habitante ---")
    
    sexo = input("Sexo (M/F): ").upper()
    if sexo == 'F':
        total_feminino += 1
    elif sexo == 'M':
        total_masculino += 1
    else:
        print("Sexo inválido. Por favor, insira M ou F.")
        continue

    olhos = input("Cor dos olhos (azuis/verdes/castanhos): ").lower()
    cabelos = input("Cor dos cabelos (louros/castanhos/pretos): ").lower()

    try:
        idade = int(input("Idade: "))
        soma_idades += idade
    except ValueError:
        print("Idade inválida. Por favor, insira um número.")
        continue

    try:
        altura = float(input("Altura: "))
        soma_alturas += altura
    except ValueError:
        print("Altura inválida. Por favor, insira um número.")
        continue

    try:
        peso = float(input("Peso: "))
        soma_pesos += peso
    except ValueError:
        print("Peso inválido. Por favor, insira um número.")
        continue
        
    total_pessoas += 1

    if olhos == 'verdes' and cabelos == 'louros':
        total_olhos_verdes_cabelos_louros += 1

    continuar = input("Deseja inserir mais um habitante? (S/N): ")

print("\n--- Resultados da Pesquisa ---")
if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas
    media_peso = soma_pesos / total_pessoas
    media_altura = soma_alturas / total_pessoas

    porcentagem_feminino = (total_feminino / total_pessoas) * 100
    porcentagem_masculino = (total_masculino / total_pessoas) * 100
    porcentagem_olhos_verdes_cabelos_louros = (total_olhos_verdes_cabelos_louros / total_pessoas) * 100
    
    print(f"Média da idade dos participantes: {media_idade:.2f} anos")
    print(f"Média do peso: {media_peso:.2f} kg")
    print(f"Média da altura: {media_altura:.2f} m")
    print(f"Porcentagem de pessoas do sexo feminino: {porcentagem_feminino:.2f}%")
    print(f"Porcentagem de pessoas do sexo masculino: {porcentagem_masculino:.2f}%")
    print(f"Porcentagem de pessoas com olhos verdes e cabelos louros: {porcentagem_olhos_verdes_cabelos_louros:.2f}%")
else:
    print("Nenhum dado foi inserido para análise.")