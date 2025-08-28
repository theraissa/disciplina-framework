"""
Questão 5. Escreva um algoritmo para repetir a leitura de uma senha até que ela seja válida. 
Para cada leitura de senha incorreta informada, escreva a mensagem "SENHA INVÁLIDA". 
Quanto à senha incorreta informada, deve ser impressa a mensagem "ACESSO PERMITIDO" e o 
algoritmo é encerrado, mostrando quantas vezes a senha foi digitada. 
Considere que a senha correta tem o valor 2014.

[Dados de entrada] [Saída esperada]
22000 SENHA INVÁLIDA
2010 SENHA INVÁLIDA
2022 SENHA INVÁLIDA
1111 SENHA INVÁLIDA
"""

senha_correta = 2014
senha_digitada = 0  
tentativas = 0

while senha_digitada != senha_correta:

    try:
        senha_digitada = int(input())
    except ValueError:
        print("SENHA INVÁLIDA")
        continue  
        
    tentativas += 1
    
    if senha_digitada != senha_correta:
        print("SENHA INVÁLIDA")
print("ACESSO PERMITIDO")
print(f"Total de tentativas: {tentativas}")