'''Questão número 1º'''
vogais = ['a','e','i','o','u']

letra = str(input('Digite uma letra:')).lower().strip()[0]

if letra in vogais:
    print('É vogal')
else:
    print('Não é vogal')



'''Questão número 2º'''
produto = {}

while True:
    item = str(input('Digite um produto:'))
    valor = int(input('Valor: '))
    decisao = str(input('Quer continuar [s/n]: ')).lower().strip()[0]

    produto[item] = valor

    if decisao == 'n':
        break
    else:
        continue

quantidade = produto.values()


menor_numero = float('inf')
produto_mais_barato = ''
for numeros in quantidade:
    if menor_numero > numeros:
        menor_numero = numeros
        produto_mais_barato = item
print(f"O produto mais barato é {produto_mais_barato}, custá apenas {menor_numero} Reais")



'''Questão 3º'''   
numero1 = int(input('Digite o numero: '))
numero2 = int(input('Digite o numero: '))
numero3 = int(input('Digite o numero: '))
    
if numero1 < numero2 and numero1 < numero3:
    if numero2 < numero3:
        print(numero1,numero2,numero3)
    else:
        print(numero1,numero3,numero2)
elif numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
        print(numero2,numero1,numero3)
    else:
        print(numero2,numero3,numero1)
elif numero3 < numero1 and numero3 < numero2:
    if numero1 < numero2:
        print(numero3,numero1,numero2)
    else:
        print(numero3,numero2,numero1)
else:
    print('todos são iguais')

'''Questão 4º'''
turno = str(input('Digite seu turno M/para matutino V/Vespetino N/Noturno: ')).upper().strip()[0]

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa Noite')
else:
    print('Turno inexistente!')

'''Questão 5º'''
semana = ['Domingo', 'Segunda - Feira', 'Terça - Feira','Quarta - Feira', 'Quinta - Feira', 'Sexta - Feira', 'Sabádo']
numero = int(input('Digite o número do dia da semana, Domingo[0]/ Segunda[1] e etc... :'))

if numero == 0:
    print(semana[numero])
elif numero == 1:
    print(semana[numero])
elif numero == 2:
    print(semana[numero])
elif numero == 3:
    print(semana[numero])
elif numero == 4:
    print(semana[numero])
elif numero == 5:
    print(semana[numero])
elif numero == 6:
    print(semana[numero])
else:
    print('dia nao existente')

'''Questões 5º'''
n1 = float(input('Digite nota1: '))
n2 = float(input('Digite nota2: '))

media = (n1 + n2) / 2

if media >= 9.0 and media <= 10:
    print('Conceito A')

elif media >= 7.5 and media <= 9.0:
    print('Conceito B')

elif media >= 6.0 and media <= 7.5:
    print('Conceito C')

elif media >= 4.0 and media <= 6.0:
    print('Conceito D')

elif media >= 4.0:
    print('Conceito E')

else:
    print('Reprovado')

'''Questão 6º'''
ano = int(input('ano: '))
ano1 = ano % 4
ano2 = ano % 100
ano3 = ano % 400

if ano1 == 0 and ano2 == 0 and ano3 == 0:
    print('ele é bissexto!')
elif ano1 == 0 and ano2 > 0:
    print('ele é um ano bissexto!')
elif ano3 > 0:
    print('ele não é ano bissexto!')


'''Questão 7º'''
def menu():
    print('\n[1] Adição')
    print('[2] Subtração')
    print('[3] Multiplicação')
    print('[4] Divisão')
    print('[5] Exponeciação')



def entra_de_dados():
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    return n1,n2
opcao = 's'

while opcao == 's':
    menu()
    escolha = int(input('Opção:'))

    if escolha == 1:

        n1, n2 = entra_de_dados()        
        solucao = n1 + n2
    elif escolha == 2:

        n1, n2 = entra_de_dados() 
        solucao = n1 - n2
    elif escolha == 3:

        n1, n2 = entra_de_dados() 
        solucao = n1 * n2
    elif escolha == 4:

        n1, n2 = entra_de_dados()
        solucao = n1 / n2
    elif escolha == 5:

        n1, n2 = entra_de_dados()
        solucao = n1 ** n2
    else:
        print('Escolha errada!!')

    print(solucao,'é o resultado')

    opcao = input('Deseja continuar [s/n]: ').lower().strip()[0]

e_par = solucao % 2 == 0

if e_par :
    print('É par')
else:
    print('É impar')

if solucao < 0:
    print('Ele é negativo')
elif solucao > 0:
    print('Ele é positivo')

tipo = type(solucao)
print(f'Tipo dele é {tipo}')


'''Questão 8º'''
idade = int(input('Idade: '))
if idade >= 0 and idade <= 150:
    print(f'Sua idade é {idade}')
    print('Os valores aceitáveis devem estar entre 0 e 150.')


'''Questão 9º'''
lista_de_numeros = []
c = 0
total_de_numeros = 0
while c <= 4:
    numero = input('Número:')
    lista_de_numeros.append(numero)
    c += 1
for digitos in lista_de_numeros:

    digito = digitos
    digito = int(digito)

    total_de_numeros += digito
tamanho = len(lista_de_numeros)

media = total_de_numeros/tamanho
print(media)


'''Questão 10º'''
numero = int(input('Verificador de número primo: '))

divisores = 0

for c in range(1, numero + 1):
    if numero % c == 0:
        divisores += 1

if divisores == 2:
    print(f'{numero} é um número primo.')
else:
    print(f'{numero} não é um número primo.')

'''Questão 11º'''
temperaturas = []
c = 0
repeticao = True
while repeticao:
    temperatura = input('Digite a temperatura:')
    temperaturas.append(temperatura)
    c += 1
    opcao = input('Quer adicionar outra? [s/n]:').lower().strip()[0]

    if opcao == 'n':
        repeticao = False
    elif opcao == 's':
        continue
    elif opcao != 'n':
        while opcao != 's':
            opcao = input('Quer adicionar outra? [s/n]:').lower().strip()[0]
            if opcao == 'n':
                repeticao = False
                break

maiores_temperaturas = 0
menores_temperaturas = 0
soma_de_temperaturas = 0
for c, temperatura_ in enumerate(temperaturas):

    temperatura_float = temperatura_
    temperatura_float = float(temperatura_float)
    
    soma_de_temperaturas += temperatura_float
    if c == 1:
        maiores_temperaturas = temperatura_float
        menor_numero_temperaturas = temperatura_float

    if temperatura_float < menores_temperaturas:
        menores_temperaturas = temperatura_float

    elif temperatura_float > maiores_temperaturas:
        maiores_temperaturas = temperatura_float

print(f'\nA maior temperatura foi de: {maiores_temperaturas}°')
print(f'e menor temperatura foi de: {menores_temperaturas}°')
print(f'A média das temperaturas foi de: {soma_de_temperaturas/c}°')

'''Questão 12°'''

saldo = float(input('Digite seu saldo médio autal:'))

if saldo > 0 and saldo <= 200:
    print('Nenhum crédito disponível')
elif saldo > 200 and saldo <= 400:
    saldo_com_credito = saldo * 0.20
    print('Crédito disponível de "20%"')
    print(f'Valor do seu crédito é de {saldo_com_credito:.0f}')
elif saldo > 400 and saldo <= 600:
    saldo_com_credito = saldo * 0.30
    print('Crédito disponível de "30%"')
    print(f'Valor do seu crédito é de {saldo_com_credito:.0f}')
elif saldo > 600:
    saldo_com_credito = saldo * 0.40
    print('Crédito disponível de "40%"')
    print(f'Valor do seu crédito é de {saldo_com_credito:.0f}')
else:
    print('Valor desconhecido')


'''Questão 13º'''
print('INSS')
nome = str(input('Digite seu nome:'))
idade = int(input('Digite sua idade:'))

aposentadoria = 65 - idade
ano_da_aposentadoria = 2024 + aposentadoria

if idade < 65:
    print(f'\n{nome}, você ainda não atingiu a idade necessária para se aposentar.')
    print(f'Você tem {idade} anos, No ano de {ano_da_aposentadoria} você estará apto.')
else:
    print('Você está apto para se aposentar.')


'''Questão 14º'''
valor_hora = float(input("Informe o valor da sua hora de trabalho: R$ "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))


salario_bruto = valor_hora * horas_trabalhadas


if salario_bruto <= 2112.00:
    ir = 0
elif salario_bruto <= 2826.65:
    ir = salario_bruto * 0.075
elif salario_bruto <= 3751.05:
    ir = salario_bruto * 0.15
elif salario_bruto <= 4664.68:
    ir = salario_bruto * 0.225
else:
    ir = salario_bruto * 0.275


desconto_sindicato = salario_bruto * 0.03


fgts = salario_bruto * 0.11

salario_liquido = salario_bruto - (ir + desconto_sindicato)


print(f"Salário Bruto: R$ {salario_bruto:.2f}")
print(f"Desconto do IR: R$ {ir:.2f}")
print(f"Desconto do Sindicato: R$ {desconto_sindicato:.2f}")
print(f"Contribuição ao FGTS: R$ {fgts:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")
