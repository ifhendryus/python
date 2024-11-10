import json

def buscar_produto(arquivo_json, nome_produto):
    with open(arquivo_json, mode='r') as file:
        catalogo = json.load(file)  # Carregar o conteúdo do arquivo JSON
        
        for produto in catalogo['produtos']:  # Iterar pelos produtos no catálogo
            if produto['nome'].lower() == nome_produto.lower():  # Comparar o nome (ignorar maiúsculas/minúsculas)
                return produto
        
        return None


arquivo_json = 'catalogo.json' 

nome_produto = input('Digite o nome do produto que deseja buscar: ')
produto_encontrado = buscar_produto(arquivo_json, nome_produto)

if produto_encontrado:
    print(f"Produto encontrado: {produto_encontrado}")
else:
    print('Produto não encontrado.')
