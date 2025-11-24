import csv


def guardar_csv(inventario, ruta, incluir_header=True):

    if not inventario:
        print("\nNo se puede guardar: el inventario está vacío.")
        return

    try:
        with open(ruta, "w", newline="") as f:
            writer = csv.writer(f)

            # Escribe el encabezado
            if incluir_header:
                writer.writerow(["nombre", "precio", "cantidad"])

            # Escribe productos
            for p in inventario:
                writer.writerow([p["nombre"], p["precio"], p["cantidad"]])

        print(f"\nInventario guardado en: {ruta}")

    except PermissionError:
        print("\nError: No tienes permisos para escribir en esa ruta.")
    except Exception as e:
        print(f"\nError inesperado al guardar CSV: {e}")

def cargar_csv(ruta):

    # Carga un archivo CSV y retorna una lista de productos válidos.
    # También retorna cuántas filas inválidas se omitieron.


    productos_cargados = []
    filas_invalidas = 0

    try:
        with open(ruta, "r") as f:
            reader = csv.reader(f)
            rows = list(reader)

        # Valida el encabezado
        if not rows:
            print("\nEl archivo está vacío.")
            return [], 0

        encabezado = [col.strip().lower() for col in rows[0]]

        if encabezado != ["nombre", "precio", "cantidad"]:
            print("\nEncabezado inválido. Debe ser: nombre,precio,cantidad")
            return [], 0

        # Procesar filas
        for row in rows[1:]:
            if len(row) != 3:
                filas_invalidas += 1
                continue

            nombre, precio, cantidad = row

            try:
                precio = float(precio)
                cantidad = int(cantidad)

                if precio < 0 or cantidad < 0:
                    filas_invalidas += 1
                    continue

                productos_cargados.append({
                    "nombre": nombre.strip(),
                    "precio": precio,
                    "cantidad": cantidad
                })
            except ValueError:
                filas_invalidas += 1

        return productos_cargados, filas_invalidas

    except FileNotFoundError:
        print("\nArchivo no encontrado.")
        return [], 0
    except UnicodeDecodeError:
        print("\nError de lectura: el archivo no está en formato UTF-8.")
        return [], 0
        
