"""
Questão 13. Para evitar erros de digitação de sequências de números de importância fundamental,
como matrícula de um aluno, o CPF do Imposto de Renda, o número de conta bancária, geralmente
se adiciona ao número um dígito verificador. Por exemplo, o CPF 546471429 é usado como 54647142949,
onde 49 são os dígitos verificadores, calculados da seguinte maneira:

Para calcular o (1) digito verificador:

    1. cada um dos nove primeiros algarismos é multiplicado por um peso começando de 10 e diminuindo
    de 1 a cada passo:
        5*10, 4*9, 6*8, 4*7, 7*6, 1*5, 4*4, 2*3, 9*2;

    2. somam-se as parcelas obtidas: S=50+36+48 + 28 +42+5+16+6+ 18 = 249;

    3. calcula-se o digito através da seguinte expressão:
        11- (S% 11) = 11 - (249% 11) = 11 - 7 = 4

    obs. se o resto encontrado for 10 ou 11, o dígito verificador será 0; nos outros casos, o dígito
    verificador é o próprio resto encontrado.

Para calcular o (2°) digito verificador:

    1. cada um dos dez primeiros algarismos é multiplicado por um peso começando de 11 e diminuindo
    de 1 a cada passo:

    2. somam-se as parcelas obtidas:
        55+40+54+32+49+6+20+8+27 + 8 = 299;
    
    3. calcula-se o digito através da seguinte expressão:
        11 - (S% 11) =
        11- (299% 11) = 2
        11- 2=9

obs. se o resto encontrado for 10 ou 11, o dígito verificador será 0; nos outros casos, o dígito
verificador é o próprio resto encontrado.
"""
cpf_base = input("Digite os 9 primeiros dígitos do CPF (ex: 546471429): ")

soma_1 = 0
soma_2 = 0

# --- CÁLCULO DO 1º DÍGITO VERIFICADOR ---
for i in range(9):
    digito = int(cpf_base[i])
    peso = 10 - i
    soma_1 += digito * peso

resto_1 = soma_1 % 11

if resto_1 == 10 or resto_1 == 11:
    digito_verificador_1 = 0
else:
    digito_verificador_1 = 11 - resto_1

# --- CÁLCULO DO 2º DÍGITO VERIFICADOR ---
cpf_10digitos = cpf_base + str(digito_verificador_1)

for i in range(10):
    digito = int(cpf_10digitos[i])
    peso = 11 - i
    soma_2 += digito * peso

resto_2 = soma_2 % 11

if resto_2 == 10 or resto_2 == 11:
    digito_verificador_2 = 0
else:
    digito_verificador_2 = 11 - resto_2

print(f"O 1º dígito verificador é: {digito_verificador_1}")
print(f"O 2º dígito verificador é: {digito_verificador_2}")
print(f"O CPF completo com os dígitos verificadores é: {cpf_base}{digito_verificador_1}{digito_verificador_2}")