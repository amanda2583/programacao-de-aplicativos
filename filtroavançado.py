def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    condicao_principal = nota_teste > 80 and anos_xp > 2
    
    condicao_certificacao = possui_certificacao
    
    return condicao_principal or condicao_certificacao

nota = float(input("Digite a nota do teste: "))
anos = float(input("Digite os anos de experiência: "))
certificacao_input = input("Possui certificação? (s/n): ").lower()

possui_certificacao = certificacao_input == 's'

if verificar_aprovacao(nota, anos, possui_certificacao):
    print("Contratar")
else:
    print("Descartar")