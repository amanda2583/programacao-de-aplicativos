def somar_carrinho(lista_precos):
    total = 0
    
    for preco in lista_precos:
        total += preco
    
    if total > 500:
        total *= 0.9  
    
    return total
compras = [120.0, 250.0, 180.0, 90.0]

valor_final = somar_carrinho(compras)

print(f"Total a pagar: R$ {valor_final:.2f}")