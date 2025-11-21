#CRUD de inventario de productos

#Inventario avanzado con colecciones y persistencia en archivos

inventario = []

def add_inventory(inventario):
    print("\n---- Agregar producto al inventario ----")
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio unitario: "))
    cantidad = int(input("Cantidad: "))
    # Agrega producto o actualiza si ya existe
    nombre_key = nombre.lower()

    for p in inventario:
        if p["nombre"].lower() == nombre_key:
            p["cantidad"] += cantidad
            p["precio"] = precio
            print("Cantidad actualizada.")
            return
        
    inventario.append({
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    })
    print("Producto agregado.")

    
    
def show_inventory(inventario):
    if not inventario:
        print("Inventario vacío.")
        return
    print(f"{'Nombre':30} {'Precio':>10} {'Cantidad':>10} {'Subtotal':>12}")
    for p in inventario:
        subtotal = p["precio"] * p["cantidad"]
        print(f"{p['nombre'][:30]:30} {p['precio']:10.2f} {p['cantidad']:10d} {subtotal:12.2f}")


def search_product(inventario, nombre):
    clave = nombre.strip().lower()
    for p in inventario:
        if p["nombre"].strip().lower() == clave:
            return p
    return None

def update_product(inventario, nombre, nuevo_precio=None, nueva_cantidad=None):
    p = search_product(inventario, nombre)
    if not p:
        return False
    if nuevo_precio is not None:
        p["precio"] = float(nuevo_precio)
    if nueva_cantidad is not None:
        p["cantidad"] = int(nueva_cantidad)
    return True


def delete_product(inventario, nombre):
    clave = nombre.strip().lower()
    for i, p in enumerate(inventario):
        if p["nombre"].strip().lower() == clave:
            del inventario[i]
            return True
    return False


def calcular_estadisticas(inventario):
    if not inventario:
        return {"unidades_totales":0, "valor_total":0.0, "producto_mas_caro":(None,0.0), "producto_mayor_stock":(None,0)}
    subtotal = lambda p: p["precio"] * p["cantidad"]
    unidades_totales = sum(p["cantidad"] for p in inventario)
    valor_total = sum(subtotal(p) for p in inventario)
    producto_mas_caro = max(inventario, key=lambda p: p["precio"])
    producto_mayor_stock = max(inventario, key=lambda p: p["cantidad"])
    return {
        "unidades_totales": unidades_totales,
        "valor_total": valor_total,
        "producto_mas_caro": (producto_mas_caro["nombre"], producto_mas_caro["precio"]),
        "producto_mayor_stock": (producto_mayor_stock["nombre"], producto_mayor_stock["cantidad"])
    }


# add_inventory(inventario, "Lápiz", 500.0, 10)
# add_inventory(inventario, "Cuaderno", 1500.5, 5)