def esta_na_lista(lista_nomes, nome_busca):
    for nome in lista_nomes:
        if nome == nome_busca:
            return "Encontrado!"
    return "Não disponível"


# Programa principal
frutas = ["maçã", "banana", "laranja", "uva"]

busca = input("Digite o nome da fruta que deseja buscar: ")

resultado = esta_na_lista(frutas, busca)

print(resultado)