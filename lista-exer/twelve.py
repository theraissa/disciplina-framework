"""
Questão 12. Faça um algoritmo que leia valores inteiros e positivos e cujo último valor é -1. 
Dentre os valores lidos, o algoritmo deve mostrar:

a) o menor valor dentre os maiores que 100 e menores que 1000
b) a média desses valores dentre os maiores que 100 e menores que 1000
c) a soma desses valores dentre os maiores que 100 e menores que 1000
d) a soma de todos os valores lidos
e) o menor valor digitado
f) o maior valor digitado
g) total de valores digitados

O valor -1 não deve ser considerado; Além disso, se nenhum valor digitado estiver dentro do
intervalo de 100 para e 1000, o algoritmo deve imprimir uma mensagem para o usuário explicando
que não foi digitado valores para esses cálculos.
"""

soma_total = 0
total_valores = 0
menor_geral = float('inf') 
maior_geral = float('-inf')

soma_intervalo = 0
total_intervalo = 0
menor_intervalo = float('inf')

while True:
    try:
        valor = int(input("Digite um valor inteiro positivo (-1 para encerrar): "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        continue 

    if valor == -1:
        break

    soma_total += valor
    total_valores += 1
    
    if valor < menor_geral:
        menor_geral = valor
    if valor > maior_geral:
        maior_geral = valor

    if 100 < valor < 1000:
        soma_intervalo += valor
        total_intervalo += 1
        
        if valor < menor_intervalo:
            menor_intervalo = valor

print("\n--- Resultados ---")
if total_intervalo > 0:
    media_intervalo = soma_intervalo / total_intervalo
    print(f"a) O menor valor entre 100 e 1000: {menor_intervalo}")
    print(f"b) A média dos valores entre 100 e 1000: {media_intervalo:.2f}")
    print(f"c) A soma dos valores entre 100 e 1000: {soma_intervalo}")
else:
    print("Nenhum valor digitado estava no intervalo entre 100 e 1000.")

if total_valores > 0:
    print(f"d) A soma de todos os valores lidos: {soma_total}")
    print(f"e) O menor valor digitado: {menor_geral}")
    print(f"f) O maior valor digitado: {maior_geral}")
    print(f"g) Total de valores digitados: {total_valores}")
else:
    print("Nenhum valor foi digitado.")