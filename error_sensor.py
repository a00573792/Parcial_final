def calcular_porcentaje_error(lecturas):
    total_lecturas = len(lecturas)
    lecturas_fuera_rango = sum(1 for lectura in lecturas if lectura < 10 or lectura > 40)
    porcentaje_error = (lecturas_fuera_rango / total_lecturas) * 100

    return porcentaje_error

def main():
    try:
        num_lecturas = int(input("Ingrese el número de lecturas del sensor de temperatura: "))
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        return

    lecturas_sensor = []

    for i in range(num_lecturas):
        while True:
            try:
                lectura = float(input(f"Ingrese la lectura {i + 1} del sensor: "))
            except ValueError:
                print("Error: Ingrese un número válido.")
                continue

            lecturas_sensor.append(lectura)
            break

    porcentaje_error = calcular_porcentaje_error(lecturas_sensor)

    print(f"\nPorcentaje de lecturas fuera del rango: {porcentaje_error:.2f}%")
    print(f"Total de lecturas: {num_lecturas}")

if __name__ == "__main__":
    main()
