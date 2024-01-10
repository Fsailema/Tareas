
def conversor():
    temp = input("Ingrese la temperatura   ")
    unidad = temp[-1].upper()
    grados = float(temp[:-1])

    if unidad == "C":
        temp_conv = round(grados * (9/5) + 32, 1)
        print(f"{grados}°{unidad} es equivalente a {temp_conv}°F")

    else:
        temp_conv = round((grados - 32) * (5/9), 1)
        print(f"{grados}°{unidad} es equivalente a {temp_conv}°C")

conversor()

