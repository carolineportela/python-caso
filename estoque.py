#**************************************************************************************
# Objetivo: Criação de um sistema responsavel pela gestão de um estoque de eletronicos
# Estudo de caso : Computational Logical Using Python
# Data: 17/06/2024
# Autor: Caroline Portela
# Versão: 1.0
#**************************************************************************************

# definindo uma lista vazia para armazenar os produtos
produtos = []

# função para adicionar produto
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
    print("#" * 80)

# função para editar um produto pelo nome
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
            print("#" * 80)
            return
    print("Produto não encontrado.")
    print("#" * 80)

# função para trazer uma lista de produtos cadastrados
def visualizar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        print("#" * 80)
        return
    for produto in produtos:
        print("Vizualizando estoque :")
        print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}")
    print("#" * 80)

# função para remover um produto pelo nome
def remover_produto():
    nome = input("Digite o nome do produto que deseja remover: ")
    for produto in produtos:
        if produto["nome"] == nome:
            produtos.remove(produto)
            print("Produto removido com sucesso!")
            print("#" * 80)
            return
    print("Produto não encontrado.")
    print("#" * 80)

def menu():
    while True:
        print("\nMenu:")
        print("1. Adicionar produto")
        print("2. Editar produto")
        print("3. Visualizar produtos")
        print("4. Remover produto")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_produto()
        elif opcao == "2":
            editar_produto()
        elif opcao == "3":
            visualizar_produtos()
        elif opcao == "4":
            remover_produto()
        elif opcao == "5":
            print("Saindo...")
            print("#" * 80)
            break
        else:
            print("Opção inválida. Tente novamente.")
            print("#" * 80)
        
        continuar = input("Deseja realizar outra operação? (s/n): ").lower()
        if continuar != 's':
            print("Saindo...")
            print("#" * 80)
            break

# start o menu
menu()
