# Escreva um script que solicita ao usuário uma lista de 
# compras e as salva em um arquivo de texto.
'''with open('lista_de_compras.txt', 'w') as arquivo:

    sair = 's'
    lista = []
    while sair != 'n' :
        item = input('anote o item que voce deseja:')
        lista.append(item)
        arquivo.write(item + '\n')
        sair = input('voce desja sair sim ou não?:').lower().strip()[0]'''


# Desenvolva um programa que 
# lê um arquivo de texto contendo números, 
# um por linha, e calcula a soma desses números.

# with open('soma.txt','w') as arquivo:
#     numero = 'Numero1 = 31'
#     numero2 = 'Numero2 = 47'
    
#     _, numero_int = numero.split('=')
#     _, numero_int2 = numero2.split('=')
    
    
#     numero_int = int(numero_int)
#     numero_int2 = int(numero_int2)
#     resultado = numero_int + numero_int2
#     resultado_str = str(resultado)

#     arquivo.write(numero + '\n')
#     arquivo.write(numero2)
#     arquivo.write('\nO resultado e: '+ resultado_str)



# Crie um sistema simples de registro de notas,
# onde o usuário insere o nome do aluno e a nota, 
# e o programa salva essas informações em um arquivo.
    

with open('notas_alunos.txt', 'a') as arquivo: 
    c = 0
    while True:
        nome = str(input("digite seu nome: "))
        nota = float(input(f"digite sua nota '{nome}': ")) 
        nota_str = nota
        msg = f'Nome: {nome} \nNota: {nota_str}\n' 
        arquivo.write(msg)
        c += 1
        if c >= 2: 
            break
