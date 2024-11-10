dic_produtos = {}
nome_produto = input("Nome do produto: ")
preco_produto = input("Preço do produto: ")

# cadastrar o novo produto (se o produto não existir)
# caso o produto exista ele vai editar o produto
nome_produto = nome_produto.lower()
preco_produto = float(preco_produto)

dic_produtos[nome_produto] = preco_produto
print(dic_produtos)

produto = 'iphone'

dic_produtos[produto]
