import math
import random
 
 
def pedir_numero(mensaje, tipo=float):
    while True:
        try:
            valor = tipo(input(mensaje))
            if valor <= 0:
                print("  Error: el valor debe ser mayor que 0.")
                continue
            return valor
        except ValueError:
            print("  Error: ingrese un número válido.")
 
 
def en_elipse(x, y, a, b):
    return (x ** 2) / (a ** 2) + (y ** 2) / (b ** 2) <= 1
 
 
def en_hiperbola(x, y, c, d):
    return (x ** 2) / (c ** 2) - (y ** 2) / (d ** 2) >= 1
 
 
def monte_carlo(a, b, c, d, cantidad):
    n_elipse = 0
    n_inter = 0
    for _ in range(cantidad):
        x = random.uniform(-a, a)
        y = random.uniform(-b, b)
        if en_elipse(x, y, a, b):
            n_elipse += 1
            if en_hiperbola(x, y, c, d):
                n_inter += 1
    return n_elipse, n_inter
 
 
def main():
    a = pedir_numero("Ingrese a (elipse): ")
    b = pedir_numero("Ingrese b (elipse): ")
    c = pedir_numero("Ingrese c (hipérbola): ")
    d = pedir_numero("Ingrese d (hipérbola): ")
    cantidad = pedir_numero("Cantidad de puntos aleatorios: ", int)
 
    area_elipse = math.pi * a * b
    n_elipse, n_inter = monte_carlo(a, b, c, d, cantidad)
 
    print("\n--- RESULTADOS ---")
    print(f"Puntos dentro de la elipse: {n_elipse}")
    print(f"Puntos en la intersección elipse-hipérbola: {n_inter}")
    print(f"Área de la elipse: {area_elipse:.4f}")
 
    if n_elipse == 0:
        print("Ningún punto cayó en la elipse; aumente la cantidad de puntos.")
        return
 
    area_aprox = (n_inter / n_elipse) * area_elipse
    print(f"Área aproximada de la intersección: {area_aprox:.4f}")
 
 
if __name__ == "__main__":
    main()