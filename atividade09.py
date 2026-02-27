temperatura = float(input)("digite a temperatura do servidor")

if temperatura >80:
    print ("perigo,desligando servidor por superaqueciment!")

elif temperatura>=50:
    print ("alerta: ligado no maximo:")

else:
    print("temperatura normal")
    