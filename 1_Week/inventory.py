# Fundamentos y operaciones básicas del inventario


while True:
    #solicita datos al usuario - strip: elimina espacios en blanco
    print("--- ENTER PRODUCT DATA ---")
    product_name = input("Enter the product name: ").strip() 
     #valida que el nombre no este vacio
    if product_name:
        break
    else:
        print("Error: the name can not be empty.")


while True:
    #try-except para manejar errores
    try:
        price = float(input("Enter the price: "))
        if price >= 0:
            break
        else:
            print("Error: the price can not be negative.")
    except ValueError:
        print("Error: You must enter a valid number for the price.")
        
#valida que el precio sea un numero positivo
while True:
    try:
        amount = int(input("Enter the amount: "))
        if amount >= 0:
            break
        else:
            print("Error: the amount must be greater than 0.")
    except ValueError:
        print("Error: You must enter a valid integer. ")

print("\nData entered correctly:")
print(f"Name: {product_name}")
print(f"Price: {price}")
print(f"Amount: {amount}")

#se calcula el costo total de los productos
total_cost = price * amount

print(f"\nProduct: {product_name} | Price: {price} | Amount: {amount} | The total cost was: ", total_cost)