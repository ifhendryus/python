

while True:
    import os
    os.system('cls')
    numero1 = int(input('Primeiro valor: '))
    operador = input('Digite o operador [ex: + - * / ]: ')
    numero2 = int(input('Segundo valor: '))

    if operador in '+':
        resultado = numero1 + numero2
    elif operador in '-':
        resultado = numero1 - numero2
    elif operador in '*':
        resultado = numero1 * numero2
    elif operador in '/':
        resultado = numero1 / numero2
    else:
        print('voce digitou o operador errado!')
    print(f'O resultado é {int(resultado)}')
    resposta = input('Deseja sair? [s/n]: ').lower()[0]

    if resposta == 's':
        break
    else:
        continue

  
    
""" Calculadora com while """
# while True:
#     numero_1 = input('Digite um número: ')
#     numero_2 = input('Digite outro número: ')
#     operador = input('Digite o operador (+-/*): ')

#     numeros_validos = None

#     try:
#         num_1_float = float(numero_1)
#         num_2_float = float(numero_2)
#         numeros_validos = True
#     except:
#         numeros_validos = None

#     if numeros_validos is None:
#         print('Um ou ambos os números digitados são inválidos.')
#         continue

#     operadores_permitidos = '+-/*'

#     if operador not in operadores_permitidos:
#         print('Operador inválido.')
#         continue

#     if len(operador) > 1:
#         print('Digite apenas um operador.')
#         continue

#     ###

#     sair = input('Quer sair? [s]im: ').lower().startswith('s')

#     if sair is True:
#         break