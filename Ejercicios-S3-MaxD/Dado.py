import random

# Colores ANSI para los mensajes
COLOR_DANGER = "\033[91m"
COLOR_WARNING = "\033[93m"
COLOR_SUCCESS = "\033[92m"
COLOR_RESET = "\033[0m"

def lanzar_dado():
    resultado = random.randint(1, 6)
    print(f"{COLOR_SUCCESS}Lanzaste el dado y obtuviste: {resultado}{COLOR_RESET}")
    return resultado

def lanzar_varias_veces(n):
    if not isinstance(n, int) or n <= 0:
        print(f"{COLOR_DANGER}Error: Debes ingresar un número entero positivo.{COLOR_RESET}")
        return
    print(f"{COLOR_WARNING}Simulando {n} lanzamientos del dado...{COLOR_RESET}")
    resultados = [lanzar_dado() for _ in range(n)]
    print(f"{COLOR_SUCCESS}Resultados: {resultados}{COLOR_RESET}")
    return resultados

# Ejemplo de uso
if __name__ == "__main__":
    try:
        veces = int(input("¿Cuántas veces deseas lanzar el dado? "))
        lanzar_varias_veces(veces)
    except ValueError:
        print(f"{COLOR_DANGER}Error: Entrada inválida. Ingresa un número entero.{COLOR_RESET}")
