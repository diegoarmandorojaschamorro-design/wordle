#Esta es la palabra clave a encontrar
palabra_secreta = "limon"
cantidad_letras = len(palabra_secreta)
#La cantidad maxima de intentos
max_intentos = 6

#Verifica si la palabra ingresada coincide con la secreta
def verificador_palabra(palabra_ingresada, palabra_secreta):
    resultado = []
    
    for i in range(cantidad_letras):
        letra = palabra_ingresada[i]
        
        if letra == palabra_secreta[i]:
            resultado.append(f"[{letra}]")
        elif letra in palabra_secreta:
            resultado.append(f"({letra})")
        else:
            resultado.append(f" {letra} ")
    # el .join solo es para separar por espacio las letras lo mire en youtube
    return " ".join(resultado)

#Inicia el juego

def iniciar_juego():
    intentos = 0
    print(f"Juego de palabras: Tienes {max_intentos} intentos para adivinar.")

    while intentos < max_intentos:
        intentos_restantes = max_intentos - intentos
        print(f"Te quedan {intentos_restantes} intentos")
        
        entrada = input("Ingrese una palabra: ").lower().strip()

        if len(entrada) != cantidad_letras:
            print(f"La palabra debe tener {cantidad_letras} letras.")
            continue

        intentos += 1
        pista = verificador_palabra(entrada, palabra_secreta)
        print(f"Resultado: {pista}")

        if entrada == palabra_secreta:
            print("Acertaste la palabra. Ganaste")
            break
        
        if intentos == max_intentos:
            print(f"Llegaste al limite de intentos. La palabra era: {palabra_secreta}")

#Llama al juego
iniciar_juego()