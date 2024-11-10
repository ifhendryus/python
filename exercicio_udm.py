opcao = ''
while opcao == '':
    print('\n\n')
    print('Que horas são? "Ex: 12-30"')
    hora = input('hora:')

    if hora[0] in '0' or hora[0] in '1' and hora[1] in '1':
        print(f'Bom dia neymar, são {hora} da manhã')
    elif hora[1] in '2' or hora[1] in '3' or hora[1] in '4' or hora[1] in '5' or hora[1] in '6' or hora[1] in '7':
        print(f'Boa tarde neymar, são {hora} da tarde')
    else:
        print(f'Boa noite neymar, são {hora} da noite')
    opcao = input(':')



#     # Pedir a hora no formato HH-MM
# hora = input('Que horas são? (Ex: 12-30): ')
# horas, minutos = hora.split('-')  # Separando a entrada em horas e minutos

# # Convertendo as partes da hora para inteiros
# horas = int(horas)

# # Verificação para determinar a saudação com base na hora
# if 0 <= horas < 12:
#     print(f'Bom dia, Neymar! São {horas}:{minutos} da manhã.')
# elif 12 <= horas < 18:
#     print(f'Boa tarde, Neymar! São {horas}:{minutos} da tarde.')
# else:
#     print(f'Boa noite, Neymar! São {horas}:{minutos} da noite.')
