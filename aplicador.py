def aplicar_promocao(lista_precos):
    nova_lista = []
    
    for preco in lista_precos:
        if preco > 100.0:
            preco_com_desconto = preco * 0.85  
            nova_lista.append(preco_com_desconto)
        else:
            nova_lista.append(preco)
    
    return nova_lista
compras = [150.0, 80.0, 200.0, 50.0]

compras_atualizadas = aplicar_promocao(compras)

print("Lista original:", compras)
print("Lista com desconto:", compras_atualizadas)