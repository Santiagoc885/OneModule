#APP.PY
#contiene el menú y la interacción con el usuario.


from services import add_inventory, show_inventory, search_product, update_product,delete_product, calcular_estadisticas

inventario = []
# add_inventory(inventario, "Lápiz", 500.0, 10)
# add_inventory(inventario, "Cuaderno", 1500.5, 5)
# show_inventory(inventario)
# print(calcular_estadisticas(inventario))



def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Agregar")
        print("2. Mostrar")
        print("3. Buscar")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Estadisticas")
        print("7. Guardar CSV")
        print("8. Actualizar CSV")
        print("9. Salir")
        opcion = input("Selecciona una opción (1-9): ").strip()
        if opcion == "1":
            add_inventory(inventario)
        elif opcion == "2":
            show_inventory(inventario)
        elif opcion == "3":
            nombre = input("Nombre a buscar: ").strip()
            producto = search_product(inventario, nombre)

            if producto:
                print("\n---- Producto encontrado ----")
                print(f"Nombre:   {producto['nombre']}")
                print(f"Precio:   {producto['precio']}")
                print(f"Cantidad: {producto['cantidad']}")
            else:
                print("\nProducto NO encontrado.")

        elif opcion == "4":
            nombre = input("Nombre del producto a actualizar: ").strip()

            nuevo_precio = input("Nuevo precio (dejar vacío para no cambiar): ").strip()
            nueva_cantidad = input("Nueva cantidad (dejar vacío para no cambiar): ").strip()

            # Convierte valores vacíos a None-vacios
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None
            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None

            exito = update_product(inventario, nombre, nuevo_precio, nueva_cantidad)

            if exito:
                print("\nProducto actualizado correctamente.")
            else:
                print("\nProducto NO encontrado.")

        elif opcion == "5":
            nombre = input("Nombre del producto a eliminar: ").strip()
            exito = delete_product(inventario, nombre)

            if exito:
                print("\nProducto eliminado correctamente.")
            else:
                print("\nProducto NO encontrado.")
  
            
        # elif opcion == "6":
        #     statistics()
        # elif opcion == "7":
        #     save_csv()
        # elif opcion == "8":
        #     upload_csv()
        elif opcion == "9":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida. Elige entre 1 y 9.")
menu()