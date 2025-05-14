# registrar compras de boletos de pasajeros
# su destino
# equipaje
#calcular el costo total del viaje
# asignando un ID único por reserva para hacer seguimiento.
# El sistema debe validar los límites de peso
# aplicar cobros por equipaje 
# generar un resumen detallado.

import datetime

# Global Data Storage
compras = []
contador_id = 1

# --- Constantes ---
PRECIOS_BASE = {
    "nacional": 230_000,
    "internacional": 4_200_000
}

COSTOS_EQUIPAJE = [
    (20, 50_000),
    (30, 70_000),
    (50, 110_000),
]

MAX_PESO_EQUIPAJE_MANO = 13
MAX_PESO_EQUIPAJE_PRINCIPAL = 50

# --- Funciones auxiliares ---
def generar_id_compra():
    global contador_id
    id_compra = f"COMP{contador_id:03d}"
    contador_id += 1
    return id_compra

def obtener_precio_base(tipo_viaje):
    return PRECIOS_BASE.get(tipo_viaje.lower(), 0)

def calcular_costo_equipaje(peso):
    if peso > MAX_PESO_EQUIPAJE_PRINCIPAL:
        return None, "No admitido"
    for limite, costo in COSTOS_EQUIPAJE:
        if peso <= limite:
            return costo, "Admitido"
    return 0, "Admitido"

def evaluar_equipaje_mano(peso):
    return "Rechazado" if peso > MAX_PESO_EQUIPAJE_MANO else "Admitido"

# --- Registro de compra ---
def registrar_compra():
    nombre = input("Nombre del pasajero: ").strip()
    tipo_viaje = input("Tipo de viaje (nacional/internacional): ").strip().lower()
    destino = "Bogotá → Medellín" if tipo_viaje == "nacional" else "Bogotá → España"

    try:
        peso_equipaje = float(input("Peso del equipaje principal (kg): "))
        if peso_equipaje<0:
            print("El peso debe ser positivo")
    except ValueError:
        print("Peso inválido.")
        return

    lleva_mano = input("¿Lleva equipaje de mano? (sí/no): ").strip().lower()
    peso_mano = 0
    if lleva_mano == "sí":
        try:
            peso_mano = float(input("Peso del equipaje de mano (kg): "))
        except ValueError:
            print("Peso inválido.")
            return

    fecha = input("Fecha del viaje (YYYY-MM-DD): ").strip()

    id_compra = generar_id_compra()
    precio_base = obtener_precio_base(tipo_viaje)
    costo_equipaje, estado_principal = calcular_costo_equipaje(peso_equipaje)
    estado_mano = evaluar_equipaje_mano(peso_mano)

    if costo_equipaje is None:
        costo_total = precio_base
    else:
        costo_total = precio_base + costo_equipaje

    compra = {
        "id": id_compra,
        "nombre": nombre,
        "destino": destino,
        "fecha": fecha,
        "tipo": tipo_viaje,
        "estado_principal": estado_principal,
        "estado_mano": estado_mano,
        "costo_total": costo_total
    }

    compras.append(compra)
    mostrar_resumen_cliente(compra)

# --- Mostrar resumen de compra ---
def mostrar_resumen_cliente(compra):
    print("\n--- RESUMEN DE COMPRA ---")
    print(f"ID de compra: {compra['id']}")
    print(f"Nombre del pasajero: {compra['nombre']}")
    print(f"Destino: {compra['destino']}")
    print(f"Fecha del viaje: {compra['fecha']}")
    print(f"Estado equipaje principal: {compra['estado_principal']}")
    print(f"Estado equipaje de mano: {compra['estado_mano']}")
    print(f"Costo total del viaje: ${compra['costo_total']:,}\n")

# --- Reportes administrativos ---
def reporte_total_recaudado():
    total = sum(compra["costo_total"] for compra in compras)
    print(f"\nTotal recaudado: ${total:,}")

def reporte_por_fecha():
    fecha = input("Ingrese la fecha a consultar (YYYY-MM-DD): ").strip()
    total = sum(compra["costo_total"] for compra in compras if compra["fecha"] == fecha)
    print(f"Total recaudado en {fecha}: ${total:,}")

def reporte_numero_pasajeros():
    print(f"Pasajeros procesados: {len(compras)}")

def reporte_pasajeros_por_tipo():
    nacionales = sum(1 for compra in compras if compra["tipo"] == "nacional")
    internacionales = sum(1 for compra in compras if compra["tipo"] == "internacional")
    print(f"Pasajeros nacionales: {nacionales}")
    print(f"Pasajeros internacionales: {internacionales}")

def consultar_por_id():
    id_buscar = input("Ingrese el ID de compra a consultar: ").strip().upper()
    for compra in compras:
        if compra["id"] == id_buscar:
            mostrar_resumen_cliente(compra)
            return
    print("Compra no encontrada.")

