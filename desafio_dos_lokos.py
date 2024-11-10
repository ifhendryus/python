"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""
cpf = '746.824.890-70'
primerios, segundo, terceiro = cpf.split('.')
novo1, novo2 = terceiro.split('-') 
novo = novo1 + novo2
numeros = primerios + segundo + novo


numero_soma = 0
c = 10
for numero in numeros:
    numero1 = numero
    numero1 = int(numero1)
    numero_resultado = numero1 * c
    numero_soma = numero_soma + numero_resultado
    c -= 1
    if c == 2:
        break
numero_soma *= 10
numero_soma = numero_soma % 11

if numero_soma > 9:
    print('o resultado é zero')
else:
    print(numero_soma)


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""

cpf = '746.824.890-70'
primerios, segundo, terceiro = cpf.split('.')
novo1, novo2 = terceiro.split('-') 
novo = novo1 + novo2
numeros = primerios + segundo + novo


numero_soma = 0
c = 11
for numero in numeros:
    numero1 = numero
    numero1 = int(numero1)
    numero_resultado = numero1 * c
    numero_soma = numero_soma + numero_resultado
    c -= 1
    if c == 1:
        break
numero_soma *= 10
numero_soma = numero_soma % 11

print(numero_soma)
# if numero_soma > 9:
#     print('o resultado é zero')
# else:
#     print(numero_soma)
