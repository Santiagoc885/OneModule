#Control de flujo y manejo de listas en el inventario

inventory = []

def menu():
    while True:
        print("\n====== MENÚ PRINCIPAL ======")
        print("1. Agregar producto al inventario.")
        print("2. Mostrar inventario.")
        print("3. Calcular estadísticas del inventario.")
        print("4. Salir")

        choice = input("Elige una opción (1-4): ")

        
        if choice == "1":
            # Valida el nombre del producto
            while True:
                print("\n--- Agregar producto ---")
                product_name = input("Ingresa el nombre del producto: ").strip()
                if product_name:
                    break
                else:
                    print("El producto no puede ser vacio")

            # Validar precio
            while True:
                try:
                    price = float(input("Ingresa el precio: "))
                    if price >= 0:
                        break
                    else:
                        print("El precio debe ser mayor o igual a 0.")
                        
                except ValueError:
                    print("Opción invalida. Intente de nuevo.")

            # Validar cantidad
            while True:
                try:
                    amount = int(input("Ingresa la cantidad del producto: "))
                    if amount >= 0:
                        break
                    else:
                        print("La cantidad no puede ser negativa.")
                except ValueError:
                    print("Opción invalida. Intente de nuevo.")

            # Guardar producto
            product = {
                "Nombre producto": product_name,
                "Precio": price,
                "Cantidad": amount
            }
            inventory.append(product)
            print("\nProducto agregado correctamente")


        elif choice == "2":
            if not inventory:
                print("\nEl inventario esta vacio.")
            else:
                print("\n--- INVENTARIO ---")
                for idx, product in enumerate(inventory, start=1):
                    print(f"{idx}. Producto: {product['Nombre producto']} | Precio: {product['Precio']} | Cantidad: {product['Cantidad']}")

        elif choice == "3":
            if not inventory: #si inventario esta vacio
                print("\nEl inventario esta vacio.")
            else:
                total_value = sum(p['Precio'] * p['Cantidad'] for p in inventory)
                total_items = sum(p['Cantidad'] for p in inventory)

                print(f"\nValor total del inventario: {total_value}")
                print(f"Número total de artículos en inventario: {total_items}")

        elif choice == "4":
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

menu()
