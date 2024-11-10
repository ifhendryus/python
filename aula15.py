"""
Formatação f strings
"""
variavel = 'ABC'
print(f'{variavel: >10}') #alinha para direita
print(f'{variavel: <10}') #alinha para esquerda
print(f'{variavel: ^10}') #alinha para o meio/centro
print(f'{variavel:$^10}') #adiciona $ nos espaços em branco
print(f'{10000.002920922233:,.1f}') #formatação de numeros