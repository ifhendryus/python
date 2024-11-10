
for i in range(0,10):
    qnt = 0
    print('-=-=VERFICADOR DE PAR OU ÍMPAR=-=-\n')
    numero = input('Apenas números inteiros:')
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('É um número par!!')
    else:
        print('É um número ímpar', qnt)
        qnt += 1
