
temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]

while True:
    resposta = input("Deseja adicionar uma nova temperatura? (s/n): ").lower()
    
    if resposta == 's':
        nova_temp = float(input("Digite a temperatura: "))
        temps.append(nova_temp)
    elif resposta == 'n':
        break
    else:
        print("Resposta inválida! Digite 's' ou 'n'.")

print("\n--- Relatório de Temperaturas ---")

for temp in temps:
    if temp > 30.0:
        print(f"ALERTA: Temperatura Crítica! ({temp}°C)")
    else:
        print(f"Temperatura Normal. ({temp}°C)")