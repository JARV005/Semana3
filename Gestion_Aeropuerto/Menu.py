# registrar compras de boletos de pasajeros
# su destino
# equipaje
#calcular el costo total del viaje
# asignando un ID único por reserva para hacer seguimiento.
# El sistema debe validar los límites de peso
# aplicar cobros por equipaje 
# generar un resumen detallado.
from G_Aeropuerto import * 
# --- Menús ---
def menu_admin():
    while True:
        print("\n--- MENÚ ADMINISTRADOR ---")
        print("1. Total recaudado")
        print("2. Total por fecha")
        print("3. Número de pasajeros")
        print("4. Número de pasajeros por tipo de viaje")
        print("5. Consultar compra por ID")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            reporte_total_recaudado()
        elif opcion == "2":
            reporte_por_fecha()
        elif opcion == "3":
            reporte_numero_pasajeros()
        elif opcion == "4":
            reporte_pasajeros_por_tipo()
        elif opcion == "5":
            consultar_por_id()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

def Menu():
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE EQUIPAJE AÉREO ---")
        print("1. Registrar nueva compra")
        print("2. Ingresar como administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_compra()
        elif opcion == "2":
            menu_admin()
        elif opcion == "3":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")
        



Menu()