import os
from time import sleep
lista = []

#by_hendrix :)
def limpa_tela():
    os.system('cls')
def enter():
    input('Pressione Enter para continuar...')

while True:
    try:
        print('-=-=-=Lista=-=-=-')
        print('Selecione uma opção')
        opcao = str(input('[I]nserir [A]pagar [L]istar [S]air: ')).upper().strip()[0]
    except IndexError:
        limpa_tela()
        continue

    if opcao == 'I':
        decisao = 'S'
        while decisao != 'N':
            limpa_tela()

            valor = input('Item: ').strip()

            if valor.isnumeric():
                print('Números isolados não são permitidos.')
                print('São permitidos ex: "2x Maçã"')
                enter()
                limpa_tela()
                continue

            elif valor in '':
                print('Você digitou nada... Digite algo :)')
                enter()
                continue

            lista.append(valor)

            print('Item inserido na lista!!')

            try:    
                decisao = str(input('Quer inserir outro item? [s/n]: ')).upper().strip()[0]
                limpa_tela()
                
                if decisao in 'S':
                    continue
                elif decisao in 'N':
                    break
                    
                if decisao.isnumeric() or decisao != 'N':
                    while decisao.isnumeric() or decisao != 'S':

                        print('Digite [S/N] para sair ou continuar!!')
                        decisao = str(input('Quer inserir outro item? [s/n]: ')).upper().strip()[0]
                        if decisao in 'N':
                            break
                        limpa_tela()

                limpa_tela()
                
            except IndexError:
                limpa_tela()
                print('Você digitou nada... Digite algo :)')
                enter()

    elif opcao == 'A':
        if not lista:
            limpa_tela()
            print('Impossível apagar')
            print('A lista está vazia!! Adicione algo nela :)')
            enter()
            limpa_tela()
        else:
            try:
                decisao2 = 'S'
                while decisao2 != 'N':
                    mostrador = 0   
                    limpa_tela()

                    if not lista:
                        limpa_tela()
                        print('Impossível apagar')
                        print('A lista está vazia!! Adicione algo nela :)')
                        enter()
                        limpa_tela()
                        break

                    print('ÍNDICES     ITENS')

                    for numero,itens in enumerate(lista):
                        print(f'{numero:>4}{" " *8}{itens}')

                    numero_indice = int(input('Escolha o índice para apagar: '))

                    lista.remove(lista[numero_indice])

                    print('Removendo...')
                    sleep(2)

                    limpa_tela()
                    print('Removido com sucesso!!')

                    decisao2 = str(input('Deseja remover outro item? [s/n]: ')).upper().strip()[0]
                    if decisao2 in 'S' :
                        if not lista:
                            limpa_tela()
                            print('Impossível apagar')
                            print('A lista está vazia!! Adicione algo nela :)')
                            enter()
                            mostrador += 1
                            limpa_tela()
                            
                    else:
                        if decisao2.isnumeric() or decisao2 in '' or decisao2 != 'N':
                            while decisao2.isnumeric() or decisao2 in '' or decisao2 != 'N':
                                limpa_tela()
                                print('Você está digitando errado!!')
                                decisao2 = str(input('Deseja remover outro item? [s/n]: ')).upper().strip()[0]
                                if decisao2 in 'S':
                                    break

                    if mostrador == 1:
                        break
                    else:    
                        limpa_tela()

            except (IndexError, ValueError): 
                limpa_tela()
                print('Esse índice não existe!!')
                print('Verifique se o índice que você digitou está correto.')
                enter()
                limpa_tela()
                continue

    elif opcao == 'L':
        if not lista:
            limpa_tela()
            print('A lista está vazia!! Adicione algo nela :)')
            enter()
            limpa_tela()
        else:
            limpa_tela()

            print('ÍNDICES     ITENS')
            for numero,itens in enumerate(lista):
                print(f'{numero:>4}{" " *8}{itens}')

            enter()    
            limpa_tela()
    elif opcao == 'S':
        print('Saindo...')
        sleep(2)
        break
    else:
        limpa_tela()
        print('Você não escolheu nenhuma das opções!!')
        enter()
        limpa_tela()
        continue
#by_hendrix :)