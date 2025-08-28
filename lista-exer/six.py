""" 
Questão 6. Escreva um programa que calcule a média aritmética de duas notas válidas (intervalo [0..10]).
Seu programa não pode aceitar notas que não estejam no intervalo e deve informar a mensagem 
"Nota inválida" quando inserir uma nota que não respeite o intervalo. Ainda, ao concluir o cálculo
e exibir a média calculada, você deve exibir a mensagem: Novo cálculo (1.sim 2.não)?, 
solicitando ao usuário que informe um código (1 ou 2) indicando se ele deseja ou não executar
o algoritmo novamente. Se for informado o código 1, então deve ser repetida a execução de todo
o algoritmo para permitir um novo cálculo, caso contrário, ele deve ser encerrado.

[Dados de entrada] [Saída esperada]
-2 (nota 1)         Nota inválida
7 (nota 1)
9 (nota 2)          8 (média)
Novo cálculo?(1.sim 2.não)?

1
6 (nota 1)
12 (nota 2)         Nota inválida
-3 (nota 2)         Nota inválida
10 (nota 2)         8 (média)

Novo cálculo?(1.sim 2.não)?
2
"""
while True: 
    
    while True:
        try:
            nota1 = float(input("Nota 1: "))
            if 0 <= nota1 <= 10:
                break 
            else:
                print("Nota inválida")
        except ValueError:
            print("Nota inválida")
            
    while True:
        try:
            nota2 = float(input("Nota 2: "))
            if 0 <= nota2 <= 10:
                break
            else:
                print("Nota inválida")
        except ValueError:
            print("Nota inválida")

    media = (nota1 + nota2) / 2
    print(f"{media} (média)")
    
    try:
        decisao = int(input("Novo cálculo?(1.sim 2.não)? "))
        if decisao == 2:
            break
    except ValueError:
        break