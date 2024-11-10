from time import sleep
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
tentativas = 0
contador = 0
while True:
    try:
        for pergunta in perguntas:
            for chave, valor in pergunta.items():
                if chave == 'Resposta':
                    continue
                elif chave == 'Opções':
                    print(f'{chave}:')
                    for indice, valores in enumerate (valor):
                        print(f'{indice}){valores}')
                        if valores == pergunta['Resposta']:
                            alternativa_correta = indice
                else:
                    print(chave, valor)        
            alternativa = int(input('Digte a alternativa correta:'))
            contador += 1
            if alternativa == alternativa_correta:
                print('acertou!')
                tentativas += 1
            else:
                print('errou')
            sleep(0.2)
            print('\n')
        if contador == 3:
            break
    except ValueError:
        print('DIGITE PELA ALTERNATIVA!!\n')
        continue
print(f'Você acertou {tentativas} de 3 perguntas')