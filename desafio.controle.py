autorizados = ["Alice", "Bob", "Carlos"]

nome = input("Digite o nome do pesquisador: ")


if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"Acesso Permitido! O pesquisador {nome} está na posição {indice}.")

    remover = input("Deseja remover esse pesquisador da lista? (Sim/Não): ")

    if remover.lower() == "sim":
        autorizados.remove(nome)
        print("Pesquisador removido com sucesso!")
        print("Lista atualizada:", autorizados)
    else:
        print("Nenhuma alteração realizada.")

else:
    print(f"Acesso Negado! O pesquisador {nome} não foi encontrado.")

    cadastrar = input("Deseja cadastrar esse novo pesquisador? (Sim/Não): ")

    if cadastrar.lower() == "sim":
        autorizados.append(nome)
        print("Pesquisador cadastrado com sucesso!")
        print("Lista final:", autorizados)
    else:
        print("Nenhuma alteração realizada")