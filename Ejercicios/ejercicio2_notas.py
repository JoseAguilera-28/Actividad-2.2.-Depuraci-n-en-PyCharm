def calcular_media(notas):
    total = 0
    for n in notas:
        total = total + n
    return total / len(notas)
def evaluar_aprobado(media):
    if media < 5:
        return "Suspenso"
    elif media < 7:
        return "Aprobado"
    elif media < 9:
        return "Notable"
    else:
        return "Sobresaliente"
def main():
    notas = [3, 7, 8, 5]
    media = calcular_media(notas)
    resultado = evaluar_aprobado(media)
    print("Media:", media)
    print("Resultado:", resultado)
if __name__ == "__main__":
    main()


# Código arreglado