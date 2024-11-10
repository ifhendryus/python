# palavra_secreta = 'jogador'
# palavra = ['*','*','*','*','*','*','*']
# tamanho_p= len(palavra_secreta)
# c = 0
# while True:
#     import os
#     os.system('cls')

#     if c >= tamanho_p:
#         break

#     print(f'{palavra[0]}{palavra[1]}{palavra[2]}{palavra[3]}{palavra[4]}{palavra[5]}{palavra[6]}')
#     letra = input('Digite uma letra: ')
#     tamanho = len(letra)
#     if tamanho > 1 or letra == ' ':
#         while tamanho > 1 or letra == ' ':
#             print('Você ta digitando várias letras!!\nUma letra por vez.') 
#             print('\n')
#             letra = input('Digite uma letra: ')
#             tamanho = len(letra)

#     if letra in palavra_secreta:
#         indice = palavra_secreta.index(letra)
#         palavra[indice] = letra
#         print(palavra[indice])
#         c +=1
#     else:
#         print('nao')
    
# print(palavra_secreta)

import os

palavra_secreta = 'jogador'
palavra = ['*'] * len(palavra_secreta)
tentativas = 6
letras_adivinhadas = []

while tentativas > 0:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(' '.join(palavra))  # Exibe a palavra com espaços entre os caracteres
    letra = input('Digite uma letra: ').lower()

    # Verifica se a entrada é válida
    if len(letra) != 1 or letra == ' ':
        print('Você deve digitar uma letra por vez.')
        continue

    if letra in letras_adivinhadas:
        print('Você já tentou essa letra.')
        continue

    letras_adivinhadas.append(letra)

    if letra in palavra_secreta:
        # Atualiza todas as ocorrências da letra
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra[i] = letra
        print('Boa! Você acertou uma letra.')
    else:
        tentativas -= 1
        print('Letra não encontrada. Tentativas restantes:', tentativas)

    # Verifica se o jogador ganhou
    if '*' not in palavra:
        print(f'Parabéns! Você adivinhou a palavra: {palavra_secreta}')
        break
else:
    print(f'Você perdeu! A palavra era: {palavra_secreta}')
