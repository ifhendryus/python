

# for c in range(5,0,-1):
#     if c == 1:
#         print(f'''{c} patinhos foram passear
# Além das montanhas Para brincar A mamãe gritou: Quá, quá, quá, quá
# nenhum patinhos voltaram de lá''')
#         break
#     print(f'''{c} patinhos foram passear
# Além das montanhas Para brincar A mamãe gritou: Quá, quá, quá, quá
# Mas só {c-1} patinhos voltaram de lá\n''')

numeros = ['zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez']
for c in range(1,11):
    incomoda = ' incomoda'
    if c % 2 == 0:
        print(f'{numeros[c]} elefante{incomoda*c} muito mais!!')
    else:
        print(f'{numeros[c]} elefante incomodam muita gente.')
    
    if c == 10:
        for c in range(9,0,-1):
            incomoda = ' incomoda'
            if c % 2 == 0:
                print(f'{numeros[c]} elefante{incomoda*c} muito mais!!')
            else:
                print(f'{numeros[c]} elefante incomodam muita gente.')