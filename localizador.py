ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]

busca = input("Digite o nome da ferramenta que deseja procurar: ")

encontrado = False

for ferramenta in ferramentas:
    if ferramenta.lower() == busca.lower():
        print(f"Ferramenta '{busca}' encontrada no estoque!")
        encontrado = True
        break

if not encontrado:
    print(f"Ferramenta '{busca}' NÃO está no estoque.")