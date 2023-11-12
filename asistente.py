def detectar_alexa(texto):
    # Dividir el texto en palabras
    palabras = texto.split()

    # Contar el número de veces que se menciona "Alexa"
    menciones = palabras.count('Alexa')

    if menciones == 1:
        print("Hola, soy Alexa. ¿En qué puedo ayudarte?")
    elif menciones > 1:
        print("Tranquilo, solo di mi nombre una vez.")
    else:
        print("No mencionaste mi nombre.")

# Solicitar al usuario que ingrese un texto
texto_usuario = input("Ingresa un texto: ")

# Llamar a la función para detectar menciones de "Alexa"
detectar_alexa(texto_usuario)
