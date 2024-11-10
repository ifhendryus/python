c = 0
vogais = ['A','E','I','O',"U"]
while c < 4:
    letra = str(input('Letra:')).upper().strip()
    c += 1
    if letra in vogais:
        print('é uma vogal')
    else:
        print('Nao é vogal')


produto1 = input('Digite o produto:')
valor1 = float(input('Digite o valor do produto:'))

produto2 = input('Digite o produto:')
valor2 = float(input('Digite o valor do produto:'))

produto3 = input('Digite o produto:')
valor3 = float(input('Digite o valor do produto:'))

if valor1 < valor2 and valor1 < valor3:
  print(produto1,' É o mais barato')
elif valor2 < valor1 and valor2 < valor3:
  print(produto2,'É o mais barato')
else:
  print(produto3, 'É o mais barato')



numero1 = int(input('numero1: '))
numero2 = int(input('numero2: '))
numero3 = int(input('numero3: '))


if numero1 < numero2 and numero1 < numero3:
    if numero2 < numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
elif numero2 < numero1 and numero2 < numero3:
    if numero1 < numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1)
else:
    if numero1 < numero2:
        print(numero3, numero1, numero2)
    else:
        print(numero3, numero2, numero1)



turma = str(input('Digite M-matutino/ V-vespetino / N-noturno: ')).upper()[0]

if turma == 'M':
    print('Bom dia')
elif turma == 'V':
    print('Boa tarde')
elif turma == 'N':
    print('Boa noite')
else:
    print('Não existe esse turno')