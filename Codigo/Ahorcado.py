# Importación de la biblioteca random.
# Esta biblioteca proporciona funciones para generar valores aleatorios.
# Se utiliza para seleccionar una palabra diferente cada vez que inicia una partida.
import random


# Una lista es una estructura de datos que permite almacenar múltiples elementos.
# En este caso, la lista contiene todas las palabras disponibles para el juego.
# Despues, el sistema seleccionará una de ellas de manera aleatoria.
PALABRAS = ["python","programacion","algoritmo","computadora","desarrollo","variable","funcion","repositorio","github","software"]


# Una función es un bloque de código reutilizable que realiza una tarea específica.
# Esta función se encarga de seleccionar una palabra aleatoria de la lista PALABRAS.
# Se utiliza para que cada partida sea diferente.
def seleccionar_palabra():
    return random.choice(PALABRAS)


# Esta función muestra al usuario toda la información necesaria
# para conocer el estado actual de la partida.
# Recibe como parámetros el progreso de la palabra,
# la cantidad de intentos disponibles y las letras utilizadas.
def mostrar_estado(progreso, intentos, letras_usadas):

    print("\n" + "=" * 50)
    print("PALABRA:", " ".join(progreso))
    print("INTENTOS RESTANTES:", intentos)

    # La estructura condicional IF permite ejecutar instrucciones
    # únicamente cuando se cumple una condición determinada.
    # Aquí verifica si existen letras almacenadas en la lista.
    if letras_usadas:
        print("LETRAS UTILIZADAS:", ", ".join(letras_usadas))
    else:
        print("LETRAS UTILIZADAS: Ninguna")

    print("=" * 50)


# Esta función verifica si una letra ingresada por el usuario
# se encuentra dentro de la palabra secreta.
# Devuelve True si la letra existe y False si no existe.
def verificar_letra(letra, palabra, progreso):

    # Variable booleana.
    # Los valores booleanos solo pueden ser True o False.
    # Se utiliza para indicar si la letra fue encontrada.
    encontrada = False

    # El ciclo FOR es una estructura repetitiva.
    # Permite recorrer una secuencia de elementos.
    # En este caso, recorre todas las posiciones de la palabra.
    for i in range(len(palabra)):

        # La estructura IF permite comparar dos valores.
        # Si la letra coincide con una posición de la palabra,
        # se actualiza el progreso del jugador.
        if palabra[i] == letra:

            progreso[i] = letra
            encontrada = True

    return encontrada


# Esta función contiene la lógica principal de una partida.
# Se encarga de controlar el flujo completo del juego.
def jugar():

    # Se llama a la función seleccionar_palabra()
    # para obtener una palabra aleatoria.
    palabra = seleccionar_palabra()

    # len() devuelve la cantidad de caracteres de la palabra.
    # La multiplicación crea una lista de guiones bajos
    # con el mismo tamaño de la palabra seleccionada.
    # Cada guion representa una letra aún no descubierta.
    progreso = ["_"] * len(palabra)

    # Variable que almacena la cantidad máxima de errores permitidos.
    intentos = 6

    # Lista vacía destinada a almacenar las letras ingresadas.
    letras_usadas = []

    print("\n¡BIENVENIDO AL JUEGO DEL AHORCADO!")

    # El ciclo WHILE es una estructura repetitiva.
    # Ejecuta instrucciones mientras una condición sea verdadera.
    #
    # El juego continuará mientras:
    # 1. Existan intentos disponibles.
    # 2. Queden letras por descubrir.
    while intentos > 0 and "_" in progreso:

        mostrar_estado(progreso, intentos, letras_usadas)

        # input() permite recibir datos ingresados por el usuario.
        # lower() convierte el texto a minúsculas para evitar errores
        # durante las comparaciones.
        letra = input("Ingrese una letra: ").lower()

        # Esta validación verifica que el usuario ingrese
        # únicamente una letra del alfabeto.
        if len(letra) != 1 or not letra.isalpha():

            print("Error: Debe ingresar una sola letra.")
            continue

        # Esta condición verifica si la letra ya fue utilizada.
        # Su objetivo es evitar que el jugador repita intentos.
        if letra in letras_usadas:

            print("Ya utilizó esa letra.")
            continue

        # append() es un método de las listas.
        # Permite agregar un nuevo elemento al final de la colección.
        letras_usadas.append(letra)

        # Se llama a la función verificar_letra().
        # Dependiendo del resultado, se ejecutará un bloque diferente.
        if verificar_letra(letra, palabra, progreso):

            print("¡Correcto! La letra está en la palabra.")

        else:

            print("Letra incorrecta.")

            # Operador de asignación compuesto.
            # Reduce el número de intentos disponibles en una unidad.
            intentos -= 1

    # Esta condición determina si el jugador ganó la partida.
    # Si no existen guiones bajos, significa que descubrió
    # todas las letras de la palabra.
    if "_" not in progreso:

        print("\n🎉 ¡FELICIDADES! HAS GANADO.")
        print("La palabra era:", palabra)

    else:

        # Si los intentos llegan a cero antes de completar la palabra,
        # el jugador pierde la partida.
        print("\n❌ HAS PERDIDO.")
        print("La palabra correcta era:", palabra)


# Función principal del programa.
# Su objetivo es controlar la ejecución general del sistema
# y permitir que el usuario juegue múltiples partidas.
def main():

    # WHILE TRUE crea un ciclo repetitivo que mantiene
    # el programa en ejecución hasta que el usuario decida salir.
    while True:

        # Se ejecuta una partida completa del juego.
        jugar()

        # Ciclo de validación de respuesta.
        # Garantiza que el usuario ingrese únicamente
        # opciones válidas para continuar o finalizar.
        while True:

            # input() permite capturar datos desde el teclado.
            # lower() convierte la respuesta a minúsculas
            # para facilitar las comparaciones.
            respuesta = input("\n¿Desea jugar nuevamente? (s/n): ").lower()

            # La estructura IF verifica si la respuesta
            # corresponde a alguna opción válida para continuar.
            if respuesta in ["s", "si", "sí"]:

                print("\nIniciando una nueva partida...")

                # BREAK finaliza el ciclo de validación
                # y permite regresar al ciclo principal.
                break

            # ELIF evalúa una segunda condición.
            # Verifica si el usuario desea salir del programa.
            elif respuesta in ["n", "no"]:

                print("\nGracias por jugar.")

                # RETURN finaliza completamente la función main()
                # y termina la ejecución del programa.
                return

            # ELSE se ejecuta cuando ninguna condición anterior
            # se cumple. Su función es controlar errores de entrada.
            else:

                print( "\nOpción no válida. ", "Ingrese únicamente 's' o 'n'.")


# __name__ es una variable especial de Python.
# Esta condición garantiza que la función principal
# solo se ejecute cuando este archivo sea iniciado directamente.
if __name__ == "__main__":
    main()