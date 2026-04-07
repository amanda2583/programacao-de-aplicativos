lista_vip = []

while True:
    nome = input("Digite o nome do convidado (ou 'fim' para encerrar): ")
    
    if nome.lower() == "fim":
        break
    
    if nome and nome[0].lower() == 'a':
        lista_vip.append(nome)
        print(f"{nome} adicionado à lista VIP!")
    else:
        print("Apenas nomes com A são permitidos no VIP.")

print("\nLista VIP:")
for pessoa in lista_vip:
    print(pessoa)