def convertir_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def promedio_temperaturas(temp1, temp2, temp3):
    return (temp1 + temp2 + temp3) / 3


def main():
    temperaturas = [72, 68, 75, 80]
    suma = 0
    for t in temperaturas:
        suma += convertir_a_celsius(t)
    promedio = (suma / len(temperaturas))
    print("Promedio en °C:", promedio)

if __name__ == "__main__":
    main()

# Código arreglado