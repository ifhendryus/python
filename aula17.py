"""
introdução ao try/except

try => tentar executar o codigo
except => ocorreu algum erro ao tentar 
"""

# print(12345)
# print(355)
# int('a')

numero_str = input('vou dobrar o numero que vc digitar:')

try:
    numero_float = float(numero_str)
    print('FLOAT: ', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2}')
except:
    print('isso não é um número')