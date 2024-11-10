def multiplicador(*args):
    multi = 1
    for numeros in args:
        multi *= numeros 
    return(multi)
resultado = multiplicador(1,2,3,4,5)
print(resultado)


def parouimpar(numero):
    num = numero 
    if num % 2 == 0:
        return ('ele é par')
    return('ele é impar')
digito = int(input('numero:'))
resultado = parouimpar(digito)
print(resultado)