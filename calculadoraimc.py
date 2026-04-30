def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Baixo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return f"{nome}, com {idade} anos, possui IMC de {imc:.2f} e está na categoria: {categoria}."
nome = input("Digite o nome: ")
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
idade = int(input("Digite a idade: "))

relatorio = gerar_relatorio_saude(nome, peso, altura, idade)
print(relatorio)