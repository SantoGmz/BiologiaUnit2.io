# Números ganadores
numeros_ganadores = {7, 10, 15, 21, 22, 29}

# Tus boletos (cada lista es un boleto)
boletos = [
    [7, 20, 26, 27, 28, 34],
    [2, 7, 15, 17, 24, 29],
    [11, 12, 13, 16, 21, 32],
    [15, 17, 28, 30, 36, 37],
    [19, 12, 20, 23, 24, 30],
    [7, 13, 15, 17, 25, 27],
    [9, 17, 31, 34, 35, 37],
    [5, 16, 27, 30, 34, 39],
    [4, 10, 16, 19, 20, 38],
    [3, 11, 12, 16, 19, 38],
]


print(f"Los números que salieron son: {' '.join(map(str, sorted(list(numeros_ganadores))))}")

print("-" * 30)

# Itera sobre cada boleto y revisa los aciertos
for boleto in boletos:
    # Convierte el boleto a un conjunto para una revisión más eficiente
    boleto_set = set(boleto)

    # Encuentra la intersección (números en común)
    aciertos = boleto_set.intersection(numeros_ganadores)
    
    # Prepara el formato de salida
    linea_boleto = " ".join([str(num) for num in boleto])
    
    # Prepara la lista de aciertos para la impresión
    aciertos_str = ', '.join(map(str, sorted(list(aciertos))))
    
    if len(aciertos) == 1:
        print(f"{linea_boleto} ({len(aciertos)} acierto: {aciertos_str})")
    elif len(aciertos) > 1:
        print(f"{linea_boleto} ({len(aciertos)} aciertos: {aciertos_str})")
    else:
        print(f"{linea_boleto} (0 aciertos)")