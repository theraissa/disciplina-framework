"""
Questão 1. Faça um programa que mostre a soma dos valores pares e o produto dos valores pares, 
considerando que o intervalo de 1 até um valor informado pelo usuário.

"""

number = int(input("Escolha um número: "))
soma = 0
produto = 1

for n in range(1, number + 1):
    if (n % 2 == 0):
        soma += n
        produto *= n

print(f"A soma dos números pares no intervalo é: {soma}")
print(f"O produto dos números pares no intervalo é: {produto}")