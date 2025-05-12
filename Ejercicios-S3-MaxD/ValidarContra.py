# Colores ANSI para los mensajes
COLOR_DANGER = "\033[91m"   # Rojo claro
COLOR_WARNING = "\033[93m"  # Amarillo claro
COLOR_SUCCESS = "\033[92m"  # Verde claro
COLOR_RESET = "\033[0m"     # Resetear color

import re

def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        print(f"{COLOR_DANGER}Error: La contraseña debe tener al menos 8 caracteres.{COLOR_RESET}")
        return False
    if not re.search(r"[A-Z]", contraseña):
        print(f"{COLOR_WARNING}Advertencia: La contraseña debe contener al menos una letra mayúscula.{COLOR_RESET}")
        return False
    if not re.search(r"[a-z]", contraseña):
        print(f"{COLOR_WARNING}Advertencia: La contraseña debe contener al menos una letra minúscula.{COLOR_RESET}")
        return False
    if not re.search(r"[0-9]", contraseña):
        print(f"{COLOR_WARNING}Advertencia: La contraseña debe contener al menos un número.{COLOR_RESET}")
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contraseña):
        print(f"{COLOR_WARNING}Advertencia: La contraseña debe contener al menos un símbolo (ej. !, @, #, etc.).{COLOR_RESET}")
        return False
    
    print(f"{COLOR_SUCCESS}Contraseña válida y segura.{COLOR_RESET}")
    return True

# Ejemplo de uso
if __name__ == "__main__":
    contraseña_usuario = input("Ingresa una contraseña para validar: ")
    validar_contraseña(contraseña_usuario)
