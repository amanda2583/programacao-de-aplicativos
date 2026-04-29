def sofrer_dano(vida_atual, valor_dano):
    vida_atual -= valor_dano
    return vida_atual
vida = 100

while vida > 0:
    dano = float(input("Quanto de dano o monstro causou? "))
    
    vida = sofrer_dano(vida, dano)
    
    print(f"Vida restante: {vida}")

print("Game Over")