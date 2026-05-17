# Función para dibujar el mapa
def dibujar_mapa(mapa):

    print("\n  0 1 2 3 4")

    for i in range(len(mapa)):

        print(f"{i} ", end="")

        for j in range(len(mapa[i])):

            valor = mapa[i][j]

            if valor == 1:
                simbolo = "B"

            elif valor == 8:
                simbolo = "X"

            elif valor == 9:
                simbolo = "O"

            else:
                simbolo = "~"

            print(f"{simbolo} ", end="")

        print()

def main():

    # 1. Declarar la matriz de 5x5 llena de ceros
    oceano = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0]
    ]

    # 2. Posicionar 3 barcos manualmente
    oceano[1][2] = 1
    oceano[3][4] = 1
    oceano[4][0] = 1

    print("¡Océano generado y flota desplegada!")

    # Mostrar mapa inicial
    dibujar_mapa(oceano)

    fila = int(input("\nIngresa la Fila para atacar (0-4): "))
    columna = int(input("Ingresa la Columna para atacar (0-4): "))

    # Validar coordenadas
    if fila < 0 or fila > 4 or columna < 0 or columna > 4:

        print("Coordenadas inválidas.")

    else:

        # Búsqueda y Modificación
        if oceano[fila][columna] == 1:

            print("¡IMPACTO CRÍTICO! Hundiste un barco.")

            oceano[fila][columna] = 8

        else:

            print("Fallaste. Solo le diste al agua.")

            oceano[fila][columna] = 9

        # Mostrar resultado final
        dibujar_mapa(oceano)

main()