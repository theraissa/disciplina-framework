"""
Questão 10. Faça um algoritmo que leia 3 notas obtidas por 5 alunos. Calcule a média de notas de
todos os alunos usando a seguinte fórmula: 

Média por aluno (MA) = (N1 + N2 + N3) / 3
Mídia Geral = (MA1 + MA2 + MA3 + MA4 + MA5)/5

A seguir mostre a média e o conceito do aluno baseado na tabela:

Média                   Conceito
9,0 ou acima de 9,0         A
entre 7,5 e 8,9             B
entre 6,0 e 7,4             C
entre 4,0 e 5,9             D
abaixo de 4,0               E

Ao final mostre a mensagem de acordo com a média da turma.
"""
soma_das_medias = 0

for i in range(1, 6):
    print(f"\n--- Aluno {i} ---")
    
    try:
        n1 = float(input("Digite a nota N1: "))
        n2 = float(input("Digite a nota N2: "))
        n3 = float(input("Digite a nota N3: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite números para as notas.")
        continue 
    
    media_aluno = (n1 + n2 + n3) / 3
    soma_das_medias += media_aluno
    
    if media_aluno >= 9.0:
        conceito = "A"
    elif media_aluno >= 7.5:
        conceito = "B"
    elif media_aluno >= 6.0:
        conceito = "C"
    elif media_aluno >= 4.0:
        conceito = "D"
    else:
        conceito = "E"
        
    print(f"Média do aluno: {media_aluno:.2f}")
    print(f"Conceito do aluno: {conceito}")
media_geral = soma_das_medias / 5

print("\n--- Resultados Finais ---")
print(f"Média Geral da Turma: {media_geral:.2f}")