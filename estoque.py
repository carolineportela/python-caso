#**************************************************************************************
# Objetivo: Criação de um sistema responsavel pela gestão de um estoque de eletronicos
# Estudo de caso : Computational Logical Using Python
# Data: 17/06/2024
# Autor: Caroline Portela
# Versão: 1.0
#**************************************************************************************

#definindo uma lista vazia para armazenar os produtos

produtos = []

#funcao para adicionar produto
def adicionar_produto():

    nome = input("Digite o nome do produto: ")

    preco = float(input("Digite o preço do produto: "))

    quantidade = int(input("Digite a quantidade do produto: "))

    produto = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }

    produtos.append(produto)
    print("Seu produto foi adicionado com sucesso!")

#funcao para editar um produto pelo nome
def editar_produto():
    nome = input("Digite o nome do produto que deseja editar: ")
    for produto in produtos:

        if produto["nome"] == nome:

            print(f"Produto encontrado: {produto}")

            novo_nome = input("Digite o novo nome do produto (ou pressione Enter para manter o nome atual): ")

            if novo_nome:
                produto["nome"] = novo_nome
            novo_preco = input("Digite o novo preço do produto (ou pressione Enter para manter o preço atual): ")
            if novo_preco:
                produto["preco"] = float(novo_preco)
            nova_quantidade = input("Digite a nova quantidade do produto (ou pressione Enter para manter a quantidade atual): ")
            if nova_quantidade:
                produto["quantidade"] = int(nova_quantidade)
            print("Produto atualizado com sucesso!")
            return
    print("Produto não encontrado.")


#funcao para trazer uma lista de produtos cadastrados
def visualizar_produtos():

    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Editar produto")
        print("3. Visualizar produtos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            editar_produto()
        elif opcao == "3":
            visualizar_produtos()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

# inicializa o menu
menu()
