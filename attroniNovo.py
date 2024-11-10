'''Se o objeto é o primeiro na lista, seu peso dobra.
2. Se o objeto é o último na lista, seu peso triplica.
3. Se o objeto está em qualquer outra posição, seu peso é somado ao peso do objeto
anterior da lista.
4. Caso o objeto seja tanto o primeiro quanto o último (ou seja, o único na lista), ele
deve ter seu peso quadruplicado.'''
# objetos = []
# c = 0
# decisao = 's'
# while decisao != 'n':

#     objeto = input('Digite:')
#     peso = int(input('Seu peso:'))
#     decisao = input('Quer adicionar outro? [s/n]')
#     if decisao == 'n':
#         peso *= 4
#         coisas = objeto,peso
#         break
#     elif decisao == 's':
#         ...

#     coisas = objeto,peso
#     coisas = list(coisas)
#     objetos.append(coisas)
    

# for objetos1 in objetos:
#     c += 1  


# print(c)
# print(objetos[:])

    
def calcula_pesos(lista_objetos):
   
    if len(lista_objetos) == 1:
        nome, peso = lista_objetos[0]
        peso_modificado = peso * 4
        return [(nome, peso_modificado)]
    
    
    resultado = []
    
    for i, (nome, peso) in enumerate(lista_objetos):
        if i == 0:  
            peso_modificado = peso * 2
        elif i == len(lista_objetos) - 1:  
            peso_modificado = peso * 3
        else:  
            peso_modificado = peso + resultado[i - 1][1]  
        resultado.append((nome, peso_modificado))
    
    return resultado

def calcula_pesos_com_input():
    
    n = int(input("Quantos objetos deseja inserir? "))
    
    
    lista_objetos = []
    
    
    for i in range(n):
        nome = input(f"Nome do objeto {i + 1}: ")
        peso = float(input(f"Peso do objeto {i + 1}: "))
        lista_objetos.append((nome, peso))
    
    
    resultado = calcula_pesos(lista_objetos)
    
    
    print("\nLista de objetos com pesos modificados:")
    for nome, peso_modificado in resultado:
        print(f"{nome}: {peso_modificado}")

calcula_pesos_com_input()
