# 🧾 Sistema de Inventario en Python (CRUD + Persistencia CSV)

Este proyecto implementa un **sistema de inventario** en Python utilizando un menú interactivo que permite realizar operaciones **CRUD** (Crear, Leer, Actualizar, Eliminar), además de **guardar** y **cargar** datos desde archivos CSV.

Incluye:

- Manejo completo de inventario en memoria.
- Persistencia de datos en archivos CSV.
- Subflujos para guardar y cargar.
- Validación de datos.
- Cálculo de estadísticas.
- Menú principal interactivo.

---

## 📌 Funcionalidades

### 🔹 **1. Agregar producto**

Permite ingresar:

- Nombre del producto
- Precio
- Cantidad

Valida que los datos sean correctos antes de agregarlos al inventario.

---

### 🔹 **2. Mostrar inventario**

Muestra en pantalla todos los productos almacenados, con:

- Nombre
- Precio
- Cantidad

---

### 🔹 **3. Buscar producto**

Permite buscar un producto por nombre.

---

### 🔹 **4. Actualizar producto**

Permite modificar:

- Precio
- Cantidad

---

### 🔹 **5. Eliminar producto**

Elimina un producto por nombre.

---

### 🔹 **6. Estadísticas del inventario**

Calcula:

- Valor total del inventario.
- Cantidad total de productos.

---

### 🔹 **7. Guardar CSV**

Subflujo:

1. Usuario ingresa ruta del archivo.
2. Se valida ruta.
3. Se escribe el CSV.
4. Se confirma con un mensaje.

---

### 🔹 **8. Cargar CSV**

Subflujo:

1. Usuario ingresa ruta del archivo.
2. Se valida que sea CSV.
3. Si existe inventario, pregunta:
   - **Sobrescribir**
   - **Fusionar**
4. Actualiza inventario.
5. Muestra mensaje final.

## ▶️ Ejecución

Para ejecutar el programa:

```bash
python main.py
```
