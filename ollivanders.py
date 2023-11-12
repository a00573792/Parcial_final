# Crear variables para el conteo de clientes y el registro de compras
total_clientes = 0
clientes_que_compraron = 0
registro_compras = {}

def registrar_compra(varita):
    global clientes_que_compraron
    clientes_que_compraron += 1

    if 'Anónimo' in registro_compras:
        registro_compras['Anónimo'].append(varita)
    else:
        registro_compras['Anónimo'] = [varita]

def mostrar_registros():
    print("\nRegistro de compras:")
    for cliente, compras in registro_compras.items():
        print(f"{cliente}: {', '.join(compras)}")

# Función principal
def main():
    global total_clientes

    clientes_presentes = input("¿Hay clientes en la tienda? (s/n): ").lower()

    if clientes_presentes != 's':
        print("No hay clientes en la tienda. Programa terminado.")
        return

    while True:
        print("\nBienvenido a la tienda de varitas mágicas!")
        entrada_cliente = input("¿Compra una varita? (s/n): ").lower()

        if entrada_cliente != 's':
            break

        total_clientes += 1

        print("Opciones de varitas:")
        print("1. Varita de Saúco")
        print("2. Varita de Espino")
        print("3. Varita de Sauce")
        print("4. Varita de Acebo")

        opcion_varita = input("Seleccione el número de la varita que desea comprar: ")

        if opcion_varita in ['1', '2', '3', '4']:
            varita_elegida = {
                '1': 'Varita de Saúco',
                '2': 'Varita de Espino',
                '3': 'Varita de Sauce',
                '4': 'Varita de Acebo'
            }[opcion_varita]

            registrar_compra(varita_elegida)
            print(f"¡Compra registrada! Varita comprada: {varita_elegida}.")
        else:
            print("Opción no válida. Por favor, seleccione un número de varita válido.")

    print(f"\nTotal de clientes que entraron a la tienda: {total_clientes}")
    print(f"Total de clientes que compraron varitas: {clientes_que_compraron}")
    mostrar_registros()

if __name__ == "__main__":
    main()
