"""
Questão 9. As cidades da região metropolitana se reuniram para discutir quais os dados 
dos habitants seriam coletados para realizar uma pesquisa. Os dados informados por cada
habitante na pesquisa serão: idade, sexo (1. Feminino 2. Masculinho) e salário. 
Faça um programa que leia os dados e informe ao final:

a) média de salário dos habitantes;
b) maior idade;
c) menor idade;
d) maior salário;
e) maior salário das pessoas do sexo feminino;
f) menor idade do sexo masculino;
g) quantas pessoas do sexo feminino possuem salário maior R$500;
h) quantos habitantes são do sexo masculino e tem idade entre 15 e 50 anos;
i) quantos habitantes tem idade entre 18 e 65 anos e possuem salário acima de R$1000.

Encerre a entrada de dados quando for digitada uma idade negativa.
"""
soma_salarios = 0
total_habitantes = 0

maior_idade = -1
menor_idade = float('inf') 

maior_salario = -1
maior_salario_feminino = -1

menor_idade_masculino = float('inf')

mulheres_salario_alto = 0
homens_idade_media = 0
trabalhadores_experientes = 0

print("Início da pesquisa. Digite uma idade negativa para encerrar.")

while True:
    try:
        idade = int(input("\nIdade: "))
    except ValueError:
        print("Entrada inválida. Digite um número inteiro para a idade.")
        continue
        
    if idade < 0:
        break
        
    try:
        sexo = int(input("Sexo (1.Feminino 2.Masculino): "))
        salario = float(input("Salário: "))
    except ValueError:
        print("Entrada inválida. Digite 1 ou 2 para sexo e um número para o salário.")
        continue
    
    total_habitantes += 1
    soma_salarios += salario
    
    if idade > maior_idade:
        maior_idade = idade
    if idade < menor_idade:
        menor_idade = idade
        
    if salario > maior_salario:
        maior_salario = salario
        
    if sexo == 1 and salario > maior_salario_feminino:
        maior_salario_feminino = salario
        
    if sexo == 2 and idade < menor_idade_masculino:
        menor_idade_masculino = idade
        
    if sexo == 1 and salario > 500:
        mulheres_salario_alto += 1
        
    if sexo == 2 and 15 <= idade <= 50:
        homens_idade_media += 1
        
    if 18 <= idade <= 65 and salario > 1000:
        trabalhadores_experientes += 1

print("\n--- Resultados da Pesquisa ---")
if total_habitantes > 0:
    media_salarios = soma_salarios / total_habitantes
    print(f"a) Média de salário dos habitantes: R${media_salarios:.2f}")

    print(f"b) Maior idade: {maior_idade} anos")
    print(f"c) Menor idade: {menor_idade} anos")
    print(f"d) Maior salário: R${maior_salario:.2f}")

    if maior_salario_feminino != -1:
        print(f"e) Maior salário do sexo feminino: R${maior_salario_feminino:.2f}")
    else:
        print("e) Nenhum dado do sexo feminino foi coletado.")

    if menor_idade_masculino != float('inf'):
        print(f"f) Menor idade do sexo masculino: {menor_idade_masculino} anos")
    else:
        print("f) Nenhum dado do sexo masculino foi coletado.")

    print(f"g) Mulheres com salário > R$500: {mulheres_salario_alto}")
    print(f"h) Homens com idade entre 15 e 50 anos: {homens_idade_media}")
    print(f"i) Pessoas com idade entre 18 e 65 e salário > R$1000: {trabalhadores_experientes}")
else:
    print("Nenhum dado válido foi inserido para a pesquisa.")