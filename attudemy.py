 

'''Criar uma lista chamada minhaLista com os seguinte itens: 76, 92.3, “oi”, True, 4, 76.  

Depois execute os seguintes comandos: 

a) Inserir “pitomba” e 76 no final da lista. 

b) Inserir o valor “Cibele” na posição de índice 3. 

c) Inserir o valor 99 no início da lista. 

d) Encontrar o índice de “oi”. 

e) Remover True da lista.''' 

lista = [76, 92.3, "oi", True, 4, 76]   # declarei a lista principal 
lista2 = ['pitomba']                    # criei outra lista e guardei o valor ‘pitomba’ 
lista += lista2                         # concatenei a lista2 com a lista 
lista[3] = 'cibele'                     # adicionei ‘cibele’ no lugar de True (ao mesmo tempo excluindo) 
lista[0] = 99                           # adicionei 99 no primeiro índice 
indice = 0                              #iniciei um contador para encontra o índice ‘oi’ na lista 
for buscador in lista: 
    if buscador == 'oi':                # coloquei um identificador chamado ‘buscador’ para encontrá-lo 
        break 
    indice += 1                         # adicionei +1 cada vez que ele percorresse sobre os itens da lista 

 
print('LISTA:',lista) 
print('A posição do "oi" está no índice:', indice)
print('\n')

 

 