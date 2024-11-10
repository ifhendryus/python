
# opcao = ''
# while opcao == '' or opcao == 'n':
#     opcao = input('Deseja sair [s/n]: ').lower()
#     opcao = opcao.startswith('s')
#     print(opcao)
while True :
    opcao = input('Deseja sair [s/n]: ')
    opcao = opcao.lower()
    opcao = opcao.startswith('s')
    print(opcao)