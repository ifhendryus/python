lista = ['Hendryus','Érica','Bolinho']
contador = 0
for nomes in lista:
    print(f'O índice {nomes} = "{contador}"')
    contador += 1



nome1, *_ = lista 
print(nome1)