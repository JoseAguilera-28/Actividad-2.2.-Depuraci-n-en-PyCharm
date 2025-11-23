def obtener_elemento(lista, indice):
    return lista[indice]
def sumar_lista(lista):
    total = 0
    for i in range(len(lista)):
        total += lista[i]
    return total
def main():
    datos = [2, 4, 6, 8]

    print("Elemento:", obtener_elemento(datos, 3))

    try:
        print("Elemento:", obtener_elemento(datos, 4))
    except IndexError as e:
        print(f"Error detectado: No se pudo obtener el elemento. {e}")

    print("Suma total:", sumar_lista(datos))


if __name__ == "__main__":
    main()


# Código arreglado