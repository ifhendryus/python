nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome == '' or idade == '':
    print('"Desculpe, você deixou campos vazios."\n')
else:
    if nome == nome and idade == idade:
        print(f'Seu nome é {nome}')
        print('Seu nome invertido:',nome[::-1])
        if ' ' in nome:
            print('Seu nome contém espaços')
        else:
            print('Seu nome não contém espaços')
        print('A primeira letra do seu nome é',nome[0]) 
        print('A ultima letra do seu nome é',nome[-1]) 
        print('Seu nome contém:',len(nome),'letras')   

