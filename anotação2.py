'''
existe um negocio chamado 

O método replace() precisa de dois argumentos:
o que você quer substituir e o que deseja colocar no lugar.

No seu código, falta o segundo argumento. Se você quer remover os pontos, o correto

.replace('Aqui dentro voce escolhe o que quer substituir . / e etc')
'''
# cpf = '123.123.123-00'.replace('-', '').replace('.','')
# print(cpf)


'''
existe outra coisa também que se chama re 

é uma expressão regular. tem um método que 
substitue tudo que nao for número 're.sub'

import re

'''
# import re
# cpf = re.sub( r'[^0-9]', '', '123.123.123-00')
# print(cpf)

'''
gerar cpf validos

'''
import random
cpf_gerador = ''

for i in range(11):
    cpf_gerador += str(random.randint(0,9))

print(cpf_gerador)
'''
checar de tem cpf repetido

'''
# import sys
# entrada = input('')

# primerio_caractere_entrada = entrada == entrada[0] * len(entrada)

# if primerio_caractere_entrada:
#     print('vacilo')
#     sys.exit()
