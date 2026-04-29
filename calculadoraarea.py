def calcular_area(largura, comprimento):
    return largura * comprimento
contador = 1

while contador <= 3:
    print(f"\nTerreno {contador}")
    
    largura = float(input("Digite a largura: "))
    comprimento = float(input("Digite o comprimento: "))
    
    area = calcular_area(largura, comprimento)
    
    print(f"Área do terreno: {area}")
    
    contador += 1
    