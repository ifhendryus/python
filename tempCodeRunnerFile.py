ano = int(input('ano: '))

ano1 = ano % 4
ano2 = ano % 100
ano3 = ano % 400

if ano1 == 0 and ano2 == 0 and ano3 == 0:
    print('ele é bissexto!')
elif ano1 == 0 and ano2 > 0:
    print('ele é um ano bissexto!')
elif ano3 > 0:
    print('ele não é ano bissexto!')
