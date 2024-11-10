# import os
# c = 0
# def limpa_tela():
#     os.system('cls')
# while c < 7:
#     limpa_tela()
#     hora, minutos = input('Horário:').split(':')
#     c += 1

#     hora = int(hora)
#     minutos = int(minutos)
#     if hora > 24:
#         print('Não existe esse horário!')
#     elif hora > 0 and hora < 12:
#         print(f'Bom dia, são {hora}:{minutos:02}')
#     elif hora > 12 and hora < 18:
#         print(f'Boa tarde, são {hora}:{minutos:02}')
#     elif hora >= 18:
#         print(f'Boa noite, são {hora}:{minutos:02}')
#     input('')

'''Questão 11º'''
# temperaturas = []
# c = 0
# repeticao = True
# while repeticao:
#     temperatura = input('Digite a temperatura:')
#     temperaturas.append(temperatura)
#     c += 1
#     opcao = input('Quer adicionar outra? [s/n]:').lower().strip()[0]

#     if opcao == 'n':
#         repeticao = False
#     elif opcao == 's':
#         continue
#     elif opcao != 'n':
#         while opcao != 's':
#             opcao = input('Quer adicionar outra? [s/n]:').lower().strip()[0]
#             if opcao == 'n':
#                 repeticao = False
#                 break

# maiores_temperaturas = 0
# menores_temperaturas = 0
# soma_de_temperaturas = 0
# for c, temperatura_ in enumerate(temperaturas):

#     temperatura_float = temperatura_
#     temperatura_float = float(temperatura_float)
    
#     soma_de_temperaturas += temperatura_float
#     if c == 1:
#         maiores_temperaturas = temperatura_float
#         menor_numero_temperaturas = temperatura_float

#     if temperatura_float < menores_temperaturas:
#         menores_temperaturas = temperatura_float

#     elif temperatura_float > maiores_temperaturas:
#         maiores_temperaturas = temperatura_float

# print(f'\nA maior temperatura foi de: {maiores_temperaturas}°')
# print(f'e menor temperatura foi de: {menores_temperaturas}°')
# print(f'A média das temperaturas foi de: {soma_de_temperaturas/c}°')

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s2 - s1
s3 = s1 ^ s2
print(s3)