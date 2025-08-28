"""
Questão 2. Faça um programa que imprima os números entre um intervalo 
definido pelo usuário e ao final mostre a soma dos valores pares

"""

int_1, int_2 = map(int, input("Escolha dois números separados por um espaço: ").split())

soma = 0
menor = min(int_1, int_2)
maior = max(int_1, int_2)

for i in range(menor, maior + 1):
    if i % 2 == 0:
        soma += i
        
print(f"Soma dos valores pares entre o intervalo de {int_1} a {int_2} é {soma}")