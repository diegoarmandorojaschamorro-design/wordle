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