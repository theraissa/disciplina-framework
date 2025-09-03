"""
Questão 11. Fazer um algoritmo que leia para cada um dos funcionários, os seguintes dados:
matrícula, nome, sexo, salário bruto, número de dependentes, ano de nascimento, 
ano de ingresso na empresa. Observe as seguintes regras: 

* é acrescido ao salário líquido R$14,00 de salário família por dependente (isento de tributos);
* desconto de 12% no salário bruto para o INSS;
* o desconto do imposto de renda sobre o salário bruto segue a tabela abaixo:

Faixa salarial                  Desconto

R$ 0 a R$ 1.500                 Isento
R$ 1.500,01 a R$ 2.700          15%
R$ 2.700,01 a R$ 4.700          27,5%
Acima de R$ 4700                35%

Calcular e escrever:

a) o nome do funcionário (pode ser homem ou mulher) mais antigo da empresa;
b) o nome da funcionária de maior salário líquido;
c) a porcentagem de funcionários do sexo masculino com idade menor que 27 anos e salário menor que
d) R$ 1.700,00;
e) a soma de todos os salários líquidos dos funcionários da empresa

"""
import datetime

total_funcionarios = 0
ano_atual = datetime.datetime.now().year
nome_funcionario_mais_antigo = ""
ano_ingresso_mais_antigo = ano_atual
nome_funcionaria_maior_salario = ""
maior_salario_liquido_feminino = -1
homens_jovens_salario_baixo = 0
soma_salarios_liquidos = 0

while True:
    print("\n--- Inserir dados do funcionário ---")
    
    matricula = input("Matrícula (digite 'sair' para encerrar): ")
    if matricula.lower() == 'sair':
        break
        
    try:
        nome = input("Nome: ")
        sexo = input("Sexo (M/F): ").upper()
        salario_bruto = float(input("Salário Bruto: "))
        dependentes = int(input("Número de Dependentes: "))
        ano_nascimento = int(input("Ano de Nascimento: "))
        ano_ingresso = int(input("Ano de Ingresso na Empresa: "))
    except ValueError:
        print("Entrada inválida. Tente novamente.")
        continue
    
    total_funcionarios += 1
    desconto_inss = salario_bruto * 0.12
    
    if 0 <= salario_bruto <= 1500:
        desconto_ir = 0
    elif 1500.01 <= salario_bruto <= 2700:
        desconto_ir = salario_bruto * 0.15
    elif 2700.01 <= salario_bruto <= 4700:
        desconto_ir = salario_bruto * 0.275
    else:
        desconto_ir = salario_bruto * 0.35
    
    salario_familia = dependentes * 14
    salario_liquido = salario_bruto - desconto_inss - desconto_ir + salario_familia
    soma_salarios_liquidos += salario_liquido

    if ano_ingresso < ano_ingresso_mais_antigo:
        ano_ingresso_mais_antigo = ano_ingresso
        nome_funcionario_mais_antigo = nome

    if sexo == 'F' and salario_liquido > maior_salario_liquido_feminino:
        maior_salario_liquido_feminino = salario_liquido
        nome_funcionaria_maior_salario = nome
    
    idade = ano_atual - ano_nascimento
    if sexo == 'M' and idade < 27 and salario_bruto < 1700:
        homens_jovens_salario_baixo += 1

print("\n--- Resultados Finais da Pesquisa ---")
if total_funcionarios > 0:
    print(f"a) O nome do funcionário mais antigo da empresa é: {nome_funcionario_mais_antigo}")
    
    if nome_funcionaria_maior_salario:
        print(f"b) O nome da funcionária de maior salário líquido é: {nome_funcionaria_maior_salario}")
    else:
        print("b) Nenhum dado de funcionário do sexo feminino foi coletado.")
        
    porcentagem_homens_jovens = (homens_jovens_salario_baixo / total_funcionarios) * 100
    print(f"c) A porcentagem de funcionários do sexo masculino com idade < 27 anos e salário < R$1.700 é: {porcentagem_homens_jovens:.2f}%")
    
    print(f"d) A soma de todos os salários líquidos dos funcionários é: R${soma_salarios_liquidos:.2f}")
else:
    print("Nenhum dado de funcionário foi inserido para a análise.")