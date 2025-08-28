"""
Questão 3. Elabore um algoritmo que depois de ler uma sequência de N números 
(N deve ser solicitado pelo usuário), mostre os seguintes resultados:

a) o maior valor
b) o menor valor
c) a soma dos valores
d) a média dos valores
e) quantos números maiores a 20
f) a porcentagem de valores maiores que 10
g) a média dos valores entre 10 e 100
"""

quant = int(input("Informe a quantidade de números: "))

soma = 0
num_maior_20 = 0
contagem_maior_10 = 0
soma_10_100 = 0
quant_10_100 = 0

maior = -float('inf')  
menor = float('inf')  

for i in range(quant):
    number = int(input(f"Número {i+1}: "))
    
    if number > maior:
        maior = number
    if number < menor:
        menor = number
        
    soma += number
    
    if number > 20:
        num_maior_20 += 1
        
    if number > 10:
        contagem_maior_10 += 1
        
    if number >= 10 and number <= 100:
        soma_10_100 += number 
        quant_10_100 += 1

media = soma / quant
por_maior_10 = (contagem_maior_10 / quant) * 100 if quant > 0 else 0
media_10_100 = soma_10_100 / quant_10_100 if quant_10_100 > 0 else 0

print(f"a) O maior valor é: {maior}")
print(f"b) O menor valor é: {menor}")
print(f"c) A soma dos valores é: {soma}")
print(f"d) A média dos valores é: {media:.2f}")
print(f"e) Quantos números são maiores que 20: {num_maior_20}")
print(f"f) A porcentagem de valores maiores que 10 é: {por_maior_10:.2f}%")
print(f"g) A média dos valores entre 10 e 100 é: {media_10_100:.2f}")
