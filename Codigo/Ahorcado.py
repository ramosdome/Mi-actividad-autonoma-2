import random

# Lista de palabras disponibles
palabras = [
    "python",
    "programacion",
    "algoritmo",
    "computadora",
    "desarrollo"
]

# Seleccionar una palabra aleatoria
palabra = random.choice(palabras)

# Inicializar variables del juego
progreso = ["_"] * len(palabra)
intentos = 6
letras_usadas = []

print("=== JUEGO DEL AHORCADO ===")

# Bucle principal del juego
while intentos > 0 and "_" in progreso:

    print("\nPalabra:", " ".join(progreso))
    print("Intentos restantes:", intentos)
    print("Letras usadas:", ", ".join(letras_usadas))

    letra = input("Ingrese una letra: ").lower()

    # Validación básica
    if len(letra) != 1:
        print("Ingrese solo una letra.")
        continue

    if letra in letras_usadas:
        print("Ya utilizó esa letra.")
        continue

    letras_usadas.append(letra)

    # Verificar si la letra pertenece a la palabra
    if letra in palabra:
        print("¡Correcto!")

        for i in range(len(palabra)):
            if palabra[i] == letra:
                progreso[i] = letra

    else:
        print("Letra incorrecta.")
        intentos -= 1

# Resultado final
if "_" not in progreso:
    print("\n¡Felicidades! Has ganado.")
    print("La palabra era:", palabra)
else:
    print("\nHas perdido.")
    print("La palabra correcta era:", palabra)